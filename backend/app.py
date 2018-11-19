import copy
from bson import objectid
from eve import Eve
from flask import request, current_app, abort

app = Eve(settings="settings.py")
mongo = app.data.driver


def update_frames(frames, pins_knocked_down):
    """Add a new roll to a set of frames

    Args:
        frames (list(list)): A list of frames in the game. Cannot be more than 10.
        pins_knocked_down (number): The number of pins knocked down on this roll

    Returns:
        list: The updated frame
    """

    # if no previous frames return new frame
    if not frames:
        return [[pins_knocked_down]]

    if len(frames) > 10:
        abort(400, "A game cannot have more than 10 frames.")

    if len(frames) == 10 and len(frames[-1]) > 2:
        abort(400, "Last frame cannot have more than three rolls.")

    if pins_knocked_down > 10:
        abort(400, "Invalid pin value.")

    # deep copy isn't really necessary here but helps in testing
    new_frames = copy.deepcopy(frames)
    # check if previous frame is full or strike.  last frame can have more than two rolls
    if (len(new_frames[-1]) == 2 or new_frames[-1][0] == 10) and len(frames) != 10:
        new_frames.append([pins_knocked_down])
    else:
        # check to see if pin number is valid
        if new_frames[-1][0] + pins_knocked_down > 10:
            abort(400, "Invalid pin value.")

        new_frames[-1].append(pins_knocked_down)
    return new_frames


def score_frames(frames):
    """Reads the list of frames and returns the score

    Args:
        frames (list): A list of lists representing the pins knocked down in each frame

    Returns:
        number: The score total of the frames. Returns None if the score can't be tallied.
        e.g. a stike has been scored, but their have not been two subsequent rolls.
    """

    score = 0
    for idx, frame in enumerate(frames):
        if len(frame) == 1:
            # strike or not full
            if frame[0] != 10:
                pass  # don't total incomplete frames
            else:
                # handle strikes
                num_frames = len(frames)
                if idx + 1 == num_frames or (len(frames[idx + 1]) == 1 and idx + 2 == num_frames):
                    pass  # not enough rolls for calculation
                elif len(frames[idx + 1]) > 1:
                    # next frame includes two rolls
                    score += 10 + sum(frames[idx + 1][:2])
                elif idx + 2 < len(frames) and len(frames[idx + 1]) == 1:
                    # there are two more frames and the next frame is a strike
                    score += 20 + frames[idx + 2][0]
        elif sum(frame) < 10:
            # regular addition if not a spare
            score += sum(frame)
        elif idx == 9:
            # last frame
            if len(frame) == 2 and sum(frame) < 10:
                # regular addition
                score += sum(frame)
            elif frame[0] == 10 and len(frame) < 3:
                pass  # for more rolls
            elif len(frame) == 2 and sum(frame[:2]) == 10:
                pass  # for more rolls (spare)
            else:
                # valid srike or spare
                score += sum(frame)
        elif sum(frame) == 10:
            # spares
            num_frames = len(frames)
            if idx + 1 == num_frames:
                pass  # not enough rolls for calculation
            else:
                score += 10 + frames[idx + 1][0]

    return score or None


def update_game_score(rolls):
    """Update the game with newly knocked down pins.

    Args:
        rolls (list(dict)): A list rolls with the player_id and the number of pins knocked down.
        Dict schema defined by roll_schema.
    """

    # fetch the game object
    game_object_id = objectid.ObjectId(request.view_args["game_id"])
    game_query = {"_id": game_object_id}
    game = mongo.db.games.find_one(game_query)

    if game is None:
        abort(404, "Game not found.")
    else:
        for roll in rolls:
            # convert player_id from objet id to string for lookup
            player_id = str(roll["player_id"])

            if player_id not in game["players"]:
                abort(400, "Player not in game.")

            previous_frames = game["players"][player_id]["frames"]
            new_frames = update_frames(previous_frames, roll["pins_knocked_down"])
            roll["frames"] = new_frames
            game["players"][player_id]["frames"] = new_frames

            score = score_frames(new_frames)
            roll["score"] = score
            game["players"][player_id]["score"] = score

            current_app.data.driver.db.games.update_one({"_id": game_object_id}, {"$set": {f"players.{player_id}": game["players"][player_id]}})


def create_new_game(items):
    """Mutate the inital game objet passed by the user.

    Args:
        items (dict): A dictionay with the current bowling lane and a list of the player ids playing in the game
    """

    for item in items:
        players = item["players"]
        item["players"] = {}
        for player in players:
            item["players"][str(player)] = {"frames": [], "score": None}


app.on_insert_games += create_new_game
app.on_insert_roll += update_game_score

if __name__ == "__main__":
    app.run(host="0.0.0.0")

from app import update_frames, score_frames

single_strike_frame = [[10]]  # None
last_frame_strike = [[2, 3], [5, 4], [10]]  # 14
last_frame_full = [[2, 3], [5, 4], [5, 5]]  # 14
last_frame_open = [[2, 3], [5, 4], [5]]  # 14
basic_unfinished = [[2, 3], [5, 4], [5, 1]]  # 20
three_strike_frame = [[10], [10], [10]]  # 30
four_strike_frame = [[10], [10], [10], [10]]  # 60
five_strike_frame = [[10], [10], [10], [10], [10]]  # 90
my_typical_game = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]  # 300
full_test = [[10], [7, 3], [9, 0], [10], [0, 8], [8, 2], [0, 6], [10], [10], [10, 8, 1]]  # 167
basic_spare_frame = [[2, 3], [5, 5], [5, 1]]  # 26
full_test_two = [[9, 1], [0, 10], [10], [10], [6, 2], [7, 3], [8, 2], [10], [9, 0], [9, 1, 10]]  # 168


class TestScoring(object):
    def test_update_frames_len(self):
        assert len(update_frames(single_strike_frame, 10)) == 2
        assert len(update_frames(last_frame_strike, 3)) == 4
        assert len(update_frames(last_frame_full, 3)) == 4
        assert len(update_frames(last_frame_open, 3)) == 3

    def test_update_frames(self):
        assert update_frames([], 10) == [[10]]
        assert update_frames([[10]], 10) == [[10], [10]]
        assert update_frames([[10], [10]], 10) == [[10], [10], [10]]
        assert update_frames([[10], [10], [10]], 10) == [[10], [10], [10], [10]]
        assert update_frames([[10], [10], [10], [10]], 10) == [[10], [10], [10], [10], [10]]
        assert update_frames([[10], [10], [10], [10], [10]], 10) == [[10], [10], [10], [10], [10], [10]]

    def test_first_roll(self):
        assert score_frames([[1]]) is None
        assert score_frames([[3]]) is None
        assert score_frames(single_strike_frame) is None

    def test_preset_frames(self):
        assert score_frames(last_frame_strike) == 14
        assert score_frames(last_frame_full) == 14
        assert score_frames(last_frame_open) == 14
        assert score_frames(basic_unfinished) == 20
        assert score_frames(three_strike_frame) == 30
        assert score_frames(four_strike_frame) == 60
        assert score_frames(five_strike_frame) == 90
        assert score_frames(my_typical_game) == 300

    def test_spares(self):
        assert score_frames(full_test_two) == 168
        assert score_frames(full_test) == 167
        assert score_frames(basic_spare_frame) == 26

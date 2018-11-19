dart-bowl

![bowling gif](https://thumbs.gfycat.com/ThickLinearGoldenretriever-size_restricted.gif)

CHALLENGE:
The challenge is to implement a bowling scoring REST API (and optional front end). Basically, something that takes in pins knocked down for players and keeps track of them and calculates and provides their scores. If you were in a bowling alley and looked at the display, it would be the service that powered the numbers behind the display.

For this, you don't have to implement a ton of bells and whistles. Instead, we're looking for production-quality code that's well-tested and well-documented. The scoring part of it is the main thing we're looking for and how you model the data, etc. It would be best to show your usage of a REST framework of sorts and you can use any modern language that you'd like. Additionally, the solution should score as the game progresses rather than just at the end.

Here's some information on bowling scoring for reference:  
http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm


## Usage
Dependencies: make and docker.

To build local backend container:
`make build-backend-docker-container`

To run the stack:
`make up-fullstack`

This will launch the app at localhost:5000.

To run tests:
Bring the fullstack up with `make up-fullstack`.
Mount into the python container with `make mount-into-fullstack`
Run `make test-fullstack`

Postman collection with the basic operations: https://www.getpostman.com/collections/8017e9461cc7516dc60b

Other notes:
* Wanted a sweet docker-compose setup so we wouldn't have to deal with dependency issues.
* Tabnine is cool. This was my first time using it and it was interesting to use.
* Moved from flask to eve to target the `usage of a REST framework` mention and to learn more about eve.
* 'DB is cheap' so there is some duplicated data between rolls and a game object
* Gutter balls are posted as 0's, strikes as 10
* Don't really need player objects

Known issues:
* Errors in testing should return the api error response, also testing should be easier
* Testing has both unit and integration test which I have mixed feelings about.  (More bang for your buck with integration tests, but I might move their use to a determined stage in the development pipeline or use mocks underneath)
* There is some db mutation remaining after the tests run
* Running the tests shouldn't require the stack to be previously mounted and cause the server to restart.
* I'd be worthwhile to move the game logic out of app.py

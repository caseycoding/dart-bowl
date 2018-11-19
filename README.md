dart-bowl

![bowling gif](https://thumbs.gfycat.com/ThickLinearGoldenretriever-size_restricted.gif)

## Usage
Dependencies: make and docker.

To build local backend container:  
`make build-backend-docker-container`

To run the stack:  
`make up-fullstack`

This will launch the app at localhost:5000.

To run tests:  
Bring the fullstack up with `make up-fullstack`.  
Mount into the python container with `make mount-into-fullstack`.  
Run `make test-fullstack`

Postman collection with the basic operations: https://www.getpostman.com/collections/8017e9461cc7516dc60b

## Other notes:
* Wanted a sweet docker-compose setup so we wouldn't have to deal with dependency issues.
* Tabnine is cool. This was my first time using it and it was interesting to use.
* Moved from flask to eve to target the `usage of a REST framework` mention and to learn more about eve.
* 'DB is cheap' so there is some duplicated data between rolls and a game object
* Gutter balls are posted as 0's, strikes as 10
* Don't really need player objects

## Known issues:
* Errors in testing should return the api error response
* Testing has both unit and integration test which I have mixed feelings about.  (More bang for your buck with integration tests, but I might move their use to a determined stage in the development pipeline or use mocks underneath)
* There is some db mutation remaining after the tests run
* Running the tests shouldn't require the stack to be previously mounted and cause the server to restart.
* I'd be worthwhile to move the game logic out of app.py
* Could use some logging improvements (or something like sentry)

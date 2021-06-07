# Raid Boss as a Service (RBaaS)

Just a quick project to practice asyncio and other tools. 

Goals:
- Build a basic service that handles basic requests with a 'long' response time
- Fight the urge to use Flask and use Django instead
- Build out a script to action on the service and handle multiple slow requests async-ly
- Use attrs to see what it offers me on a basic level

## Usage
```
# Makefile should handle most actions
% make help
drop_db                        "Drop" the db
help                           Print this message
install                        Install requirements for entire app
populate_db                    Populate db with some test data for tests
run                            Run the warrior app against a Django server
test                           Integration test for warrior app
up                             Start Django app
```

## Notes
* Barebones project, just wanted something to work on to mess with async and learning a bit more Django.

* Warrior app is just getting familiar with aiomultiprocessing, did some extra testing, but did not commit.

* Docker should've been used for Make actions.

* Mocking async stuff was significantly harder than anticipated, will revisit
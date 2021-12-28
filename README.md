
# CSMS (Charging Station Management System)
a simple implementation of a csms rating restful api with flask as http router and marshmallow for a basic input data validation.
- how to run: 

``
  step 1: prepare your virtualenv: pip3 install virtualenv
``

``
  step 2: install dependencies: pip3 install -r requirements.txt
``

- to run tests:
```
python3 -m unittest discover -vs tests
```
- to run the app:
```
python3 ./run.py
```

- run with docker:
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

----------------------------------------------------

- the main issue with this endpoint is that we receive the rates which we use to calculate the price from client,
I don't think it's the safest approach from the business perspective, there if the rates varies from different 
charging stations there should be a trusted origin on backend where we can validate the given price from client.
or some kind of stateless jwt token to store these parameters(rate and etc). 
- same goes for other parameters that will be calculated like traveled meter, we could use a authentication method for 
- this api or just trust the data in request.
- api responses should have a standard structure, with status code, message and optional warning message.

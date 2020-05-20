# API crud for book registration.
<hr>

The application is functional on the Heroku website:
https://olist-api-crud.herokuapp.com/

In the root folder of the code insert the following command `docker-compose up -d` the application will be mounted in a docker container and will be available on port 5000.


The tests are in the SRC folder and have the name tests.py to run the tests type `python src/tests.py`

To insert the authors, the `python src/insert.py` code must be run.

To post new books use the example:

`{
	"name": "test01",
    "publication_year": 2019, 
    "edition": "2 edition", 
    "author": ["5ec44e21fc4168f0e37b1d74"]
}`
# MongoDB CRUD app

###### 2022 Dmytro Dziubenko

---

## This application is capable for

-    connect:
    1. server (use environment variable for safety)
    2. database
    3. collection

-    retreive:
    1. all databases
    2. all collections in selected database
    3. all documents in selected collection
    4. all documents in selected collection using filters

-    insert:
    1. one document to collection
    2. many documents to collection

-    update:
    1. one document in collection
    2. many documents in collection

-    delete:
    1. one document in collection
    2. many documents in collection

## Instalation
---

- Clone the project from repository.

        $ git clone https://github.com/Dima418/mongo_crud_app.git

- Change working directory.

        $ cd mongo_crud_app

- *Install and run `python venv` or `virtualenv`*.

- *Install `pip`*.

- Install requirements.

        $ pip install -r reqirements.txt

- Add MongoDB connection string to enviroment varable `MONGO_URL`. See MongoDB [Connection String URI Format](https://www.mongodb.com/docs/manual/reference/connection-string/).
    - Linux/Ubuntu:

            $ export MONGO_URL=<connection string>

    - Windows:

            $ set MONGO_URL=<connection string>

- Start application.
    - Linux/Ubuntu:

            $ python3 app.py

    - Windows:

            $ python app.py

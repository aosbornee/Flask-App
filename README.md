# Flask Web Page Application

Flask is a micro web framework, it is usually referred to as a 'do it yourself' package as it is very lightweight and doesnt' come with any
built in packages.

It is very beneficial for beginners to initially use flask as there are less layers of abstraction and the useer has
more of a hands on approach as they have to create most of the functionality themselves.

## About the Application

- This Application contains a Login Page, SignUp page, A profile page and the ability to do a Python quiz. Login details
are connected to a database and thus kept persistent when the user returns to the web site. Passwords are also hashed
to ensure encryption has taken place

## How to create the Application


- Flask allows us to use template inheritance, this means that if we have common themes that would present in all of our
web pages then we can inherit this from one file, this file is conventionally called 'base.html'

- FLask-SQLAlchemy allows us to create databases, in this module we represent tables using classes

```python
class User(User, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    created = db.Column(db.DateTime)
```
As you can see we have created a table which will store the information of our users


## How to run the Application

- Once the app has been downloaded onto an IDE, to be able to use it you must first run the command
``` SET FLASK_APP=project``` after this we can then do ``` flask run```

- This command will open the app on local host port 5000

## Future Iterations for this Application

- I hope to be able to connect this app to a Virtual Machine which would run the app on a web server, bringing multiple
topics together
- Additionally, I aim to create harder difficulties of the test
- Currently answers to the quiz is stored in a python list, I aim to put these answers in a database and thus when a user
inputs an answer it will be checked against the info in the db




## Creating the Database
- In the Python REPL
- from project import db, create_app
- db.create_all(app=create_app())

## Running the App
- SET FLASK_APP=project allows to use 'flask run'
- SET FLASK_ENV=development allows us to use dev mode





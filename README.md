




## Creating the Database
- In the Python REPL
- from project import db, create_app
- db.create_all(app=create_app())

## Running the App
- SET FLASK_APP=project allows to use 'flask run'
- SET FLASK_ENV=development allows us to use dev mode


## Common Errors:

- Be sure not to run many sessions in the terminal, as they would interfere with each other
- Sometimes I may need to restart my browser/Pycharm for some of the changes to take effect (could be due to multiple cookies while I try to login)
- Refer to documentation!
- Make sure to name my variables different names to my functions!!!, Spent ages troubleshooting my 'answers' variable issue which was due to me also having a route function called 'answers'
- TypeError: 'function' object is not subscriptable and AttributeError: 'function' object has no attribute 'get' were the two errors I was receiving


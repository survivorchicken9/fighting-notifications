import os
from flask import Flask
from views.home import home_blueprint


app = Flask(__name__)
app.secret_key = os.urandom(64)

app.register_blueprint(home_blueprint)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from data import db_session
import api

app = Flask(__name__)


def main():
    db_session.global_init("db/db_products.db")
    app.register_blueprint(api.blueprint)
    app.run()


if __name__ == '__main__':
    main()

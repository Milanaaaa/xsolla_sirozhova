from flask import Flask
from data import db_session
import api
import os

app = Flask(__name__)


def main():
    db_session.global_init("db/db_products.db")
    app.register_blueprint(api.blueprint)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)


if __name__ == '__main__':
    main()

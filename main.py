from flask import Flask
from data import db_session
import api
import os
from data.api_root import port_num

app = Flask(__name__)


def main():
    db_session.global_init("db/db_products.db")
    app.register_blueprint(api.blueprint)
    port = int(os.environ.get('PORT', port_num))
    app.run(port=port)


if __name__ == '__main__':
    main()

from flask import Flask

from src.settings import settings
from src.routes.monitoring_routes import api_routes as monitor_api


def start_app():
    print("start app..")
    app: Flask = Flask(__name__)
    app.register_blueprint(monitor_api)
    print("start translators..")
    # for i in range(settings.translators_count):
    #     translator = get_translator()
    #     translator.start()
    # app.run(debug=settings.debug, port=settings.port)

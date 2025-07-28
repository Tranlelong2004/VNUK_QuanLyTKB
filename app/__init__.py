from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Trang chủ Flask đã hoạt động!"

    return app

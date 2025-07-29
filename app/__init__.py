from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_super_secret_key_here'

    from app.login.routes import login_bp  # ✅ Import TRỰC TIẾP tránh vòng tròn
    app.register_blueprint(login_bp, url_prefix='/login')
    # Đăng ký Blueprint cho module timetable (MỚI)
    from app.timetable.routes import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/timetable')
    return app

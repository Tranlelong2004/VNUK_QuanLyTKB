from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    captcha = StringField('Mã xác thực', validators=[DataRequired(), Length(min=4, max=6)])
    submit = SubmitField('Đăng nhập')
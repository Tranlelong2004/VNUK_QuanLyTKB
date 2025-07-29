from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.login.forms import LoginForm

login_bp = Blueprint('login_bp', __name__, template_folder='templates')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        captcha = form.captcha.data

        # Giả lập kiểm tra captcha
        if captcha.upper() != 'VNUK26':  # Captcha tĩnh cho ví dụ
            flash('Mã xác thực không đúng.', 'danger')
            return render_template('', form=form, current_captcha='VNUK26')

        # --- Logic giả lập thành công/thất bại (không có DB) ---
        # Bạn có thể thay đổi điều kiện này để mô phỏng các trường hợp khác nhau
        if email == 'test@example.com' and password == 'password':
            flash('Đăng nhập thành công! (Không dùng DB)', 'success')
            # Trong thực tế, bạn sẽ chuyển hướng đến trang chính
            # return redirect(url_for('some_other_page'))
        else:
            flash('Email hoặc mật khẩu không đúng. (Không dùng DB)', 'danger')
        # -------------------------------------------------------

    # Captcha tĩnh cho ví dụ, trong thực tế sẽ được tạo động
    current_captcha = 'VNUK26'
    return render_template('login.html', form=form, current_captcha=current_captcha)
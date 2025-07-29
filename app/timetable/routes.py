from flask import render_template, Blueprint

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates')

@dashboard_bp.route('/', methods=['GET'])
def index():
    # Dữ liệu mẫu cho sidebar và nội dung chính
    sidebar_items = [
        {'name': 'Trang chủ', 'icon': 'fas fa-home', 'link': '#', 'active': False},
        {'name': 'Lộ trình học tập', 'icon': 'fas fa-book', 'link': '#', 'active': False},
        {'name': 'Giảng viên', 'icon': 'fas fa-user-tie', 'link': '#', 'active': False},
        {'name': 'Phòng học', 'icon': 'fas fa-building', 'link': '#', 'active': False},
        {'name': 'Học phần', 'icon': 'fas fa-graduation-cap', 'link': '#', 'active': False},
        {'name': 'Sinh viên/Lớp học', 'icon': 'fas fa-users', 'link': '#', 'active': False},
        {
            'name': 'Thời khóa biểu',
            'icon': 'fas fa-calendar-alt',
            'link': '#',
            'active': True,
            'has_submenu': True,
            'expanded': True,
            'submenu_items': [
                {'name': 'Báo cáo thống kê', 'link': '#', 'active': False},
                {'name': 'Duyệt yêu cầu thời khóa biểu', 'link': '#', 'active': False},
            ]
        },
        {'name': 'Đăng kí học phần', 'icon': 'fas fa-plus-square', 'link': '#', 'active': False, 'has_submenu': True},
        {'name': 'Hủy học phần', 'icon': 'fas fa-minus-square', 'link': '#', 'active': False, 'has_submenu': True},
        {'name': 'Báo cáo', 'icon': 'fas fa-chart-bar', 'link': '#', 'active': False},
        {'name': 'Cài đặt', 'icon': 'fas fa-cog', 'link': '#', 'active': False},
    ]

    return render_template('timetable.html', sidebar_items=sidebar_items)

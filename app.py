from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# Cấu hình cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'supersecret'

# Khởi tạo SQLAlchemy
db = SQLAlchemy(app)

# Mô hình dữ liệu
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

# Khởi tạo Flask-Admin
admin = Admin(app, name="Admin Panel", template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    # Tạo cơ sở dữ liệu nếu chưa có
    with app.app_context():
        db.create_all()
    app.run(debug=True)

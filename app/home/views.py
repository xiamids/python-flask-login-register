from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.home.forms import RegistForm, LoginForm
from app.models import User, db, UserLog
from datetime import datetime
from werkzeug.security import generate_password_hash
from functools import wraps


# 登录装饰器
def user_login_req(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("home.login"))
        return func(*args, **kwargs)
    return decorated_function


# 前端首页
@home.route("/")
def index():
    return render_template("home/index.html")


# 用户中心
@home.route("/user")
@user_login_req
def user():
    return render_template("home/user.html")


# 用户登录
@home.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if user.check_pwd(data["pwd"]):
            userlog = UserLog(
                user_id=user.id,
                ip=request.remote_addr
            )
            db.session.add(userlog)
            db.session.commit()
            session["name"] = user.name
            return redirect(url_for("home.user"))
    return render_template("home/login.html", form=form)


# 退出登录
@home.route("/logout",methods=["GET", "POST"])
def logout():
    form = LoginForm()
    if 'name' in session:
        session.clear()
        return redirect(url_for("home.login"))

    return render_template("home/login.html", form=form)


# 会员注册
@home.route("/register", methods=["GET", "POST"])
def register():
    form = RegistForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["pwd"]),
            addtime=datetime.now()
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功", "ok")
    return render_template("home/register.html", form=form)

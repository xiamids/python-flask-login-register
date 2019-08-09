from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired, EqualTo,  ValidationError
from app.models import User

class RegistForm(FlaskForm):

    name = StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class":"form-control input-lg",
            "placeholder":"在这里填写昵称！"
        }
    )

    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class":"form-control input-lg",
            "placeholder": "在这里填写密码！"
        }
    )
    repwd = PasswordField(
        label="确认密码",
        validators=[
            DataRequired("请输入密码！"),
            EqualTo('pwd',message="两次输入密码不一致！")
        ],
        description="确认密码",
        render_kw={
            "class":"form-control input-lg",
            "placeholder": "再次输入密码！"
        }
    )

    submit = SubmitField(
        label="提交注册",
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )

    def validate_name(self,field):
        name=field.data
        user=User.query.filter_by(name=name).count()
        if user==1:
            raise ValidationError("昵称已经存在！")


class LoginForm(FlaskForm):

    name = StringField(
        label="账户",
        validators=[
            DataRequired("请输入账户！")
        ],
        description="账户",
        render_kw={

            "class":"form-control input-lg",
            "placeholder":"在这里填写账户！"
        }
    )

    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class":"form-control input-lg",
            "placeholder": "在这里填写密码！"
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-lg btn-success btn-block"
        }
    )



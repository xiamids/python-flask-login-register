#coding utf8
# 定义蓝图
from flask import Blueprint

admin = Blueprint("admin",__name__)

import app.admin.views

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict


db = SQLAlchemy()


#: config_name:配置名称
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    db.init_app(app)
    register_blueprints(app)

    return app


# 注册蓝图
def register_blueprints(app):
    from views import blueprints
    for view, url_prefix in blueprints:
        app.register_blueprint(view, url_prefix=url_prefix)
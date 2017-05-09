#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_sockets import Sockets
from app.config import config_dict, base
from celery import Celery


db = SQLAlchemy()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main_auth.admin_login'
login_manager.login_message = u'请先登录'


sockets = Sockets()


celery = Celery(__name__, broker=base.CELERY_BROKER_URL)


#: config_name:配置名称
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    db.init_app(app)
    register_blueprints(app)
    sockets.init_app(app)

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()

    celery.conf.update(app.config)

    return app


# 注册蓝图
def register_blueprints(app):
    from views import blueprints
    from app.api import blueprints as bp_api
    for view, url_prefix in blueprints:
        app.register_blueprint(view, url_prefix=url_prefix)

    for view_api, url_prefix_api in bp_api:
        app.register_blueprint(view_api, url_prefix=url_prefix_api)
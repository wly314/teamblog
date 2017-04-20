#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import *


"""文章表"""
class Account(Base, db.Model):

    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    # 用户名　仅限邮箱注册
    username = db.Column(db.Text, nullable=False, index=True)
    # 密码加密
    password_hash = db.Column(db.Text, nullable=False)
    # 激活状态
    active = db.Column(db.Boolean, nullable=False, server_default='false')
    # 锁定状态
    locked = db.Column(db.Boolean, nullable=False, server_default='false')
    # 昵称
    nickname = db.Column(db.Text, server_default='')
    # 性别 0男　１女
    gender = db.Column(db.Boolean, server_default='false')
    # 出生日期
    birth_date = db.Column(db.DateTime, server_default=func.now())
    # 个人简介
    introduction = db.Column(db.Text, server_default='')
    # 删除标志
    delete = db.Column(db.Boolean, server_default='false')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import *


"""文章表"""
class Article(Base, db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.Text, nullable=False, index=True)
    # 内容
    content = db.Column(db.Text, server_default='')
    # 作者
    author_id = db.Column(db.Integer, db.ForeignKey('v1.id'), server_default=0, index=True)
    # 删除标志
    delete = db.Column(db.Boolean, server_default='false')
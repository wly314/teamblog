#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template


article_bp = Blueprint('views_article', __name__, template_folder='templates')


@article_bp.route('/article/writer/')
def index():
    return render_template('article/post_article.html')
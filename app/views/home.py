#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template


home_bp = Blueprint('views_home', __name__, template_folder='templates')


@home_bp.route('/')
def index():
    return render_template('home/index.html')
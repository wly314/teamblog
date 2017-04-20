#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template


account_bp = Blueprint('views_account', __name__, template_folder='templates')


@account_bp.route('/')
def index():
    return render_template('home/index.html')
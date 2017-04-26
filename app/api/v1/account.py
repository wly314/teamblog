#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template


account_bp = Blueprint('api_account', __name__, template_folder='templates')


@account_bp.route('/auth/register')
def register():
    return "good"


@account_bp.route('/auth/login')
def login():
    return render_template('account/login.html')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
from app.forms.account_form import RegisterForm
from app import sockets


account_bp = Blueprint('views_account', __name__, template_folder='templates')


@account_bp.route('/auth/register', methods=['POST', 'GET'])
def register():
    _registerForm = RegisterForm()

    if request.method == 'POST':
        print (3333333333333333333333333333333)
    if _registerForm.validate_on_submit():
        print (1111111111111111)
        pass
    return render_template('account/register.html',
                           form=_registerForm)


@account_bp.route('/auth/login')
def login():
    return render_template('account/login.html')
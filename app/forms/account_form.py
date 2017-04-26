#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = StringField('password')


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
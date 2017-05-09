#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import *


DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:pgsql@127.0.0.1:5432/teamblog'
SQLALCHEMY_TRACK_MODIFICATIONS = True

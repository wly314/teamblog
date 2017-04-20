#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from sqlalchemy.sql import func


"""表基础"""


class Base(object):
    create_time = db.Column(db.DateTime, server_default=func.now(), index=True)
    modified_time = db.Column(db.DateTime, server_default=func.now(), index=True)
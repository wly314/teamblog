#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


CSRF_ENABLED = True
SECRET_KEY = 'team_blog_is_very_safe'


CELERY_BROKER_URL = 'redis://:wly314@localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://:wly314@localhost:6379/0'
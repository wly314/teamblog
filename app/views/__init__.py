#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .home import home_bp
from .account import account_bp


# 蓝图列表
blueprints = [(home_bp, ''),
              (account_bp, ''),]
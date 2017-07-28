#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:58:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from app import app


@app.task
def add(a, b):
    return a + b
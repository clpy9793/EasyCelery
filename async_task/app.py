#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:07:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from celery import Celery


# app = Celery('app', broker='pyamqp://localhost', backend='redis://localhost')

app = Celery('app', 
            broker='pyamqp://localhost', 
            backend='redis://localhost',
            include=['task'])            




if __name__ == '__main__':
    app.start()
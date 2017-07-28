#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:58:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
from app import app
from celery.schedules import crontab


@app.task
def close_unsolved_questions():
    '''定时删除未解决的问题'''
    print(close_unsolved_questions.__name__)
    pass


@app.task
def on_push_recommend_post_on_morning():
    '''定时推送推荐文章'''
    print('morning')
    pass


@app.task
def on_push_recommend_post_on_evening():
    '''定时推送推荐文章'''
    print('evening')
    pass
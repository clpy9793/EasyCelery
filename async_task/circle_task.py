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
def on_push_recommend_post():
    '''定时推送推荐文章'''
    pass

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(1, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)    


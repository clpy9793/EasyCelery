#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:07:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
celery -A app worker -B -l info
'''
import os
from celery import Celery
from celery.schedules import crontab


# app = Celery('app', broker='pyamqp://localhost', backend='redis://localhost')
tasks = ['task', 'circle_task']
app = Celery('app', broker='pyamqp://localhost', backend='redis://localhost',include=tasks)

# circle_server
circle_beat_schedule = {
    'circle_every_day': {
        'task': 'circle_task.close_unsolved_questions',
        'schedule': crontab(hour=8),
        'args': (),
    },
    'circle_every_day': {
        'task': 'circle_task.on_push_recommend_post_on_morning',
        'schedule': crontab(hour=7),
        'args': (),
    },
    'circle_every_day': {
        'task': 'circle_task.on_push_recommend_post_on_evening',
        'schedule': crontab(hour=21),
        'args': (),
    },    
}

app.conf.beat_schedule.update(circle_beat_schedule)

if __name__ == '__main__':
    app.start()
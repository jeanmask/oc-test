# -*- coding: utf-8 -*-

from celery import Celery
from pusher import Pusher

import settings


def _pusher():
    return Pusher(app_id=settings.PUSHER_APP_ID,
                  key=settings.PUSHER_KEY,
                  secret=settings.PUSHER_SECRET,
                  ssl=True)



app = Celery('oc-test')
app.config_from_object(settings)


@app.task
def notification_trigger(channel, event, data):
    pusher = _pusher()
    pusher.trigger(channel, event, data)

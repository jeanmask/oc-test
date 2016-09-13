#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, request, response, run
from pusher import Pusher

import settings


app = Bottle()


def _pusher():
    return Pusher(app_id=settings.PUSHER_APP_ID,
                  key=settings.PUSHER_KEY,
                  secret=settings.PUSHER_SECRET,
                  ssl=True)


@app.post('/auth/')
def authenticate():
    pusher = _pusher()
    auth = pusher.authenticate(
        socket_id=request.forms['socket_id'],
        channel=request.forms['channel_name'])
    return auth


@app.post('/notification/')
def notification():
    # to prevent circular import
    from tasks import notification_trigger
    channel = request.json.pop('channel')
    notification_trigger.delay(channel, 'notification', request.json)
    response.status = 201


@app.get('/')
def index():
    return open('index.html', 'r').read()


if __name__ == '__main__':
    run(app, host='localhost', port=8000, debug=True)

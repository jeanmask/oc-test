# -*- coding: utf-8 -*-

import os
from urllib.parse import quote


PUSHER_APP_ID = ''
PUSHER_KEY = ''
PUSHER_SECRET = ''

#AWS_ACCESS_KEY_ID = ''
#AWS_SECRET_ACCESS_KEY = ''

#BROKER_URL = 'sqs://{0}:{1}@'.format(
#    quote(AWS_ACCESS_KEY_ID, safe=''),
#    quote(AWS_SECRET_ACCESS_KEY, safe='')
#)

BROKER_URL = 'redis://127.0.0.1:6379'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

#BROKER_TRANSPORT_OPTIONS = {
#    'region': 'us-east-1',
#    'polling_interval': 3,
#    'visibility_timeout': 3600,
#}

#BROKER_TRANSPORT_OPTIONS['queue_name_prefix'] = 'oc-test'

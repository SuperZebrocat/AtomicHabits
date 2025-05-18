from __future__ import absolute_import, unicode_literals

import eventlet
import os
from celery import Celery

eventlet.monkey_patch()  # noqa: E402

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

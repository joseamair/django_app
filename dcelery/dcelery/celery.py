"""
This module configures and initializes Celery, a distributed task queue, for the Django project.

It sets the Django settings module for the 'celery' program, creates a new Celery application,
and updates the application's configuration from Django settings.
"""

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
# If the 'DJANGO_SETTINGS_MODULE' environment variable is not set, it defaults to 'dcelery.settings'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

# Create a new Celery application and name it 'dcelery'.
app = Celery('dcelery')

# Load the configuration for the Celery application from the Django settings.
# It uses the 'CELERY' namespace, which means that all Celery-related settings in your Django settings should be prefixed with 'CELERY'.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Register tasks
@app.task
def add_numbers():
    return

# Search for tasks.py in each installed Django app
app.autodiscover_tasks()

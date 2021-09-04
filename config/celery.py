import os
import django

from celery import Celery
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# celery-beats scheduling configurations.
app.conf.beat_schedule = {
    'test-celery-func': {
        'task':'beats_example.erase.tasks.number_of_inactive_users',
        'schedule':15 # 15 sec
    },
    'welcome-admin': {
        'task':'beats_example.erase.tasks.number_of_active_users',
        'schedule':20 # 10 sec
    }
}





@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

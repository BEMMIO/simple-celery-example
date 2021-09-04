# celery config imports
from config.celery import app



@app.task(name='test-celery-func')
# celery perform computational tasks
def test_celery_func():
	for i in range(80):
		print(i)
	return " BEATS COMMING YEEH -:) "


# simple practical scheduled tasks example.

from django.contrib.auth.models import User

@app.task
def number_of_inactive_users():
	if users := User._default_manager.filter(is_active=False):
		return "({users_count}) in-active users in db".format(users_count=users.count())

@app.task
def number_of_active_users():
	if users := User._default_manager.filter(is_active=True):
		return "({users_count}) active users in db".format(users_count=users.count())



@app.task
def delete_all_inactive_users():
	if users := User._default_manager.filter(is_active=False):
		count = users.count()
		users.delete()
		return "({count}) in-active users deleted from db".format(count=count)


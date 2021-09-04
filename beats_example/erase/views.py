from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .tasks import test_celery_func


def index(request):

	# run a celery test
	test_celery_func.delay()

	return render(request,'index.html',{})

from django.urls import re_path, path
from . import views


urlpatterns = [
  path('messages', view=views.messages, name='messages'),
  re_path(r'^(?!.*api).*$', view=views.index, name='index'),
]
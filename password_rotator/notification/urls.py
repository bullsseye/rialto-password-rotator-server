from django.conf.urls import url
from .api import NotificationView


urlpatterns = [
    url(r'^$', NotificationView.as_view()),
]

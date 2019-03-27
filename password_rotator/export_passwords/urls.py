from django.conf.urls import url
from .api import AccountView


urlpatterns = [
    url(r'^$', AccountView.as_view()),
]

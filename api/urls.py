from django.conf import settings
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^new_room/', views.new_room),
    url (r'^room/(?P<room_id>[0-9]+)/add_participant/$', views.add_participant),
    url (r'^room/(?P<room_id>[0-9]+)/close/$', views.close_room),
    url (r'^room/(?P<room_id>[0-9]+)/check_participant/$', views.check_participant),
]

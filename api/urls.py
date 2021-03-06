from django.conf import settings
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^new_room/', views.new_room),
    url (r'^room/(?P<room_id>[0-9]+)/is_closed/$', views.is_room_closed),
    url (r'^room/(?P<room_id>[0-9]+)/add_participant/$', views.add_participant),
    url (r'^room/(?P<room_id>[0-9]+)/close/$', views.close_room),
    url (r'^room/(?P<room_id>[0-9]+)/matches/(?P<entry_id>[0-9]+)/is_locked/$', views.is_entry_locked),
    url (r'^room/(?P<room_id>[0-9]+)/matches/(?P<entry_id>[0-9]+)/$', views.check_entry),
    url (r'^room/(?P<room_id>[0-9]+)/list_participants/$', views.list_participants),
    url (r'^room/(?P<room_id>[0-9]+)/list_entries/$', views.list_entries),

]

from django.conf import settings
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url (r'^room/(?P<room_id>[0-9]+)/add/$', views.add_people, name="add_people"),
    url (r'^room/(?P<room_id>[0-9]+)/close/$', views.close_room, name="close_room"),
    url (r'^room/(?P<room_id>[0-9]+)/matches/(?P<entry_id>[0-9]+)/$', views.access_entry, name="view_entry"),
    url (r'^room/(?P<room_id>[0-9]+)/matches/$', views.list_matches, name="list_matches"),
    url (r'^room/(?P<room_id>[0-9]+)/$', views.enter_room, name="enter_room"),

]

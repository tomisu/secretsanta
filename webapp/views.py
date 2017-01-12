from django.shortcuts import render, redirect
from .api_util import API
import json

# Create your views here.

def home(request):
    if request.method == "POST":
        response = API.new_room()
        if response['status'] != "OK":
            return render(request, 'webapp/home.html',  {'description':response['description']})
        else:
            return redirect('webapp.views.add_people', room_id=response['data']['room_id'])

    else:
        return render(request, 'webapp/home.html',  {})


def enter_room(request, room_id):
    """
    This view redirects the user to home or add_people, based on whether the room is closed or not
    """

    response = API.is_room_closed(room_id)
    if response['status'] != "OK":
        return render(request, 'webapp/home.html',  {'description':response['description']})

    if response['data']['is_closed']:
        return redirect('webapp.views.list_matches', room_id=room_id)
    else:
        return redirect('webapp.views.add_people', room_id=room_id)


def add_people(request, room_id):
    """
    (If it's called by POST) Adds a participant
    Renders the list of people
    """
    if request.method == "POST":
        response = API.add_participant(room_id, request.POST.get('name',None), request.POST.get('age',None))

        if response['status'] != "OK":
            return render(request, 'webapp/error.html', {'description':response['description']})


    response = API.list_participants(room_id)
    if response['status'] != "OK":
            return render(request, 'webapp/error.html', {'description':response['description']})

    return render(request, 'webapp/create.html', {'participants':response['data']})


def close_room(request, room_id):
    response = API.close_room(room_id)
    if response['status'] == "OK":
        return redirect('webapp.views.list_matches', room_id=room_id)
    else:
        return render(request, 'webapp/error.html', {'description':response['description']})


def list_matches(request, room_id):
    response = API.list_entries(room_id)
    if response['status'] == "OK":
        return render(request, 'webapp/entries.html', {'entries':response['data']})
    else:
        return render(request, 'webapp/error.html', {'description':response['description']})



def access_entry(request, room_id, entry_id):
    if request.method == "POST":
        password = request.POST.get('password', None)

        response = API.access_entry(room_id, entry_id, password)

        if response['status'] != "OK":
            return render(request, 'webapp/error.html', {'description':response['description']})

        return render(request, 'webapp/view_entry.html', {'giftee':response['data']['giftee']})

    else:
        response = API.is_entry_locked(room_id, entry_id)
        if response['status'] != "OK":
            return render(request, 'webapp/error.html', {'description':response['description']})

        is_locked = response['data']['is_locked']
        return render(request, 'webapp/access_entry.html', {'is_locked':is_locked})

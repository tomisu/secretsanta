from django.http import Http404
import requests
import json

class API:

    @staticmethod
    def call(url, data=None):
        req = requests.post('http://localhost:8000/api/'+url, data=data)
        try:
            response = req.json();
        except:
            raise raise Http404("Bad API call")

        return response

    @staticmethod
    def new_room():
        response = API.call('new_room/')
        return response

    @staticmethod
    def is_room_closed(room_id):
        response = API.call('room/{}/is_closed/'.format(room_id))
        return response

    @staticmethod
    def add_participant(room_id, name, age):
        response = API.call('room/{}/add_participant/'.format(room_id), data={
            'name':name,
            'age':age,
        })
        return response

    @staticmethod
    def close_room(room_id):
        response = API.call('room/{}/close/'.format(room_id))
        return response

    @staticmethod
    def list_participants(room_id):
        response = API.call('room/{}/list_participants/'.format(room_id))
        if response['status'] != "OK":
            raise Exception
        return response

    @staticmethod
    def list_entries(room_id):
        response = API.call('room/{}/list_entries/'.format(room_id))
        if response['status'] != "OK":
            raise Exception
        return response

    @staticmethod
    def access_entry(room_id, entry_id, password):
        response = API.call('room/{}/matches/{}/'.format(room_id, entry_id), data={'password':password})
        return response

    @staticmethod
    def is_entry_locked(room_id, entry_id):
        response = API.call('room/{}/matches/{}/is_locked/'.format(room_id, entry_id), data={})
        return response

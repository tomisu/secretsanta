from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .exceptions import *
from .messages import message
from .util import *
import json

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def new_room(request):
    room = Room()
    try:
        room.save()
    except:
        return message.error(CantCreateRoom)

    return message.success({'room_id':room.pk})


@csrf_exempt
def is_room_closed(request, room_id):
    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    return message.success({
        'pk':room.pk,
        'is_closed':room.is_closed,
    })


@csrf_exempt
def add_participant(request, room_id):
    name = request.POST.get('name', None)
    age = request.POST.get('age', None)

    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    if name is None or age is None:
        return message.error(InvalidData)

    participant = Participant()
    participant.name = name
    participant.room = room
    try:
        participant.age = int(age)
    except ValueError:
        return message.error(InvalidData)

    try:
        participant.save()
    except:
        message.error(CantCreateParticipant)

    return message.success()


@csrf_exempt
def close_room(request, room_id):
    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    try:
        room.close()
        room.save()
    except SSException as exception:
        return message.error(type(exception))

    return message.success()


@csrf_exempt
def is_entry_locked(request,room_id, entry_id):
    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    if room.is_closed is False:
        return message.error(RoomNotClosedYet)

    try:
        entry = room.entries.get(pk=entry_id)
    except:
        return message.error(EntryNotFound)

    return message.success({
        'pk':entry.pk,
        'is_locked':entry.is_locked,
    })


@csrf_exempt
def check_entry(request, room_id, entry_id):
    password = request.POST.get('password', None)

    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    if room.is_closed is False:
        return message.error(RoomNotClosedYet)

    try:
        entry = room.entries.get(pk=entry_id)
    except:
        return message.error(EntryNotFound)

    try:
        giftee = entry.get_giftee(password=password)
    except Exception as entry_exception:
        return message.error(type(entry_exception))

    return message.success({
                'gifter':entry.gifter.name,
                'giftee':giftee.name,
                })


@csrf_exempt
def list_participants(request, room_id):
    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    participants = []
    for participant in room.participants.all():
        participants.append({
            'name':participant.name,
            'age':participant.age,
        })

    return message.success(participants)

@csrf_exempt
def list_entries(request, room_id):
    try:
        room = Room.access(room_id)
    except Exception as room_exception:
        return message.error(type(room_exception))

    if room.is_closed is False:
        return message.error(RoomNotClosedYet)

    entries = []
    for entry in room.entries.all():
        entries.append({
            'pk':entry.pk,
            'gifter':entry.gifter.name,
            'is_locked':entry.is_locked,
        })
    return message.success(entries)

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .exceptions import *
from .messages import message

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def new_room(request):
    room = Room()
    try:
        room.save()
    except:
        return message.error(CantCreateRoom)

    return message.success()

@csrf_exempt
def add_participant(request, room_id):
    """
    Add a participant to a room

    TODO: Avoid adding participants with a duplicate name
    """
    request.POST = request.GET
    try:
        room = Room.objects.get(pk=room_id)
    except ObjectDoesNotExist:
        return message.error(RoomNotFound)

    name = request.POST.get('name', None)
    age = request.POST.get('age', None)

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
        room = Room.objects.get(pk=room_id)
    except ObjectDoesNotExist:
        return message.error(RoomNotFound)

    try:
        room.close()
        room.save()
    except SSException as exception:
        return message.error(type(exception))

    return message.success()

@csrf_exempt
def check_participant(request, room_id):
    request.POST = request.GET
    try:
        room = Room.objects.get(pk=room_id)
    except ObjectDoesNotExist:
        return message.error(RoomNotFound)

    gifter_name = request.POST.get('participant', None)
    gifter = Participant.objects.get(room=room, name=gifter_name)

    giftee = room.entries.get(gifter=gifter).giftee
    return message.success({'gifter':gifter.name, 'giftee':giftee.name})

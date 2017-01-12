from django.db import models
from .exceptions import *
from .util import *
import random

# Create your models here.

class Room(models.Model):
    """
    A 'game' of Secret Santa
    """
    is_closed = models.BooleanField(default=False)

    @classmethod
    def access(cls, room_id):
        try:
            room = Room.objects.get(pk=room_id)
        except Exception:
            raise RoomNotFound

        return room


    def shuffle(self, participants):
        entries = []
        giftees = list(participants)
        for gifter in participants:
            possible_giftees = list(giftees)
            while gifter in possible_giftees: possible_giftees.remove(gifter)
            if len(possible_giftees) < 1: return False
            giftee = random.choice(possible_giftees)

            giftees.remove(giftee)
            entries.append(Entry.create(self, gifter, giftee))
        return entries


    def generate_entries(self):
        Entry.objects.filter(room=self).delete()#REMOVE
        participants = self.participants.all()
        if len(participants) <2:
            raise NotEnoughPeople

        if self.is_closed is False:
            entries = self.shuffle(participants)
            while entries is False:
                entries = self.shuffle(participants)

            for entry in entries:
                entry.save()

        else:
            raise RoomAlreadyClosed


    def close(self):
        self.is_closed = False #REMOVE
        self.generate_entries()
        self.is_closed = True
        self.save()

    def __str__(self):
        return "Room {}".format(self.pk)


class Participant(models.Model):
    """
    The name and age of a participant in a specific room
    """
    room = models.ForeignKey('Room', related_name="participants")
    name = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return "{} ({}) at room {}".format(self.name, self.age, str(self.room))


class Entry(models.Model):
    """
    The relation of gifter and giftee
    """
    room = models.ForeignKey('Room', related_name="entries")
    gifter = models.ForeignKey('Participant', related_name="gifter_entries")
    giftee = models.ForeignKey('Participant', related_name="giftee_entries")
    is_locked = models.BooleanField(default=False)
    password = models.CharField(max_length=24, default=None, null=True, blank=True)


    def __str__(self):
        return "{} gifts to {} in room {} (locked is {})".format(self.gifter.name, self.giftee.name, str(self.room), str(self.is_locked))

    @classmethod
    def create(cls, room, gifter, giftee):
        entry = cls(room=room, gifter=gifter, giftee=giftee)
        return entry

    def get_giftee(self, **kwargs):
        password = kwargs.get('password', None)
        if password is None and self.is_locked is False:
            raise NeedToSetPassword

        password_md5 = computeMD5hash(password)
        if self.is_locked:
            if password_md5 != self.password:
                raise WrongPassword
        else:
            self.password = password_md5
            self.is_locked = True
            self.save()

        return self.giftee

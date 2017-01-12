from django.test import TestCase
from api.models import *
# Create your tests here.
class PairingTestCase(TestCase):

    def setUp(self):
        participants = [
            {'name':'Sof', 'age':'21'},
            {'name':'Tom', 'age':'23'},
            {'name':'Bian', 'age':'25'},
            {'name':'Irene', 'age':'27'},
        ]
        participants = participants

        self.room = Room.objects.create()

        for participant in participants:
            Participant.objects.create(room=self.room, name=participant['name'], age=participant['age'])

        self.participants = Participant.objects.all()
        self.room.close()

    def tearDown(self):
        Participant.objects.all().delete()
        Room.objects.all().delete()
        Entry.objects.all().delete()

    def test_closing_generates_n_entries(self):
        self.assertEqual(self.room.entries.count(), len(self.participants) )

    def test_no_duplicate_gifters(self):
        already_gave = []
        entries = self.room.entries.all()

        for entry in entries:
            self.assertNotIn(entry.gifter, already_gave)
            already_gave.append(entry.gifter)

    def test_no_duplicate_giftees(self):
        already_received = []
        entries = self.room.entries.all()

        for entry in entries:
            self.assertNotIn(entry.giftee, already_received)
            already_received.append(entry.giftee)

    def test_no_self_gift(self):
        entries = self.room.entries.all()

        for entry in entries:
            self.assertNotEqual (entry.gifter, entry.giftee)

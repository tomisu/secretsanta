class SSException(Exception):

    @property
    def msg(self):
        return getattr(self, 'error', None) or str(self)


class NotEnoughPeople(SSException):
    """
    There is not enough people to shuffle
    """

class InvalidData(SSException):
    """
    The data sent is not valid to perform an action
    """

class CantCreateRoom(SSException):
    """
    For some reason, the room couldn't be created
    """

class RoomNotFound(SSException):
    """
    The room doesn't exsist
    """

class EntryNotFound(SSException):
    """
    The PK doesn't match any Entry object
    """

class CantCreateParticipant(SSException):
    """
    There was an error creating a participant
    """

class RoomAlreadyClosed(SSException):
    """
    The room that is trying to be closed is already closed
    """

class WrongPassword(SSException):
    """
    No password was sent, or didn't match
    """

class NeedToSetPassword(SSException):
    """
    A password is needed in order to lock the entry
    """

class ParticipantNotFound(SSException):
    """
    The participant requested doesn't exist
    """

class RoomNotClosedYet(SSException):
    """
    Cannot access entries, because the room is still open
    """

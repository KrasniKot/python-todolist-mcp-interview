""" Contains all the Enums used throughout the API """

from enum import Enum


class StatusEnum(str, Enum):
    """ Represents the possible statuses of a TodoItem """
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED    = "finished"

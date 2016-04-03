# -*- coding: utf-8 -*-

"""
This module contains bindings for the private API provided by Jodel at
their RESTful endpoint.
"""

import hashlib
import json
import random
import requests
import string

from datetime import datetime
from enum import Enum
from pytz import timezone


# com.jodelapp.jodelandroidv3.api.ApiModule
JODEL_ANALYTICS_ENDPOINT = "https://analytics.ext.go-tellm.com:443"
JODEL_API_ENDPOINT = "https://api.go-tellm.com:443/api"
JODEL_CLIENT_ID = "81e8a76e-1e02-4d17-9ba0-8a7020261b26"


# com.jodelapp.jodelandroidv3.api.model.FlagReason
class Flags(Enum):
    """
    Reasons why a post was flagged.
    """
    #        Reason ID | Resource ID |            Inferred Meaning
    #        ----------|-------------|----------------------------
    FlagReason1 =  1 # |  2131165277 | Disclosure of Personal Data
    FlagReason2 =  2 # |  2131165278 |                  Harassment
    FlagReason3 =  3 # |  2131165279 |                    Spamming
    FlagReason4 =  4 # |  2131165280 |                       Other


class Device(object):
    """
    Creates and restores device information.
    """
    def __init__(self, uid):
        """
        Create a new instance of the Device class using the specified UID.
        """
        self.__uid = uid

    @property
    def uid(self):
        """
        Return the UID.
        """
        return self.__uid

    @classmethod
    def from_user(cls, user, password):
        """
        Return a new device based on a user and password combination.
        """
        blob = bytes(512 * "{0}!{1}".format(user, password), "UTF-8")
        hash_object = hashlib.sha256(blob)
        return cls(hash_object.hexdigest())

    @classmethod
    def from_random(cls):
        """
        Return a new random device.
        """
        symbols = string.ascii_lowercase + string.digits
        random_uid = "".join(random.choice(symbols) for _ in range(63))
        return cls(random_uid)


class Location(object):
    """
    Contains the coordinates of a location on the map.
    """
    def __init__(self, latitude, longtitude):
        """
        Create a new instance of the Location class using the specified
        latitude and longitude values.
        """
        self.__latitude = latitude
        self.__longtitude = longtitude

    @property
    def latitude(self):
        """
        Return the latitude of the geographical location.
        """
        return self.__latitude

    @property
    def longtitude(self):
        """
        Return the longtitude of the geographical location.
        """
        return self.__longtitude



def Jodel(object):
    def __init__(self):
        pass
    def delete_post(post_id):
        pass
    def downvote_post(post_id):
        pass
    def flag_post(post_id, reason):
        pass
    def send_post(location, image=None, ancestor=None):
        pass
    def upvote_post(post_id):
        pass
    def get_most_discussed_posts(skip, latitude, longtitude, limit=10):
        pass
    def get_most_popular_posts(skip, latitude, longtitude, limit=10):
        pass
    def get_most_recent_posts(skip, latitude, longtitude, limit=10):
        pass
    def get_request_token(self):
        pass

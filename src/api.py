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

from enum import Enum


# com.jodelapp.jodelandroidv3.api.ApiModule
JODEL_ANALYTICS_ENDPOINT = "https://analytics.ext.go-tellm.com:443"
JODEL_API_ENDPOINT = "https://api.go-tellm.com:443/api"
JODEL_CLIENT_ID = "81e8a76e-1e02-4d17-9ba0-8a7020261b26"
JODEL_BASE_HEADERS = {
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json; charset=UTF-8"
}


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


class Jodel(object):
    def __init__(self, device=None):
        if isinstance(device, Device):
            self.__device = device
        else:
            self.__device = Device.from_random()
    def delete_post(self, post_id):
        pass
    def downvote_post(self, post_id):
        pass
    def flag_post(self, post_id, reason):
        pass
    def send_post(self, location, image=None, ancestor=None):
        pass
    def upvote_post(self, post_id):
        pass
    def get_most_discussed_posts(self, skip, latitude, longtitude, limit=10):
        pass
    def get_most_popular_posts(self, skip, latitude, longtitude, limit=10):
        pass
    def get_most_recent_posts(self, skip, latitude, longtitude, limit=10):
        pass
    def get_request_token(self):
        uri = "{0}/v2/users/".format(JODEL_API_ENDPOINT)
        payload = {
            "client_id": "81e8a76e-1e02-4d17-9ba0-8a7020261b26",
            "device_uid": self.__device.uid,
            "location": {
                "city": "Oslo",
                "loc_coordinates": {
                "lat": 59.9439781,
                "lng": 10.7192413
            },
            "country": "NO",
            "loc_accuracy": 40.244
            }
        }

        response = requests.post(uri, data=payload, headers=JODEL_BASE_HEADERS)
        response.raise_for_status()

        return json.loads(response.text)

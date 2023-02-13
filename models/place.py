#!/usr/bin/python3
<<<<<<< HEAD
""" Class Place """

=======
""" module for Place class """
>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """ Place class that inherits BaseModel """
=======
    """
    initiation of Place that inherits from BaseModel class

    Public Class Attributes:
       (string) city_id: initialized as empty string
       (string) user_id: initialized as empty string
       (string) name: initialized as empty string
       (string) description: initialized as empty string
       (integer) number_rooms: intialized as zero
       (integer) number_bathrooms: initialized as zero
       (integer) max_guest: initialized as 0
       (integer) price_by_night: initialized as 0
       (float) latitude: initialized as 0.0
       (float) longitude: initialized as 0.0
       (list of strings) amenity_ids: initialized as empty list
    """
>>>>>>> 15abb2f991d67e22cdaa315fded5f1c13e964639
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

#!/usr/bin/env python3

"""
user.py

This module provides a 'User' class that defines shared attributes and
methods of all user types.
"""

class User:
    """Defines shared attributs and methods"""

    def __init__(slef, uid, name, email, role):
        """
        Instantiates attributes shared by all user types.

        uid (int) 	- User ID
        name (string)	- User name
        email (string)	- Email address
        role (string)	- Role of the user (Admin, Student, Instructore...)
        """

        self.uid = uid
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        """Returns a string representation of an object"""

        return "User(ID={}, Name={}, Email={}, Role{})".format(
                self.uid, self.name, self.email, self.role)

    # Getter and Setter for uid attribute
    @property
    def uid(self):
        """Getter for __uid attribute"""

        return self.__uid

    @uid.setter
    def uid(self, value):
        """Setter for __uid attribute"""

        if not isinstance(value, int):
            raise exceptions.InvalidIDError("Invalid ID! Must be only number.")
        if len(value) < 6 or len(value) > 12:
            raise exceptions.InvalidIDError("Invalid ID! Must contain 6 to 12 digits.")

        self.__uid = value

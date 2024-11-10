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
        role (string)	- Role of the user (Admin, Student, Instructore) 
        """

        self.uid = uid
        self.name = name
        self.email = email
        self.role = role

 

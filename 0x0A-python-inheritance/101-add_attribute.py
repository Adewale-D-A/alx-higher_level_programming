#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 8:47:00 2022
@author: Adewale
"""


def add_attribute(obj, name, value):
    """
    Add attribute into the class if it's possible
    Arguments:
        obj (object): The object to set as attribute
        name (str): Name for the new attribute
        value (int): Value to new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

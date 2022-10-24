#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 8:47:00 2022
@author: Adewale
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class shape, inheirts from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

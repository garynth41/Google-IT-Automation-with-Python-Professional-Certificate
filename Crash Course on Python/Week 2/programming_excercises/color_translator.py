# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 17:49:55 2020

@author: garyn
"""
"""
Complete the function by filling in the missing parts. The color_translator function receives
the name of a color, then prints its hexadecimal value. Currently, it only supports the three
additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
"""


def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
# BABY QUAKEBOT!
#
# https://source.opennews.org/en-US/articles/how-break-news-while-you-sleep/
#
#
# This is a python file, so you're going to run them from the 
# command line by going to the folder it's in and running this terminal
# command...
#
#   python eq_homework.py
#
# Then a little magic will happen! Unfortunately, to make a lot of magic
# happen you'll need to fill in the functions below.
# 

# The info that comes from USGS looks something like this:

earthquake = {
  'rms': '1.85', 
  'updated': '2014-06-11T05:22:21.596Z', 
  'type': 'earthquake', 
  'magType': 'mwp', 
  'longitude': '-136.6561', 
  'gap': '48', 
  'depth': '10', 
  'dmin': '0.811', 
  'mag': '5.7', 
  'time': '2014-06-04T11:58:58.200Z', 
  'latitude': '59.0001', 
  'place': '73km WSW of Haines, Alaska', 
  'net': 'us', 
  'nst': '', 
  'id': 'usc000rauc'}
  
# We're going to break it into pieces and see if we can make a nice little version of Quakebot.

# If there was an earthquake, it might say this
#
#   There was a big earthquake Monday morning a ways away from Haines, Alaska
#
# But what if it was huge, or tiny, or just medium-sized? Or not near Haines at all?
# Let's see what we can do using functions to make this magic happen.


# PROBLEM 1:
# Let's make the print statement reflect the size of the earthquake
#
# Write a function that describes each earthquake using a scale similar to the
# one at the link below.
#
# Hint: You'll use if statements
#
# http://www.sdgs.usd.edu/publications/maps/earthquakes/images/RichterScale.gif

# Here, I have created a similar scale to the USGS richter scale that where we have made an adjustment to
# the not felt and minor categories.  I have also added to the scale category ranges a measure of real world resulting damage.
# Defining an earthquake size function that inputs a richter measurement, it takes sample inputs and outputs the scale category.

def earthquake_size(richter_measurement):
    richter_float = float(richter_measurement)
    if richter_float <= 2 and richter_float > 0:
        return "imperceivable"
    if richter_float <= 4 and richter_float > 2:
        return "minor"
    if richter_float <= 5 and richter_float > 4:
        return "moderate"
    if richter_float <= 6 and richter_float > 5:
        return "strong"
    if richter_float <= 7 and richter_float > 6:
        return "very strong"
    if richter_float <= 8 and richter_float > 7:
        return "major"
    if richter_float > 8:
        return "devastating"

print "Strength: " + earthquake_size(1.5)
print "Strength: " + earthquake_size('3.9')
print "Strength: " + earthquake_size(4.5)
print "Strength: " + earthquake_size(5.8)
print "Strength: " + earthquake_size(6.8)
print "Strength: " + earthquake_size(7.1)
print "Strength: " + earthquake_size(8.0)

    
# PROBLEM 2:
# Let's make the print statement reflect the depth of the earthquake
#
# Make a function that describes each earthquake using a depth according to
# the information at the linke below
#
# http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php
#
# Hint: You'll use if statements, and be careful about types!


# We will use the following scale categories (km below the earth's surface):
# Shallow earthquakes = 0-70 km deep, Intermediate earthquakes= 70-300 km, Deep earthquakes= 300-700km deep
# Here we define another earthquake function with shallow, intermediate, and deep categories.  Anything else is impossible or unmeasurable.

def earthquake_depth(depth):
    depth_float = float(depth)
    if depth_float > 0 and depth_float <= 70:
        return "shallow"
    elif depth_float > 70 and depth_float <= 300:
        return "intermediate"
    elif depth_float > 300 and depth_float <= 700:
        return "deep"
    return "impossible or unmeasurable"

print earthquake_depth('70')
print earthquake_depth(71)
print earthquake_depth(150)
print earthquake_depth(700)
print earthquake_depth(7000)
print earthquake_depth('-1')
    
    
# PROBLEM 3:
# Let's make the print statement reflect the location the earthquake
# happened by
# 
# Use regular expressions to extract the location from the argument location_string
# *or* research the 'split' function and see if it can be of use if you pass
# it a certain special separator

# Here, we used a split method on the location variable based on finding the string " of ".
# It takes whatever is after that, which is the location and returns that.

def earthquake_location(location_str):
    
    location = location_str.split(" of ", 1)[1]
    
    return location

print earthquake_location("73km WSW of Haines, Alaska")


# PROBLEM 4:
# Let's make the print statement reflect the distance between the earthquake
# and the city
#
# You'll want to use several different categories, ie 'nearby', 
# 'far away from', and 'nowhere near'
#
# Hint: You'll use regular expressions to extract the kilometers from location_string,
# then use if statements on the result
#

# After importing the re library, we define a distance function that inputs a location string.
# The function searches for all digits within the string, takes the first digit value and assigns to a variable.
# If the variable is >100km, it is not near, if it is >50km, it is somewhat close, and if it is <50km, it is dangerously close.

import re

def earthquake_distance(location_str):
    distance = re.findall(r"\d+", location_str)[0]
    if float(distance) > 100:
        return "not near"
    elif float(distance) > 50:
        return "somewhat close"
    return "dangerously close"

print earthquake_distance("101km N of Tokyo, Japan 243")
print earthquake_distance("73km WSW of Haines, Alaska")
print earthquake_distance("19km SE of Istanbul, Turkey")

# PROBLEM 5 & 6:
#
# These were written by the instructures to show what the full bot will do.
# Message: Don't worry about these two functions yet.
#
#

def earthquake_day(time_string):
    return "Monday"

def earthquake_time(time_string):
    return "morning"

print "There was a " + earthquake_size(1.1) + \
    ", " + earthquake_depth('0.1') + \
    " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_distance("73km WSW of Haines, Alaska") + \
    " " + earthquake_location("73km WSW of Haines, Alaska")

print "There was a " + earthquake_size(8.7) + \
    ", " + earthquake_depth('98.22') + \
    " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_distance("238km N of Tobelo, Indonesia") + \
    " " + earthquake_location("238km N of Tobelo, Indonesia")

print "There was a " + earthquake_size(3.3) + \
    ", " + earthquake_depth('344.32') + \
    " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_distance("10km NE of Medford, Oklahoma") + \
    " " + earthquake_location("10km NE of Medford, Oklahoma")

print "There was a " + earthquake_size(6.1) + \
    ", " + earthquake_depth(5.289) + \
    " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
    " " + earthquake_distance("91km NE of Miches, Dominican Republic") + \
    " " + earthquake_location("91km NE of Miches, Dominican Republic")

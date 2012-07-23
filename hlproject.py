#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 

Description:
  The file 'userdata.txt' contains a list of geographic points for 4
  different users sorted by the time they were recorded.
  The format of each line is 4 fields separated by a pipe character.

  name|unixtime|latitude|longitude

  example line:
  danny|1335324573|37.784372722982|-122.39083248497

  Reads userdata.txt file and outputs a list of list of encounters 
  between the 4 users.

  Only generate an encounter if:
  - the user points are <= 150 meters are apart
  - the user points are <= 6 hours old at the time they are nearby
  - the user hasn't had an encounter with the same user in the prior 24 hours
  - the encounter must be based on the present location of the users
    (not historical location)

  The output format should be similar to the input file:
  unixtime|name1|latitude1|longitude1|name2|latitude2|longitude2

  So if 'danny' and 'unclejoey' were nearby each other, it would look like this:
  1327418725|danny|37.77695245908|-122.39847741481|unclejoey|37.777335807234|-122.39812024905

Running:
  * Tested with Python 2.6.5 on Mac OSX 10.7 not using any external libraries
  >>> python hlproject.py userdata.txt

"""

import sys
import logging
logging.getLogger().setLevel(logging.DEBUG)

def usage():
  print \
    """
    Usage: python hlproject.py userdata.txt

    """

if __name__ == "__main__":
  try:
    filename = sys.argv[1]
  except (IOError, IndexError):
    usage()
    exit()

  logging.info('Loading file ' + filename + '...')
  try:
    csv_reader = open(filename, 'rU')
  except IOError:
    logging.error('File not found.')
    exit()


  while True:
    cur = [c for c in csv_reader.readline().split('|') if c]
    logging.info(cur)
    if not cur:
      break




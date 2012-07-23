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
import csv
import logging
logging.getLogger().setLevel(logging.DEBUG)

SIX_HOURS = 21600
TW4_HOURS = 86400

def usage():
  print \
    """
    Usage: python hlproject.py userdata.txt

    """

class Utils():
  """ Random processing utilities.

  """
  @classmethod
  def haversine_distance(cls, origin, destination):
    """ Haversine formula implementation
    http://www.platoscave.net/blog/2009/\
        oct/5/calculate-distance-latitude-longitude-python/
    Args:
      origin(tuple): (lat, lon)
      destination(tuple): (lat, lon)

    Returns:
      `float`
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # mean radius

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d 


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

  results = []
  cache = {}
  cache_connect = {}
  while True:
    cur = [c for c in csv_reader.readline().split('|') if c]
    nxt = [n for n in csv_reader.readline().split('|') if n]
    # EOF
    if not nxt:
      break

    # Check if valid rows
    if len(cur) != 4 or len(nxt) != 4:
      logging.error('Invalid rows')
      continue

    u1, t1, la1, lo1 = cur
    u2, t2, la2, lo2 = nxt
    try:
      t1 = int(t1)
      la1 = float(la1)
      lo1 = float(lo1)
      t2 = int(t2)
      la2 = float(la2)
      lo2 = float(lo2)
    except ValueError:
      continue

  logging.info('Total: {0}'.format(len(results)))
  tab_file = open('results.txt', 'wb')
  tab_writer = csv.writer(tab_file, delimiter='|')
  for row in results:
    tab_writer.writerow(row)

  tab_file.close()
  logging.info('Done.')


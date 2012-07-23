# HLProject

## Geolocation matching

The file 'userdata.txt' contains a list of geographic points for 4 
different users sorted by the time they were recorded.
The format of each line is 4 fields separated by a pipe character.

name|unixtime|latitude|longitude

example line:
danny|1335324573|37.784372722982|-122.39083248497

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


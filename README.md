# ETSETB - Enterprises map

This repository contains a python script that generates a map using Google Maps API with a marker per
each enterprise which the ETSETB has an agreement, so it is easier for students to filter for enterprises
that may interest them depending on its location.

## DEMO :

Open the [map](map/map.html) in a browser (download the file and open it)

## Developing

First install pipenv :

`$ pip install pipenv`

In order to develop or run the script you must run pipenv to install the required dependencies.

`$ pipenv install`

You must have defined the following environment vars in order to run the script : 

|Name|Description|
|-------|------|
|UPC_USER|Username for the UPC intranet login|
|UPC_PASS|Password for the UPC intranet login|
|MAPS_API_KEY|API Key for google maps (contact me if you don't own a key)|

### Running the script :

~~~
$ pipenv shell
$ python src/main.py
~~~

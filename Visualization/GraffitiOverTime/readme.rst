
Locations over time
===================

Visualize the time varying locations of graffiti in New York city

The scripts folder contains the scripts to get coordinates from the addresses exported from the website


Data
====

Data comes from `nycopendata.socrata.com <https://nycopendata.socrata.com/Other/Graffiti-Locations/2j99-6h29>`_ exported in json and saved initially in server/data

Working URL
===========

- `suny-albany-cci.github.com <http://suny-albany-cci.github.com/OpenDataDayAlbany2013/Visualization/GraffitiOverTime/server/static/graffitimap.html>`_
- `dhandeo <http://dhandeo.github.com/OpenDataDayAlbany2013/Visualization/GraffitiOverTime/server/static/graffitimap.html>`_


Tools used
==========

- `leaflet <http://leafletjs.com/>`_ for mapping
- `Node.js <http://nodejs.org/>`_ as the webserver of the choice
- Currently it has 370 addresses.
- Please drag the slider (from both ends) to select the range, every slider update will refresh the markers on the screen

Scripts
=======

Scripts folder contains python scripts to

- Understand the data formats returned by google geocoding service
- The original data
- Query google for coordinates of the address data
- Combine various results into single json file

Future work
===========

- Currently entire dataset is loaded in memory, this will not scale well, instead, the data should be queried from server using ajax for given date range
- The markers layer should update only those markers which are updated (removed / added), instead, presently all markers are deleted and again added if required
- It should be possible to drag a fixed range, e.g. a month around (similar to finance.google.com interface)In other words : Allow dragging for a fixed range when one of the handles  is dragged, and change the range when other handle is dragged.
- Update the coordinates for entire data set eventually.


Visualization Projects
======================

- Visualizing time trend of Graffiti locations in New York City over time (GraffitiOverTime)
- Currently it has 370 addresses.
- Please drag the slider (from both ends) to select the range, every slider update will refresh the markers on the screen

Working URL
===========

`http://suny-albany-cci.github.com/OpenDataDayAlbany2013/Visualization/GraffitiOverTime/server/static/graffitimap.html`_
`http://dhandeo.github.com/OpenDataDayAlbany2013/Visualization/GraffitiOverTime/server/static/graffitimap.html`_

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


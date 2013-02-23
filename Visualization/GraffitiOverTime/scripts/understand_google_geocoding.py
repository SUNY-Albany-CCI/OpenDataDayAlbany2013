
response = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "1",
               "short_name" : "1",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Allen Street",
               "short_name" : "Allen St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Chinatown",
               "short_name" : "Chinatown",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Manhattan",
               "short_name" : "Manhattan",
               "types" : [ "sublocality", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "New York",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "New York",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "NY",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "10002",
               "short_name" : "10002",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "1 Allen Street, New York, NY 10002, USA",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 40.71439210,
                  "lng" :-73.99300749999999
               },
               "southwest" : {
                  "lat" : 40.71438780,
                  "lng" :-73.99302510
               }
            },
            "location" : {
               "lat" : 40.71439210,
               "lng" :-73.99302510
            },
            "location_type" : "RANGE_INTERPOLATED",
            "viewport" : {
               "northeast" : {
                  "lat" : 40.71573893029151,
                  "lng" :-73.99166731970848
               },
               "southwest" : {
                  "lat" : 40.71304096970851,
                  "lng" :-73.99436528029149
               }
            }
         },
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}

print response.keys()
print response["results"][0].keys()

addr = response["results"][0]["formatted_address"]
lat = response["results"][0]["geometry"]["location"]["lat"]
lng = response["results"][0]["geometry"]["location"]["lng"]
print addr
print location
print location["lat"], location["lng"]

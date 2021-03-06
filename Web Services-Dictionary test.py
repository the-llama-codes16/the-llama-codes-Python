data={
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Cebu City",
                    "short_name": "Cebu City",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Cebu",
                    "short_name": "Cebu",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Central Visayas",
                    "short_name": "Central Visayas",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Philippines",
                    "short_name": "PH",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Cebu City, Cebu, Philippines",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 10.498277,
                        "lng": 123.9291998
                    },
                    "southwest": {
                        "lat": 10.2592519,
                        "lng": 123.7633896
                    }
                },
                "location": {
                    "lat": 10.3156992,
                    "lng": 123.8854366
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 10.498277,
                        "lng": 123.9291998
                    },
                    "southwest": {
                        "lat": 10.2592519,
                        "lng": 123.7633896
                    }
                }
            },
            "place_id": "ChIJ_S3NjSWZqTMRBzXT2wwDNEw",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}

try:
    fstep=data['results'][0]['address_components']
    listtypeval=list()
    for item in fstep:
        sstep=item['types'][0]
        listtypeval.append(sstep)
    countryloc=listtypeval.index("country")
    print(fstep[countryloc]['short_name'])
except:
    print('Not in a country')


This is a fork of OSRM backend with project specific customizations for the smart transit project. Please refer to [OSRM-README.md](OSRM-README.md) for details about the OSRM project and the instructions for general compilation. 

Follow these instructions for the use of the router with smart transit project.

1. Clone the repository locally.
2. Download the latest tennessee-latest.osm.pbf file from the geofabrik servers and copy it to a folder called tn in the root directory of the current repository.
3. Build Docker image (change build concurrency for your machine)

```
docker build . -t t_osrm -f docker/smarttransitDockerfile --build-arg BUILD_CONCURRENCY=20
```

4. Run the docker image (the command -m is asking 10g of local memory. see the note below on docker resources)

```
docker run -m=10g -t -i -p 5000:5000 t_osrm
```

5. Test it. Open a browser and visit the following. Note that only TN coordinates will work.

```
http://127.0.0.1:5000/route/v1/driving/-86.79426670074463,36.12473806954196;-86.7641830444336,36.13808266878191?overview=full&annotations=true&geometries=geojson
```

Here is an example of the table (travel time and distance matrix) 

```
http://127.0.0.1:5000/table/v1/driving/-86.79426670074463,36.12473806954196;-86.7641830444336,36.13808266878191
```

```JSON
{
    "code": "Ok",
    "durations": [
        [
            0,
            373.3
        ],
        [
            369.7,
            0
        ]
    ],
    "destinations": [
        {
            "hint": "gA8DgCYPA4ABAAAADgAAAAAAAABRAAAAJTRoP2OjFUEAAAAATKhiQgEAAAAOAAAAAAAAAFEAAADTAAAA5Z_T-kU4JwLln9P6QjgnAgAAXxEOjx5Q",
            "distance": 0.332876,
            "name": "Sweetbriar Avenue",
            "location": [
                -86.794267,
                36.124741
            ]
        },
        {
            "hint": "QAcDgDh1JYAyAAAABgAAAAAAAAAAAAAA_oVgQnOXvUAAAAAAAAAAADIAAAAGAAAAAAAAAAAAAADTAAAAhhXU-mBsJwJpFdT6Y2wnAgAAfwAOjx5Q",
            "distance": 2.631813,
            "name": "Rains Avenue",
            "location": [
                -86.764154,
                36.13808
            ]
        }
    ],
    "sources": [
        {
            "hint": "gA8DgCYPA4ABAAAADgAAAAAAAABRAAAAJTRoP2OjFUEAAAAATKhiQgEAAAAOAAAAAAAAAFEAAADTAAAA5Z_T-kU4JwLln9P6QjgnAgAAXxEOjx5Q",
            "distance": 0.332876,
            "name": "Sweetbriar Avenue",
            "location": [
                -86.794267,
                36.124741
            ]
        },
        {
            "hint": "QAcDgDh1JYAyAAAABgAAAAAAAAAAAAAA_oVgQnOXvUAAAAAAAAAAADIAAAAGAAAAAAAAAAAAAADTAAAAhhXU-mBsJwJpFdT6Y2wnAgAAfwAOjx5Q",
            "distance": 2.631813,
            "name": "Rains Avenue",
            "location": [
                -86.764154,
                36.13808
            ]
        }
    ]
}
```


**Note** - read about docker resource management. you have to enable resources in the docker system setting. by default the docker containers are limited to around 2 GB memory and a few system cores. You should change it if you want good performance. 

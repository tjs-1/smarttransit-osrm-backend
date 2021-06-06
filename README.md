This is a fork of OSRM backend with project specific customizations for the smart transit project. Please refer to [OSRM-README.md](OSRM-README.md) for details about the OSRM project and the instructions for general compilation. 

Follow these instructions for the use of the router with smart transit project.

1. Clone the repository locally.
2. Download the latest tennessee-latest.osm.pbf file from the geofabrik servers and copy it to a folder called tn in the root directory of the current repository.
3. Build Docker image

```
docker build . -t t_osrm -f docker/smarttransitDockerfile
```

4. Run the docker image



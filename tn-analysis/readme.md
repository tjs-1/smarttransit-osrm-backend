Launch the OSRM in bash mode. Assuming the current git folder is the working directory.

```
 docker run -m=10g -t -i -p 5000:5000 -v `pwd`:/weights t_osrm bash
```

Then within the shell in docker container

```
python /weights/osrmrun.py
```

after it is done you will get all the different parquet files.

you can then analyze with readparquet

Note that you do need the files in the segment_speed_data. An example file is kept there. But these files are generated using the generatePerSegmentSpeedPerMonthPerDayTypePerHour.ipynb notebook.

Note to run the segment speed notebooks you need access to INRIX maps. You will need to have an account with them and download that data. The code can be updated to generated speed segment data from other sources if that is available to you. The main thing is to get the speed in kph for every osm node that is directly connected in your region of interest.


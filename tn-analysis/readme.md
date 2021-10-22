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

Note that you do need the files in the segment_speed_data. An example file is kept there. But these files are generated using the getcelldata notebooks.



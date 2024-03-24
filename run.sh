#!/bin/bash

# Run the MapReduce job using Hadoop Streaming
hadoop jar path/to/hadoop-streaming.jar \
    -input F:/movierating/ratings.txt \
    -output F:/movierating/output \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

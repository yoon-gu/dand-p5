# Data Visualization: Baseball Data
by Yoon-gu Hwang, November 22, 2015

## Summary ##

This dataset about information of baseball players. 
It includes player's name, handedness (right, left handed, or both), height, weight, batting average, and the number of home runs.

## Design ##
### Exploratory Data Analysis using Python ###
I downloaded `baseball_data.csv` the dataset from data set options page given by Udacity. The dataset had player's physical information(`name`, `height`, `weight`) and performance information(`avg`, `HR`).


|      |      height |      weight |         avg |          HR|
|------|-------------|-------------|-------------|------------|
|count | 1157.000000 | 1157.000000 | 1157.000000 | 1157.000000|
|mean  |   72.756266 |  184.513397 |    0.186793 |   45.359551|
|std   |    2.142272 |   15.445995 |    0.106175 |   74.065110|
|min   |   65.000000 |  140.000000 |    0.000000 |    0.000000|
|25%   |   71.000000 |  175.000000 |    0.138000 |    1.000000|
|50%   |   73.000000 |  185.000000 |    0.238000 |   15.000000|
|75%   |   74.000000 |  195.000000 |    0.258000 |   55.000000|
|max   |   80.000000 |  245.000000 |    0.328000 |  563.000000|

There are 1157 players' records. Interestingly, some players have zero batting average or home runs, so I removed those rows.

|      |     height |     weight |        avg |         HR|
|------|------------|------------|------------|-----------|
|count | 871.000000 | 871.000000 | 871.000000 | 871.000000|
|mean  |  72.338691 | 182.846154 |   0.244201 |  60.253731|
|std   |   1.935478 |  14.971904 |   0.030703 |  79.940631|
|min   |  65.000000 | 140.000000 |   0.104000 |   1.000000|
|25%   |  71.000000 | 170.000000 |   0.232000 |  11.000000|
|50%   |  72.000000 | 180.000000 |   0.248000 |  27.000000|
|75%   |  74.000000 | 193.000000 |   0.263000 |  78.000000|
|max   |  80.000000 | 230.000000 |   0.328000 | 563.000000|
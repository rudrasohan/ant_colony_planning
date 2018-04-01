# ant_colony_planning
Using ACO algorithm for grid search


## RUNNING
```console
foo@bar:~/location/ant_colony_planning$ python3 ACO.py -h
usage: ACO.py [-h] [-v] length breadth goal_x goal_y num_ants

Hyperparameters

positional arguments:
  length         Lenth of the Grid
  breadth        Breadth of the Grid
  goal_x         Goal Coordinate x
  goal_y         Goal Coordinate y
  num_ants       Number of Ants

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Display individual paths

```

## OBSTACLES

``` json
{
  "num_obstacle": 5,
  "size_x": 10,
  "size_y": 10,
  "positions": [
    [2,3],
    [4,5],
    [8,9],
    [9,4],
    [5,6]
  ]
}
```

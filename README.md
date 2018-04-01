# ant_colony_planning
Using ACO algorithm for grid search


## RUNNING
```console
foo@bar:~/loaction/ant_colony_planning$ python3 ACO.py -h
usage: ACO.py [-h] [-v] alpha beta Q num_ants num_gen

Hyperparameters

positional arguments:
  alpha          Parameter Alpha
  beta           Parameter Beta
  Q              Parameter Q
  num_ants       Number of Ants
  num_gen        Number of Generations

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Display individual paths

```

## WORLD

``` json
{
  "num_obstacle": 5,
  "grid_size_x": 10,
  "grid_size_y": 10,
  "start_pos_x": 0,
  "start_pos_y": 0,
  "goal_pos_x": 9,
  "goal_pos_y": 9,
  "positions": [
    [2,3],
    [4,5],
    [8,9],
    [9,4],
    [5,6]
  ]
}
```

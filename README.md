# Some algorithms for flows in networks.


### Example
Algorithms usage example with mean time measurement could be found in `./example.py`. 
To run code properly using PyCharm, mark `core` directory as Source.
Pipenv could be used for environment setup: `pipenv install` (all dependencies are contained in Pipfile).

EXAMPLE of example.py output:
```shell
>> INFO:__main__:Ford-Fulkerson mean time on random instances: 0.091
>> INFO:__main__:Edmonds-Karp mean time on random instances: 0.006
```

### Structure
- `./core` contains main structures and algorithms.
- `./tests` contains pytest style tests.

### Implemented Algorithms
- Max-Flow algorihtms
  - Ford-Fulkerson
  - Edmonds-Karp
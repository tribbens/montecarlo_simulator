# kvu2et_ds5100_montecarlo
A module to allow the user to perform Monte Carlo simulations.

## Metadata  
**Project Name:** Monte Carlo Simulator
**Author Name:** Trenton Ribbens

## Synopsis
```python

#installation
pip install .

# import modules
from montecarlo.montecarlo import Die
from montecarlo.montecarlo import Game
from montecarlo.montecarlo import Analyzer

#create Die object
die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
#change weight
die1.change_weight(1, 5)

#create Game object
game1 = Game([die1, die1])
#play a game
game1.play_game(1000)

#create Analyzer object
analyzer1 = Analyzer(game1)

```

## API description. 


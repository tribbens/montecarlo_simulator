# Metadata  
**Project Name:** Monte Carlo Simulator
**Author Name:** Trenton Ribbens

# Synopsis
```python

#installation
pip install montecarlo.montecarlo

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

# API description. 

## Die Class

    PURPOSE:  To allow the user to create a Die object with N sides or faces and W weights.
    The weights default to 1.0 and can be customized to fit the user's needs.
    The only behavior is for it to be rolled one or more times.

### Attributes

**faces** - list of faces of die

### Methods

**weight_change**
    
    PURPOSE:  Change the weight of one side of the die to the value passed to the function.

    INPUTS:  
    face_value  str or int (depending on how the initial die was setup)
    new_weight  int or float

    OUTPUTS:
    None  Internally revises the weight of one face in the private dataframe.

**roll_die**
    
    PURPOSE:  Roll the die the specified number of times and return the outcomes as a list.
        
    INPUTS:
    num_rolls  int, default=1

    OUTPUTS:
    roll_outcomes  list (of face values as int or str)

**view_die**

    PURPOSE:  The view the current faces and weights of the die as a dataframe.
        
    INPUTS:
    None

    OUTPUTS:
    _die_status  pandas data frame


## Game Class

    PURPOSE:  To allow the user to create a game which consists of rolling one or more
    similar dice (Die objects) one or more times. Similar dice means that each die
    has the same number of sides and associated faces, but my have thier own weights.
    Game objects have a behavior to play a game, which consists of rolling all dice a given
    number of times. Game objects only keep the results of the most recent play.

### Attributes

**current_die** - list of current Die objects in game

### Methods

**play_game**

    PURPOSE:  Play a game which involves rolling all die the specified number of 
    times and internally recording the results.
        
    INPUTS:
    num_times  int

    OUTPUTS:
    None  Internally saves the results of all rolls for all die in a private data frame.

**recent_results**

    PURPOSE:  Obtain the results of the most recent game played from play_game method.
    The results can be in a wide data frame or narrow data frame based on value passed 
    to variable "wide".

    INPUTS:
    wide  bool, default=True

    OUTPUTS:
    _game_results  pandas data frame
    
**get_faces**

    PURPOSE:  Obtain the list of face options for the die currently being used in the game.
    This method assumes that all die have the same face options.
    It will be used in the Analyzer class.
        
    INPUTS:
    None

    OUTPUTS:
    face_options  list (of strings or integers)
    
**get_dice_count**

    PURPOSE:  Obtain the number of die currently being used in the game.
    It will be used in the Analyzer class.
        
    INPUTS:
    None

    OUTPUTS:
    num_die_in_play  int
    

## Analyzer Class

    PURPOSE:  An Analyzer object takes the results of a single game (Game object)
    and computes various descriptive statistical properties about it.
    
### Attributes

**game** - current Game object being used in Analyzer object

### Methods

**jackpot**

    PURPOSE:  To compute the number of times the game resulted in a jackpot.
        
    INPUTS:
    None

    OUTPUTS:
    num_jackpots  int

**face_counts_per_roll**

    PURPOSE:  Computes the number of times a given face is rolled in each event and
    returns a data frame of the results.
        
    INPUTS:
    None

    OUTPUTS:
    count_df  pandas data frame

**combo_count**

    PURPOSE:  Computes the distinct combinations of faces rolled and their counts.
    It returns the results as a data frame.
        
    INPUTS:
    None

    OUTPUTS:
    combo_df  pandas data frame
    
**permutation_count**

    PURPOSE:  Computes the distinct permutations of faces rolled and their counts.
    It returns a data frame of the results.
        
    INPUTS:
    None

    OUTPUTS:
    perm_df  pandas data frame
    

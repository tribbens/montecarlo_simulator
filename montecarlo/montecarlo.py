import pandas as pd
import numpy as np
import random
from itertools import product
from itertools import combinations_with_replacement

class Die():
    '''
    PURPOSE:  To allow the user to create a Die object with faces as strings or integers
    and revise the weights according to their needs. The class also allows the user
    to roll the die and receive the results of the rolls. The user can view the current
    state of the die at any time.
    
    INPUTS:
    faces  numpy array (of strings or integers)
    
    OUTPUTS:
    None
    '''
    
    def __init__(self, faces):
        '''
        PURPOSE:  Create the initial die using the faces passed to the function and set all weights equal to 1.
        
        INPUTS:
        faces  numpy array (of strings or integers)
        
        OUTPUTS:
        None  internally saves die with faces and weights in private dataframe
        '''
        
        #raise TypeError of faces argument is not a NumPy array
        if type(faces) != np.ndarray:
            raise TypeError("faces argument must be a NumPy array")
        
        #confirm array values are distinct
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Face values must be distinct!")
        
        faces = pd.Series(faces)
        self.faces = list(faces)
        W = []
        for i in range(len(faces)):
            W.append(1.0)
        die_priv_df = pd.DataFrame(W)
        die_priv_df = die_priv_df.set_index(faces)
        #save current die faces and weights as private data frame
        self._die_status = die_priv_df
        
    def weight_change(self, face_value, new_weight):
        '''
        PURPOSE:  Change the weight of one side of the die to the value passed to the function.
        
        INPUTS:  
        face_value  str or int (depending on how the initial die was setup)
        new_weight  int or float
        
        OUTPUTS:
        None  Internally revises the weight of one face in the private dataframe.
        '''
        
        #confirm face value is one of the faces and raise IndexError if not
        if face_value not in self.faces:
            raise IndexError("Not a valid face value")
            
        #raise TypeError for invalid weight
        if (type(new_weight) != float) and (type(new_weight) != int):
            try:
                float(new_weight)
            except:
                raise TypeError("The new weight must be a numeric value")
        
        #change weight of indicated face value
        self._die_status[0][face_value] = new_weight
        
    def roll_die(self, num_rolls=1):
        '''
        PURPOSE:  Roll the die the specified number of times and return the outcomes as a list.
        
        INPUTS:
        num_rolls  int (defaults to 1)
        
        OUTPUTS:
        roll_outcomes  list (of face values as int or str)
        '''
        #initiate blank list for outcome
        roll_outcomes = []
        #convert current weights to a list
        weights_list = self._die_status[0].tolist()
        #run selection desired number of times
        for i in range(num_rolls):
            roll_outcomes.append(random.choices(self.faces, weights_list)[0])
        
        return roll_outcomes
    
    def view_die(self):
        '''
        PURPOSE:  The view the current faces and weights of the die as a dataframe.
        
        INPUTS:
        None
        
        OUTPUTS:
        _die_status  dataframe
        '''
                
        return self._die_status

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Game():
    
    def __init__(self, current_die):
        '''
        PURPOSE:  Create a game object based on a list of Die objects being used.
        
        INPUTS:
        current_die  list (of Die objects)
        
        OUTPUTS:
        None  Saves the list of current die as an attribute.
        '''
        
        self.current_die = current_die
        
    def play_game(self, num_times):
        '''
        PURPOSE:  Play a game which involves rolling all die the specified number of times and internally recording the results.
        
        INPUTS:
        num_times  int
        
        OUTPUTS:
        None  Internally saves the results of all rolls for all die in a private data frame.
        '''
        
        #initiate blank dataframe
        game_results = pd.DataFrame()
        
        #set column index count to zero
        i = 0
        
        for dice in self.current_die:
            #run roll_die method
            roll_results = dice.roll_die(num_rolls=num_times)
            #save results to dictionary with list index as key
            new_result = {i: roll_results}
            #convert to a dataframe
            new_result_df = pd.DataFrame(new_result)
            #add the new column to the data frame
            game_results = pd.concat([game_results, new_result_df], axis=1)
            #add 1 to list index
            i += 1
                
        #create list of rolls
        rolls = []
        for i in range(1, num_times+1):
            rolls.append(i)
        rolls = pd.Series(rolls)
        #rename index and set values to roll number
        game_results = game_results.set_index(rolls)
        game_results.index.name = "Roll Number"

        #most recent results saved as a private data frame
        self._game_results = game_results
        
        
    def recent_results(self, wide=True):
        '''
        PURPOSE:  Obtain the results of the most recent game played from play_game method.
        The results can be in a wide data frame or narrow data frame based on value passed to variable "wide".
        
        INPUTS:
        wide  bool
        
        OUTPUTS:
        _game_results  data frame
        '''
        
        #Raise ValueError if bool isn't passed as value for wide
        if type(wide) != bool:
            raise ValueError("Value for wide must be True or False")
            
        elif wide:
            return self._game_results
        
        else:          
            return self._game_results.unstack().to_frame().swaplevel()
    
    def get_faces(self):
        '''
        PURPOSE:  Obtain the list of face options for the die currently being used in the game.
        This method assumes that all die have the same face options. It will be used in the Analyzer class.
        
        INPUTS:
        None
        
        OUTPUTS:
        face_options  list (of strings or integers)
        '''
        
        #this will be used in Analyzer class so I know the face options
        face_options = self.current_die[0].view_die().index.to_list()
        return face_options
    
    def get_dice_count(self):
        '''
        PURPOSE:  Obtain the number of die currently being used in the game.
        It will be used in the Analyzer class.
        
        INPUTS:
        None
        
        OUTPUTS:
        num_die_in_play  int
        '''
        
        #this will be used in the Analyzer class so I know the number of dice in play
        num_die_in_play = len(self.current_die)
        return num_die_in_play


#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------


class Analyzer():
    
    def __init__(self, input_game):
        
        if type(input_game) != Game:
            raise ValueError("Input must be a Game object")
        
        self.game = input_game
        
    
    def jackpot(self):
        
        #save recent game results as variable
        game_results = self.game.recent_results()
        
        #set jackpot count to 0
        num_jackpots = 0
        
        #iterate through the rows
        for i in range(1, len(self.game.recent_results())+1):
            if len(game_results.loc[i].unique()) == 1:
                num_jackpots += 1
            else:
                pass
        
        return num_jackpots
    
    def face_counts_per_roll(self):
        
        game_results = self.game.recent_results()
        
        #create blank dictionary
        count_dict = {i: [] for i in self.game.get_faces()}
        
        # iterate through the rows and append the count of each face
        for i in range(1, len(self.game.recent_results())+1):
            row = list(game_results.loc[i])
            for x in self.game.get_faces():
                count_dict[x].append(row.count(x))
        
        #turn the dictionary of counts into a data frame
        count_df = pd.DataFrame(count_dict)
                                     
        return count_df
                                     
    
    def combo_count(self):
        '''
        docstring
        '''
        
        #save recent game results as variable
        game_results = self.game.recent_results()
        
        #generate all combinations based on faces and number of die
        combs = combinations_with_replacement(self.game.get_faces(), self.game.get_dice_count())
        
        #create blank dataframe using the combinations as the index (as a string)
        data = {'Combination': [str(list(i)) for i in list(combs)]}
        combo_df = pd.DataFrame(data)
        combo_df.index = combo_df['Combination']
        combo_df['Count'] = 0
        combo_df = combo_df['Count'].to_frame()
        
        # iterate through the rows and increase the count for each combination rolled
        for i in range(1, len(self.game.recent_results())+1):
            row = str(sorted(list(game_results.loc[i])))
            combo_df.loc[row][0] = combo_df.loc[row][0] + 1
        
        return combo_df
            
    def permutation_count(self):
        '''
        docstring
        '''
        
        #save recent game results as variable
        game_results = self.game.recent_results()
        
        #generate all permutations based on faces and number of die
        perms = product(self.game.get_faces(), repeat=self.game.get_dice_count())
        
        #create blank dataframe using the combinations as the index (as a string)
        data = {'Permutation': [str(list(i)) for i in list(perms)]}
        perm_df = pd.DataFrame(data)
        perm_df.index = perm_df['Permutation']
        perm_df['Count'] = 0
        perm_df = perm_df['Count'].to_frame()
        
        # iterate through the rows and increase the count for each permutation rolled
        for i in range(1, len(self.game.recent_results())+1):
            row = str(sorted(list(game_results.loc[i])))
            perm_df.loc[row][0] = perm_df.loc[row][0] + 1
            
        return perm_df

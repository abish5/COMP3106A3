import numpy
import sys
import math

class td_qlearning:

  alpha = 0.2
  gamma = 0.9
  #this dict is going to follow this format {key:state, value:{key:action , value:qvalue}} 
  qvalues_dict = {}
  #this dict will be a simple key value pair of {key:state value:reward}
  rvalues_dict = {}

  def __init__(self, trial_filepath):
    # trial_filepath is the path to a file containing a trial through state space
    trial_list = []
    file_data = open(trial_filepath, 'r')
    for row in file_data:
      trial_list.append(row.strip().split(','))
    #setting the initial values for the dictionary holding all of the r values
    td_qlearning.rvalues_dict.update(dict.fromkeys(['WW', 'XX', 'YY', 'ZZ'], -1))
    td_qlearning.rvalues_dict.update(dict.fromkeys(['WX', 'WY', 'WZ', 'XW', 'XY', 'XZ', 'YX', 'YW', 'YZ', 'ZW', 'ZX', 'ZY'], 1))
    #setting the initial qvalues
    for i in range(4):
      for j in range(4):
        #the state for the mouse
        if i == 0:
          state = "W"
        elif i == 1:
          state = "X"
        elif i == 2:
          state = "Y"
        elif i == 3:
          state = "Z"
        #adding the state for the cat
        if j == 0:
          state += "W"
        elif j == 1:
          state += "X"
        elif j == 2:
          state += "Y"
        elif j == 3:
          state += "Z"
        #adding in the actions and setting the initial qvalues to 0 this also only adds actions that are takeable from that square
        if i == 0:
          td_qlearning.qvalues_dict[state] = {"N": 0, "D": 0, "R": 0}
        elif i == 1:
         td_qlearning.qvalues_dict[state] = {"N": 0, "D": 0, "L": 0}
        elif i == 2:
         td_qlearning.qvalues_dict[state] = {"N": 0, "U": 0, "R": 0}
        elif i == 3:
         td_qlearning.qvalues_dict[state] = {"N": 0, "U": 0, "L": 0}

    #going through the trial and updating all of the qvalues
    for i in range(len(trial_list)):
      #if statement to check to see if it is the last state action pair
      if i == len(trial_list) - 1:
        break
      #this variable is Q(s,a)
      q_of_sa = td_qlearning.qvalues_dict[trial_list[i][0]][trial_list[i][1]]
      #makes a list of all of the possible qvalues for Q(s',a') this will be used later to get the max a'
      all_values = td_qlearning.qvalues_dict[trial_list[i + 1][0]].values()
      #this is the update function Q(s,a)<-Q(s,a)+alpha(r(s)+(gamma * max(a'(Q(s',a'))))-Q(s,a))
      td_qlearning.qvalues_dict[trial_list[i][0]][trial_list[i][1]] = q_of_sa + td_qlearning.alpha * (td_qlearning.rvalues_dict[trial_list[i][0]][trial_list[i][1]] + td_qlearning.gamma * max(all_values) - q_of_sa)

    # Return nothing

  def qvalue(self, state, action):
    # state is a string representation of a state
    # action is a string representation of an action

    # Return the q-value for the state-action pair
    return td_qlearning.qvalues_dict[state][action]

  def policy(self, state):
    # state is a string representation of a state
    a = td_qlearning.qvalues_dict[state]
    # Return the optimal action under the learned policy
    return max(a, key=a.get())

#For Testing
def main():
  td_qlearning("Example0/trial.csv")

if __name__ == "__main__":
  main()
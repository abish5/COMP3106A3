import numpy
import sys
import math

class td_qlearning:

  alpha = 0.2
  gamma = 0.9
  qvalues_dict = {}

  def __init__(self, trial_filepath):
    # trial_filepath is the path to a file containing a trial through state space
    trial_list = []
    file_data = open(trial_filepath, 'r')
    for row in file_data:
      trial_list.append(row.strip().split(','))
    #initially Q(a, s) = r(s)
    for i in range(len(trial_list)):
      if trial_list[i][0] == 'WW' or trial_list[i][0] == 'XX' or \
          trial_list[i][0] == 'YY' or trial_list[i][0] == 'ZZ':

        td_qlearning.qvalues_dict[(trial_list[i][0], trial_list[i][1])] = -1
      else:
        td_qlearning.qvalues_dict[(trial_list[i][0], trial_list[i][1])] = 1

    # Return nothing

  def qvalue(self, state, action):
    # state is a string representation of a state
    # action is a string representation of an action

    # Return the q-value for the state-action pair
    return q

  def policy(self, state):
    # state is a string representation of a state

    # Return the optimal action under the learned policy
    return a

#For Testing
def main():
  td_qlearning("Example0/trial.csv")

if __name__ == "__main__":
  main()
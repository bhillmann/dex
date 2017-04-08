#!/usr/bin/env python
# By Nick Erickson
# DDQN Implementation

# Run with Tensorflow v12 and Keras v2.02

# Done: Target Network https://jaromiru.com/2016/10/21/lets-make-a-dqn-full-dqn/
# TODO: Prioritized Experience Replay
# TODO: Random agent saving memory/loading memory (Mostly done)
    
from __future__ import print_function

#%%

# Experimental
#import threading

# Utilities
from param_const import gym_cart_ddqn, hex_base, hex_base_gather
import play_game
import agent_ddqn
import agent_random

#%%

def main(args):    
    #play_game.run(args, agent_ddqn.Agent)
    play_game.run(args, agent_random.Agent)
    # TODO: Use finally clause to save model weights

if __name__ == "__main__":
    #args = hex_base
    args = hex_base_gather
    #args = gym_cart_ddqn
    main(args) 

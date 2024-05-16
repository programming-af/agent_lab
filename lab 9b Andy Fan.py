#Andy Fan

#%%0

import pandas as pd
from numpy import random

params = {'world_size':(8,8),
          'num_agents':5,
          'same_pref' :0.4,
          'max_iter'  :100,
          'out_path'  :r'D:\UChicago\Classes\2024Spring\Python Programming\labs\abm_results.csv' 
          }

#%%1

class Agent():
    def __init__(self):
        #color and pref
        self.world = world
        self.kind = kind
        self.same_pref = same_pref
        self.location = None

    def move(self):   
        #decision to move, based on am_i_happy
        happy = self.am_i_happy()
        
        if not happy:
            self.world.grid[self.location] = None #move out of current patch
            self.location = patch                 #assign new patch to myself
            self.world.grid[patch] = self         #update the grid
            i_moved = True
            return 1
            
        if happy:
            return 0
        
        
        
    def am_i_happy(self):
        # boolean for if happy at current loc. uses locate_neighbors
        if not loc:
            starting_loc = self.location
        else:
            starting_loc = loc

        neighbor_patches = self.locate_neighbors(starting_loc)
        neighbor_agents  = [self.world.grid[patch] for patch in neighbor_patches]
        neighbor_kinds   = [agent.kind for agent in neighbor_agents if agent is not None]
        num_like_me      = sum([kind == self.kind for kind in neighbor_kinds])

       
        #if an agent is in a patch with no neighbors at all, treat it as unhappy
        if len(neighbor_kinds) == 0:
            return False

        perc_like_me = num_like_me / len(neighbor_kinds)

        if perc_like_me < self.same_pref:
            return False
        else:
            return True
        
    def locate_neighbors(self):
        #given a loc. return all patches that are neighbors. 
        x, y = loc
        cardinal_four = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        if include_corners:
            corner_four = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
            neighbors = cardinal_four + corner_four
        else:
            neighbors = cardinal_four

#%%1.1

class World():
    def __init__(self):
        #stores grid, initializes agents loc. and number
        assert(params['world_size'][0] * params['world_size'][1] > params['num_agents']), 'Grid too small for number of agents.'
        self.params = params
        self.reports = {}

        self.grid     = self.build_grid(  params['world_size'])
        self.agents   = self.build_agents(params['num_agents'], params['same_pref'])

        self.init_world()

    def build_grid(self):        
        #returns a dict
        locations = [(i,j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l:None for l in locations}
        
    def build_agents(self):
        #gen list of agents that can be iterated over
        def _kind_picker(i):
            if i < round(num_agents / 2):
                return 'red'
            else:
                return 'blue'

        agents = [Agent(self, _kind_picker(i), same_pref) for i in range(num_agents)]
        random.shuffle(agents)
        return agents
        
    def init_world(self):
        #startding condtions of world
        for agent in self.agents:
            loc = self.find_vacant()
            self.grid[loc] = agent
            agent.location = loc

        assert(all([agent.location is not None for agent in self.agents])), "Some agents don't have homes!"
        assert(sum([occupant is not None for occupant in self.grid.values()]) == self.params['num_agents']), 'Mismatch between number of agents and number of locations with agents.'

        #set up some reporting dictionaries
        self.reports['integration'] = []
        
        
    def find_vacant(self, return_all=False):
        #find list of enmpty patches aad return one
        
    def report_integration(self):
        #generates a report at end of round
        
    def report(self, to_file=True):
        #gen report after model end:
        
    def run(self):
        #runs
        
#%%1.2

world = world()
world.run

        
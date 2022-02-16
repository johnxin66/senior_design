"""
Env 2D
@author: Jinghong Peng
"""

import numpy as np
import binvox_rw



class Env:
    def __init__(self):
        self.x_range = 1000  # size of background
        self.y_range = 1000
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs



    def obs_map(self):
        """
        Initialize obstacles' positions
        :return: map of obstacles
        """

        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        with open('test_map_1000_1000_300.binvox', 'rb') as f:
            ms = binvox_rw.read_as_coord_array(f)
        x = ms.data[0]
        y = ms.data[1]
        z = ms.data[2]
        rows, cols = (1000,1000)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(len(x)):
            if (z[i] > 100):
                xPos = x[i]
                yPos = y[i]
                obs.add((xPos, yPos))
        '''
        def add_obs(ax, ay, bx, by):
            for i in range (ay, by):
                obs.add((ax, i))
            for i in range (ay, by):
                obs.add((bx, i))
            for i in range (ax, bx):
                obs.add((i, ay))
            for i in range (ax, bx+1):
                obs.add((i, by))
        '''
 

            
        return obs
'''
        for i in range(10, 21):
            obs.add((i, 15))
        for i in range(15):
            obs.add((20, i))

        for i in range(15, 30):
            obs.add((30, i))
        for i in range(16):
            obs.add((40, i))
'''


import numpy as np
import random


class CA:

    def __init__(self, f1, f2, timesteps, _lambda, verbose=True, size=10000):
        self.verbose = verbose
        self.size = size
        self.state = None
        self.f1_rule = f1
        self.f2_rule = f2
        self.timesteps = timesteps
        self._lambda = _lambda

    def set_initial_state(self):
        self.state = np.random.randint(0, 2, (self.timesteps, self.size)).astype(np.float32)

    def get_local_neighborhood(self, prev_state, index):
        # Obtain neihbors, with boundary condition
        if index != 0:
            left = int(prev_state[index - 1])
        else:
            left = int(prev_state[-1])
        
        if index != (prev_state.size - 1):
            right = int(prev_state[index + 1])
        else:
            right = int(prev_state[0])
        
        middle = int(prev_state[index])

        return (left, middle, right)

    def get_rule_index(self, local_triple):
        local_triple_string = (str(local_triple[0]) + str(local_triple[1]) + str(local_triple[2]))
        return int(local_triple_string, 2)

    def apply_rule(self, t, prev_state, rule):
        if rule is None:
            print("Returning random iteration because no rule was specified") if self.verbose else None
            return np.random.choice([0, 1], size=(self.size,), p=[0.5, 0.5])

        for i in range(self.size):
            binary_rule = '{0:08b}'.format(rule)
            local_triple = self.get_local_neighborhood(prev_state, i)
            rule_index = self.get_rule_index(local_triple)
            self.state[t][i] = int(binary_rule[rule_index])

    def update(self, t):
        if random.uniform(0, 1.0) < self._lambda:
            self.apply_rule(t, self.state[t - 1], self.f2_rule)
        else:
            self.apply_rule(t, self.state[t - 1], self.f1_rule)

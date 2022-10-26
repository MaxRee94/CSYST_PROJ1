import numpy as np


class CA:

    def __init__(self, f1, f2, timesteps, verbose=True, size=10000):
        self.verbose = verbose
        self.size = size
        self.state = None
        self.f1_rule = f1
        self.f2_rule = f2
        self.timesteps = timesteps
        self.random_iteration = np.random.choice([0, 1], size=(self.size,), p=[0.5, 0.5])

    def set_initial_state(self):
        self.state = np.random.randint(0, 2, (self.timesteps, self.size)).astype(np.float32)

    def apply_rule(self, prev_state, rule):
        if not rule:
            print("Returning random iteration because no rule was specified") if self.verbose else None
            return self.random_iteration

    def update(self, t):
        print("Updating...") if self.verbose else None
        
        self.state[t] = self.apply_rule(self.state[t - 1], None)



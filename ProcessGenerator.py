import numpy as np


class ProcessGen:
    def __init__(self, N):
        self.starting_time = np.random.randint(1, 1000)  # random starting time

        self.proc_required = int(np.random.normal(50, 25))  # random processor load, normal distribution
        if self.proc_required > 90:
            self.proc_required = 90
        if self.proc_required < 1:
            self.proc_required = 1

        self.time_required = int(np.random.normal(100, 100))  # random time required, normal distribution
        if self.time_required < 1:
            self.time_required = 1

        self.starting_proc = np.random.randint(1, N)  # random processor on which the process starts

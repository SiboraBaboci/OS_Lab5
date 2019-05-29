class CProcessor:
    # utilization = 0
    # processes_running = []
    #
    mean_util = 0.0
    times_called = 0

    def __init__(self):
        self.utilization = 0
        self.processes_running = []

    def calc_util(self):
        self.utilization = 0
        for i in self.processes_running:
            self.utilization += i.proc_required
        return self.utilization

    def update_mean_util(self):
        # whenever this function is called it remembers the amount of times called
        # and updates its mean utilization time accordingly
        self.times_called += 1
        self.mean_util += self.calc_util()

    def get_mean_util(self):
        return self.mean_util / self.times_called

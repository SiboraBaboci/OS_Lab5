import Processor as pr
import numpy as np


def random(process_list, N, p, z, time_max):
    # N - number of processors (50-100)
    # p - threshold of processor utilization (process will be send there if utilization in smaller than p)
    # z - maximum amount of queries for processor utilization
    # time_max - maximum number of ticks
    processor_list = []
    for i in range(N):
        processor_list.append(pr.CProcessor())  # create a list of N processors

    for i in range(time_max):  # simulate the passing of time

        for process in process_list:
            process.starting_time -= 1  # decrease starting time of all processes in queue
            if process.starting_time == 0:  # if a process starting time reaches 0, it's added to a random processor
                z_temp = z  # keep track of how many times you've asked for other processes utilization
                while z_temp:
                    random_processor = np.random.randint(0, N)  # randomly choose a processor
                    if processor_list[random_processor].calc_util() < p:  # ask for its utilization, and if it's lower than p
                        processor_list[random_processor].processes_running.append(process)  # give it that process
                        break
                    else:
                        z_temp -= 1
                        if z_temp == 0:  # if you've asked 'p' processors, process it yourself
                            processor_list[process.starting_proc].processes_running.append(process)

        for processor in processor_list:  # update running time of all processes on all processors
            for process_running in processor.processes_running:
                process_running.time_required -= 1
                if process_running.time_required == 0:
                    processor.processes_running.remove(process_running)
            processor.update_mean_util()  # update mean processor load of each processor

    sum_of_means = 0
    for temp in range(len(processor_list)):
        print("Processor {0}: {1:3.2f}%".format(temp, processor_list[temp].get_mean_util()))
        sum_of_means += processor_list[temp].get_mean_util()
    print("Mean utilization of all processes: {0:3.2f}%".format(sum_of_means/N))
    return

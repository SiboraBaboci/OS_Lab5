import ProcessGenerator as pg
import Random as rd
import MaxThreshold as MxTh
import MinThreshold as MiTh
import copy

"""
Processor scheduling in distributed systems (processor assignment for a process) simulation of algorithms: 
random
maximum threshold
minimum threshold
Compare CPU load, number of requests sent, number of process migrations. 
"""


N = 100  # number of processors
p = 90  # maximum threshold
r = 40  # minimum threshold
z = 3  # number of retries
processes = 2000  # amount of processes
process_list = []

for i in range(processes):
    temp_process = pg.ProcessGen(N)
    process_list.append(temp_process)
process_list2 = copy.deepcopy(process_list)
process_list3 = copy.deepcopy(process_list)

TIME_MAX = 1500

rd.random(process_list, N, p, z, TIME_MAX)
print()
MxTh.maxThreshold(process_list2, N, p, TIME_MAX)
print()
MiTh.minThreshold(process_list3, N, p, r, TIME_MAX)

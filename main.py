import ProcessGenerator as pg
import Random as rd
import MaxThreshold as MT
import copy

N = 100  # number of processors
p = 90  # threshold
z = 3  # number of retries
processes = 2000  # amount of processes
process_list = []
process_list2 = []

for i in range(processes):
    temp_process = pg.ProcessGen(N)
    process_list.append(temp_process)
process_list2 = copy.deepcopy(process_list)

TIME_MAX = 1500

MT.maxThreshold(process_list, N, p, TIME_MAX)
print()
rd.random(process_list2, N, p, z, TIME_MAX)
print()

from multiprocessing.dummy import Pool as ThreadPool
from functools import partial

import ProcessGenerator as pg
import Random as rd
import MaxThreshold as MxTh
import MinThreshold as MiTh
import copy
import numpy as np

import matplotlib.pyplot as plt

pool = ThreadPool(8)

"""
Processor scheduling in distributed systems (processor assignment for a process) simulation of algorithms: 
random
maximum threshold
minimum threshold
Compare CPU load, number of requests sent, number of process migrations. 
"""
print("default values?")
if int(input()) == 1:
    N = 80
    p = 80
    r = 15
    z = 3
    processes = 1000
else:
    print("How many processors?")
    N = int(input())  # number of processors
    print("Maximum threshold: ")
    p = int(input())  # maximum threshold
    print("Minimum threshold: ")
    r = int(input())  # minimum threshold
    print("Number of retries: ")
    z = int(input())  # number of retries
    print("Number of processes: ")
    processes = int(input())  # amount of processes


process_list = []
for i in range(processes):
    temp_process = pg.ProcessGen(N)
    process_list.append(temp_process)

TIME_MAX = 1500

lista = range(N, 100)


temp_process_list = copy.deepcopy(process_list)

func_random = partial(rd.random, temp_process_list, p, z, TIME_MAX)
func_max = partial(MxTh.maxThreshold, temp_process_list, p, TIME_MAX)
func_min = partial(MiTh.minThreshold, temp_process_list, p, r, TIME_MAX)

outputs_rand = pool.map(func_random, lista)
outputs_max = pool.map(func_max, lista)
outputs_min = pool.map(func_min, lista)

pool.close()
pool.join()


# temp_process_list = copy.deepcopy(process_list)
# output_rand.append(rd.random(temp_process_list, N, p, z, TIME_MAX))
# temp_process_list = copy.deepcopy(process_list)
# output_max.append(MxTh.maxThreshold(temp_process_list, N, p, TIME_MAX))
# temp_process_list = copy.deepcopy(process_list)
# output_min.append(MiTh.minThreshold(temp_process_list, N, p, r, TIME_MAX))


outputs_rand = np.asarray(outputs_rand)
outputs_max = np.asarray(outputs_max)
outputs_min = np.asarray(outputs_min)


np.set_printoptions(precision=2)
print("Random: {0}".format(outputs_rand[:, 0]))
print("Max: {0}".format(outputs_max[:, 0]))
print("Min: {0}".format(outputs_min[:, 0]))

# for i in range(len(output_rand)):
#     print(output_rand[i][0])
#
# for i in range(len(output_max)):
#     print(output_max[i][0])
#
# for i in range(len(output_min)):
#     print(output_min[i][0])

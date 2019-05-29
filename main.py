import ProcessGenerator as pg
import Random as rd

N = 100  # number of processors
p = 80
z = 3
processes = 1000  # number of processes
process_list = []
for i in range(processes):
    process_list.append(pg.ProcessGen(N))

TIME_MAX = 1500

print("Random processor request, average utilization of each processor:")
rd.random(process_list, N, p, z, TIME_MAX)

from Job import Job
from System import System
import random
import numpy
import copy
import csv
import matplotlib.pyplot as plt


#LAMBDAS = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
LAMBDAS = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
JOB_SIZE = 10

DEBUG = True

 # time for running simulation
TOTAL_SIMULATION_TIME = 5000

class Simulator:
    def __init__(self, arrival_rate, service_rate):
        self.arrival_rate = arrival_rate
        self.system = System(service_rate)

    def run(self, simulation_time):
        print("\nTime: 0 sec, Simulation starts for λ=" + str(self.arrival_rate))
        #current_time = random.expovariate(self.arrival_rate)
        current_time = numpy.random.poisson(1/(self.arrival_rate))
        this_jobs = {}  # map of id:job
        job_id = 1

        while current_time <= simulation_time:
            new_job = Job(current_time, job_id, self.system.service_rate)
            this_jobs[job_id] = new_job
            new_job.add_and_process_job_queue(self.system)
            new_job.add_and_process_job_queue2(self.system)
            new_job.add_and_process_job_queue3(self.system)

            self.system.handle_jobs(new_job)
            #current_time += random.expovariate(self.arrival_rate)
            current_time += numpy.random.poisson(1/(self.arrival_rate))
            job_id += 1

        self.system.finalize_jobs()
        print("Total jobs: " + str(len(this_jobs)))
        return this_jobs


def plot_simulation_delay_time_per_job(jobs, arrival_rate, sumarize):
    job_ids = [key for key in jobs]

    simulation_data = [job_ids, [jobs[job_id].job_delay_time for job_id in jobs]]

    simulation_delay_avg = sum(simulation_data[1]) / len(simulation_data[1])

    print("Average delay per job - SS: " + str(simulation_delay_avg))
    simulation_data_delay_averages = [job_ids, [simulation_delay_avg for job_id in jobs]]

    theoretical_data = [job_ids, [1 / ( JOB_SIZE - arrival_rate) for job_id in jobs]]

    sumarize[arrival_rate] = [simulation_delay_avg, 1 / ( JOB_SIZE - arrival_rate)]

def plot_simulation2_delay_time_per_job(jobs, arrival_rate, sumarize2):
    job_ids = [key for key in jobs]

    simulation2_data = [job_ids, [jobs[job_id].job_delay2_time for job_id in jobs]]

    simulation2_delay_avg = sum(simulation2_data[1]) / len(simulation2_data[1])


    print("Average delay per job - RS1: " + str(simulation2_delay_avg))
    simulation2_data_delay_averages = [job_ids, [simulation2_delay_avg for job_id in jobs]]


    theoretical2_data = [job_ids, [1 / (JOB_SIZE - arrival_rate) for job_id in jobs]]

    sumarize2[arrival_rate] = [simulation2_delay_avg, 1 / (JOB_SIZE - arrival_rate)]

def plot_simulation3_delay_time_per_job(jobs, arrival_rate, sumarize3):
    job_ids = [key for key in jobs]


    simulation3_data = [job_ids, [jobs[job_id].job_delay3_time for job_id in jobs]]

    simulation3_delay_avg = sum(simulation3_data[1]) / len(simulation3_data[1])

    print("Average delay per job - RS2: " + str(simulation3_delay_avg))
    simulation3_data_delay_averages = [job_ids, [simulation3_delay_avg for job_id in jobs]]

    theoretical3_data = [job_ids, [1 / (JOB_SIZE - arrival_rate) for job_id in jobs]]

    sumarize3[arrival_rate] = [simulation3_delay_avg, 1 / (JOB_SIZE - arrival_rate)]


"""def plot_simulationAll_delay_time_per_job(jobs, arrival_rate, sumarizeall):

    simulationall_data = [job_ids, [jobs[job_id].delay for job_id in jobs]]

    simulationall_delay_avg = sum(simulationall_data[1]) / len(simulationall_data[1])

    print("Average delay per job - RS2: " + str(simulationall_delay_avg))
    simulationall_data_delay_averages = [job_ids, [simulationall_delay_avg for job_id in jobs]]

    theoreticalall_data = [job_ids, [(1 / (JOB_SIZE - arrival_rate)) + (1 / (JOB_SIZE - arrival_rate)) + (1 / (JOB_SIZE - arrival_rate)) for job_id in jobs]]

    sumarizeall[arrival_rate] = [simulationall_delay_avg, (1 / (JOB_SIZE - arrival_rate)) + (1 / (JOB_SIZE - arrival_rate)) + (1 / (JOB_SIZE - arrival_rate))]
"""


if __name__ == '__main__':
    summary_results = {}
    summary2_results = {}
    summary3_results = {}
    summaryall_results = {}
    for this_lambda in LAMBDAS:
        simulator = Simulator(this_lambda, JOB_SIZE)
        the_jobs = simulator.run(TOTAL_SIMULATION_TIME)

        plot_simulation_delay_time_per_job(the_jobs, this_lambda, summary_results)
        plot_simulation2_delay_time_per_job(the_jobs, this_lambda, summary2_results)
        plot_simulation3_delay_time_per_job(the_jobs, this_lambda, summary3_results)
        #plot_simulationAll_delay_time_per_job(the_jobs, this_lambda, summaryall_results)


        if DEBUG:
            outDataFileName = "./jobs_" + str(this_lambda) + ".csv"
            outfile = open(outDataFileName, "w")
            writer = csv.writer(outfile)
            header = ['id', 'arrival', 'service time start', 'service time end', 'total delay', 'Service time',
                      'queue time', 'service2 time start', 'service2 time end', 'total delay2', 'Service2 time',
                      'queue2 time']
            writer.writerow(header)

            for job in the_jobs:
                job_data = []
                job_data.append(the_jobs[job].job_id)
                job_data.append(the_jobs[job].arrival_time)
                job_data.append(the_jobs[job].service_start_time)
                job_data.append(the_jobs[job].service_end_time)
                job_data.append(the_jobs[job].job_delay_time)
                job_data.append(the_jobs[job].service_time)
                job_data.append(the_jobs[job].queue_time)
                job_data.append(the_jobs[job].service2_start_time)
                job_data.append(the_jobs[job].service2_end_time)
                job_data.append(the_jobs[job].job_delay2_time)
                job_data.append(the_jobs[job].service2_time)
                job_data.append(the_jobs[job].queue2_time)
                writer.writerow(job_data)
            outfile.close()

    lamdas = [lamda for lamda in summary_results]
    lamdas2 = [lamda for lamda in summary2_results]
    lamdas3 = [lamda for lamda in summary3_results]
    lamdasall = [lamda for lamda in summaryall_results]

    the_simulation_data = [lamdas, [summary_results[lamda][0] for lamda in lamdas]]
    the_simulation2_data = [lamdas, [summary2_results[lamda][0] for lamda in lamdas2]]
    the_simulation3_data = [lamdas, [summary3_results[lamda][0] for lamda in lamdas3]]
    the_simulationall_data = [lamdas, [summaryall_results[lamda][0] for lamda in lamdasall]]
    the_theoretical_data = [lamdas, [summary_results[lamda][1] for lamda in lamdas]]
    the_theoretical2_data = [lamdas, [summary2_results[lamda][1] for lamda in lamdas]]
    the_theoretical3_data = [lamdas, [summary3_results[lamda][1] for lamda in lamdas]]
    the_theoreticalall_data = [lamdas, [summaryall_results[lamda][1] for lamda in lamdasall]]

    plt.figure("Comparison")
    axis = plt.subplot()

    #plt.plot(the_simulationall_data[0], the_simulationall_data[1], 'b--')
    #plt.plot(the_simulationall_data[0], the_simulationall_data[1], 'bo', label='SS + RS1 + RS2 delay time')

    #plt.plot(the_theoreticalall_data[0], the_theoreticalall_data[1], 'g--')
    #plt.plot(the_theoreticalall_data[0], the_theoreticalall_data[1], 'go', label='Theoretical All')


    plt.plot(the_simulation_data[0], the_simulation_data[1], 'b--')
    plt.plot(the_simulation_data[0], the_simulation_data[1], 'bo', label='Simulation SS delay time')

    plt.plot(the_theoretical_data[0], the_theoretical_data[1], 'g--')
    plt.plot(the_theoretical_data[0], the_theoretical_data[1], 'go', label='Theoretical SS')
    
    plt.plot(the_simulation2_data[0], the_simulation2_data[1], 'r:')
    plt.plot(the_simulation2_data[0], the_simulation2_data[1], 'rp', label='Simulation RS-1 delay time')
    
    plt.plot(the_simulation3_data[0], the_simulation3_data[1], 'm-')
    plt.plot(the_simulation3_data[0], the_simulation3_data[1], 'ms', label='Simulation RS-2 delay time')

    #plt.plot(the_theoretical2_data[0], the_theoretical2_data[1], 'y--')
    #plt.plot(the_theoretical2_data[0], the_theoretical2_data[1], 'yo', label='Theoretical RS-1')

    axis.set_xlabel('Lambda Value')
    axis.set_ylabel('Delay Time (secs)')
    axis.legend()
    axis.set_title("Simulation Vs steady-state: Avg Delay time on M/M/1 " + ", Simulation time: " + str(
        TOTAL_SIMULATION_TIME) + "secs")
    plt.show()
    plt.close()
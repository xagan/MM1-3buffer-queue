import random
import numpy as np
# class to create an object that represent a single job
class Job:
    def __init__(self, arrival_time, job_id, job_size):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.arrival2_time = arrival_time
        self.arrival3_time = arrival_time
        #self.service_time = random.expovariate(1 / job_size)
        #self.service2_time = random.expovariate(1 / job_size)
        #self.service3_time = random.expovariate(1 / job_size)
        self.service_time = np.random.exponential(1 / job_size)
        self.service2_time = np.random.exponential(1 / job_size)
        self.service3_time = np.random.exponential(1 / job_size)
        self.service_start_time = 0
        self.service2_start_time = 0
        self.service3_start_time = 0
        self.service_end_time = 0
        self.service2_end_time = 0
        self.service3_end_time = 0
        self.job_delay_time = 0
        self.job_delay2_time = 0
        self.job_delay3_time = 0
        self.queue_time = 0
        self.queue2_time = 0
        self.queue3_time = 0
        self.status = 0  # 0 for created, 1 for queued, 2 for processing, 3 for completed
        self.status2 = 0
        self.status3 = 0

    def add_and_process_job_queue(self, this_system):
        self.service_time = self.service_time
        self.service_start_time = max(self.arrival_time, this_system.latest_job_service_ending_time)
        self.service_end_time = self.service_start_time + self.service_time
        self.queue_time = self.service_start_time - self.arrival_time
        self.job_delay_time = self.queue_time + self.service_time
               

    def add_and_process_job_queue2(self, this_system):
        self.arrival2_time = this_system.latest_job_service_ending_time
        self.service2_time = self.service2_time
        self.service2_start_time = max(self.arrival2_time, this_system.latest_job_service2_ending_time)
        self.service2_end_time = self.service2_start_time + self.service2_time
        self.queue2_time = self.service2_start_time - self.arrival2_time
        self.job_delay2_time = self.queue2_time + self.service2_time


    def add_and_process_job_queue3(self, this_system):
        self.arrival3_time = this_system.latest_job_service2_ending_time 
        self.service3_time = self.service3_time
        self.service3_start_time = max(self.arrival3_time, this_system.latest_job_service3_ending_time)
        self.service3_end_time = self.service3_start_time + self.service3_time
        self.queue3_time = self.service3_start_time - self.arrival3_time
        self.job_delay3_time = self.queue3_time + self.service3_time

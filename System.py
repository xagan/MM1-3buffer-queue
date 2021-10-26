import copy

TOTAL_SIMULATION_TIME = 100000 


class System:
    def __init__(self, service_rate):
        self.service_rate = 10  # random.expovariate(self.service_rate)
        self.latest_job_service_ending_time = 0  # initially no job
        self.latest_job_service2_ending_time = 0
        self.latest_job_service3_ending_time = 0
        self.queue_list = []
        self.queue2_list = []
        self.queue3_list = []
        self.queue_summary_over_time = {}
        self.queue2_summary_over_time = {}
        self.queue3_summary_over_time = {}

    def handle_jobs(self, the_new_job):
        current_time = the_new_job.arrival_time
        self.latest_job_service_ending_time = the_new_job.service_end_time

        new_job_inserted = False
        finished_jobs = []
        temp_copy_of_jobs_in_sys = copy.copy(self.queue_list)

        for this_job in temp_copy_of_jobs_in_sys:
            if this_job.service_start_time <= current_time and this_job.status < 2:
                self.queue_summary_over_time[current_time] = len(self.queue_list)
                this_job.status = 2
                if this_job.service_end_time <= current_time:
                    this_job.status = 3
                    self.queue_list.remove(this_job)
                    self.queue_summary_over_time[current_time] = len(self.queue_list)
                    finished_jobs.append(this_job)
                else:
                    continue

            elif this_job.service_end_time <= current_time and this_job.status == 2:
                this_job.status = 3
                self.queue_list.remove(this_job)
                self.queue_summary_over_time[current_time] = len(self.queue_list)
                finished_jobs.append(this_job)

        if not new_job_inserted:
            # add current job to the system's jobs
            self.queue_list.append(the_new_job)
            # update queue summary
            self.queue_summary_over_time[current_time] = len(self.queue_list)

            the_new_job.status = 1 
#-------------------------------------------------------------------------------------------------------
        current_time2 = the_new_job.arrival2_time
        self.latest_job_service2_ending_time = the_new_job.service2_end_time

        new_job2_inserted = False
        finished2_jobs = []
        temp_copy_of_jobs_in_sys2 = copy.copy(self.queue2_list)

        for this_job in temp_copy_of_jobs_in_sys2:
            if this_job.service2_start_time <= current_time2 and this_job.status2 < 2:
                self.queue2_summary_over_time[current_time2] = len(self.queue2_list)
                this_job.status2 = 2
                if this_job.service2_end_time <= current_time2:
                    this_job.status2 = 3
                    self.queue2_list.remove(this_job)
                    self.queue2_summary_over_time[current_time2] = len(self.queue2_list)
                    finished2_jobs.append(this_job)
                else:
                    continue

            elif this_job.service2_end_time <= current_time2 and this_job.status2 ==2:
                this_job.status2 = 3
                self.queue2_list.remove(this_job)
                self.queue2_summary_over_time[current_time2] = len(self.queue2_list)
                finished2_jobs.append(this_job)

        if not new_job2_inserted:
            self.queue2_list.append(the_new_job)
            self.queue2_summary_over_time[current_time2] = len(self.queue2_list)
            the_new_job.status = 1 

#----------------------------------------------------------------------------------------------------------
        current_time3 = the_new_job.arrival3_time
        self.latest_job_service3_ending_time = the_new_job.service3_end_time

        new_job3_inserted = False
        finished3_jobs = []
        temp_copy_of_jobs_in_sys3 = copy.copy(self.queue3_list)

        for this_job in temp_copy_of_jobs_in_sys3:
            if this_job.service3_start_time <= current_time3 and this_job.status3 < 2:
                self.queue3_summary_over_time[current_time3] = len(self.queue3_list)
                this_job.status3 = 2
                if this_job.service3_end_time <= current_time3:
                    this_job.status3 = 3
                    self.queue3_list.remove(this_job)
                    self.queue3_summary_over_time[current_time3] = len(self.queue3_list)
                    finished3_jobs.append(this_job)
                else:
                    continue

            elif this_job.service3_end_time <= current_time3 and this_job.status3 ==2:
                this_job.status3 = 3
                self.queue3_list.remove(this_job)
                self.queue3_summary_over_time[current_time3] = len(self.queue3_list)
                finished3_jobs.append(this_job)

        if not new_job3_inserted:
            self.queue3_list.append(the_new_job)
            self.queue3_summary_over_time[current_time3] = len(self.queue3_list)
            the_new_job.status = 1



    def finalize_jobs(self):
        temp_copy_of_jobs_in_sys_at_end_time = copy.copy(self.queue_list)
        current_time = TOTAL_SIMULATION_TIME

        for this_job in temp_copy_of_jobs_in_sys_at_end_time:
            if this_job.status == 2:
                this_job.status = 3
                self.queue_list.remove(this_job)
                self.queue_summary_over_time[this_job.service_end_time] = len(self.queue_list)
                if this_job.service_end_time > current_time:
                    current_time = this_job.service_end_time
            elif this_job.status < 2:
                self.queue_summary_over_time[this_job.service_end_time] = len(self.queue_list)
                this_job.status = 2

                this_job.status = 3
                self.queue_list.remove(this_job)
                self.queue_summary_over_time[this_job.service_end_time] = len(self.queue_list)
                if this_job.service_end_time > current_time:
                    current_time = this_job.service_end_time

        print("Time: " + str(current_time) + "secs End of last job in the System")

#--------------------------------------------------------------------------------------------------------
        temp_copy_of_jobs_in_sys2_at_end_time = copy.copy(self.queue2_list)
        current_time2 = TOTAL_SIMULATION_TIME

        for this_job in temp_copy_of_jobs_in_sys2_at_end_time:
            if this_job.status2 == 2:
                this_job.status2 = 3
                self.queue2_list.remove(this_job)
                self.queue2_summary_over_time[this_job.service2_end_time] = len(self.queue2_list)
                if this_job.service2_end_time > current_time2:
                    current_time2 = this_job.service2_end_time
            elif this_job.status2 < 2:
                self.queue2_summary_over_time[this_job.service2_end_time] = len(self.queue2_list)
                this_job.status2 = 2

                this_job.status2 = 3
                self.queue2_list.remove(this_job)
                self.queue2_summary_over_time[this_job.service2_end_time] = len(self.queue2_list)
                if this_job.service2_end_time > current_time2:
                    current_time2 = this_job.service2_end_time

        print("Time: " + str(current_time2) + "secs End of last job in the System")
#---------------------------------------------------------------------------------------------------------------

        temp_copy_of_jobs_in_sys3_at_end_time = copy.copy(self.queue3_list)
        current_time3 = TOTAL_SIMULATION_TIME

        for this_job in temp_copy_of_jobs_in_sys3_at_end_time:
            if this_job.status3 == 2:
                this_job.status3 = 3
                self.queue3_list.remove(this_job)
                self.queue3_summary_over_time[this_job.service3_end_time] = len(self.queue3_list)
                if this_job.service3_end_time > current_time3:
                    current_time3 = this_job.service3_end_time
            elif this_job.status3 < 2:
                self.queue3_summary_over_time[this_job.service3_end_time] = len(self.queue3_list)
                this_job.status3 = 2

                this_job.status3 = 3
                self.queue3_list.remove(this_job)
                self.queue3_summary_over_time[this_job.service3_end_time] = len(self.queue3_list)
                if this_job.service3_end_time > current_time3:
                    current_time3 = this_job.service3_end_time

        print("Time: " + str(current_time3) + "secs End of last job in the System\nSimulation summary:")

#!/usr/bin/env python3

import os
import sys
import time

class Armstrong:
    def __init__(self):
        self.num, self.proc = 0, 0
        self.get_input()
        self.start_time = time.time()
        self.calculate(self.num, self.proc)

    def calculate(self, number, processes):
        for p in range(1, processes + 1):
            pid = os.fork()
            if pid == 0:
                pass
            elif pid > 0:
                child_nums = []
                for n in range(9 + p, number + 1, processes):
                    digits = str(n)
                    num_length = len(digits)
                    candidate_sum = 0
                    for digit in digits:
                        candidate_sum += int(digit) ** num_length
                    if candidate_sum == n:
                        child_nums.append(n)
                if child_nums:
                    self.write_child_process_numbers_to_file(pid, child_nums)
                    print(f'Child process PID: {pid} found {child_nums}')
                self.read_child_process_numbers_from_file()
                program_runtime = round((time.time() - self.start_time) * 1000)
                print(f'It took {program_runtime} milliseconds to complete the task.')
                all_nums = self.read_child_process_numbers_from_file()
                print(f'Armstrong numbers found: {all_nums}')
                os.waitpid(pid, 0)
                # self.read_child_process_numbers_from_file()
                # program_runtime = round((time.time() - self.start_time) * 1000)
                # print(f'It took {program_runtime} milliseconds to complete the task.')
                # self.read_child_process_numbers_from_file()
                exit(1)
            else:  # pid < 0
                raise OSError('Fork failed.')

    def write_child_process_numbers_to_file(self, pid, child_nums):
        with open(f'most_recent_execution.txt', 'w') as f:
            f.write(f'PID: {pid}\n')
            for num in child_nums:
                f.write(f'{num}, ')

    def read_child_process_numbers_from_file(self):
        all_nums = []
        with open(f'most_recent_execution.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line[:3] == 'PID':
                    continue
                all_nums.append(line)
        return all_nums

    def get_input(self):
        # add input validation
        self.num = int(input(f'Welcome to the Armstrong number calculator.\n'
                f'Please enter the maximum number to calculate '
                f'Armstrong numbers to (10 to 100,000,000): '))

        # add input validation
        self.proc = int(input(f'Please enter the number of processes to use: '))
        print(f'Numbers per process: {round(self.num / self.proc)}')


if __name__ == "__main__":
    a = Armstrong()

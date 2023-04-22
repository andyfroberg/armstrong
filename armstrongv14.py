#!/usr/bin/env python3

import os
import sys
import time


class Armstrong:
    def __init__(self):
        self.start_time = None
        self.num, self.proc = 0, 0
        self.get_input()
        self.start_time = time.time()
        self.calculate(self.num, self.proc)

    def calculate(self, number, processes):
        child_processes = []
        for p in range(1, processes + 1):
            child_processes.append(os.fork())

        for i, pid in enumerate(child_processes, start=1):
            if pid == 0:
                pass
            elif pid > 0:
                child_list = []
                for n in range(9 + i, number + 1, processes):
                    digits = str(n)
                    num_length = len(digits)
                    candidate_sum = 0
                    for digit in digits:
                        candidate_sum += int(digit) ** num_length
                    if candidate_sum == n:
                        child_list.append(n)
                if child_list:
                    print(f'Child process PID: {pid} found {child_list}')
                    self.write_child_nums_to_file(pid, child_list)
                os.waitpid(pid, 0)
                exit(0)
                    # program_runtime = round((time.time() - self.start_time) * 1000)
                    # print(f'It took {program_runtime} milliseconds to complete this task.')
            else:  # pid < 0
                raise OSError('Fork failed.')

        print(f'Armstrong numbers found: ')

    def write_child_nums_to_file(self, pid, child_nums):
        with open(f'nums/{pid}.txt', 'w') as f:
            f.write(f'[')
            for num in child_nums:
                f.write(f'{num}, ')
            f.write(f']')

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

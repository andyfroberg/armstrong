#!/usr/bin/env python3

import os
import sys
import time

def main():
    num, proc = get_input()
    start_time = time.time()
    calculate(num, proc, start_time)

def calculate(number, processes, start_time):
    child_processes = []
    child_list = []
    for p in range(1, processes + 1):
        pid = os.fork()
        if pid == 0:
            # pass  #calculate nums
            child_list = []
            for n in range(9 + p, number + 1, processes):
                digits = str(n)
                num_length = len(digits)
                candidate_sum = 0
                for digit in digits:
                    candidate_sum += int(digit) ** num_length
                if candidate_sum == n:
                    child_list.append(n)
            # if child_list:
            #     print(f'Child process PID: {pid} found {child_list}')
                # self.write_child_nums_to_file(pid, child_list)
        elif pid > 0:
            child_processes.append(pid)
        else:  # pid < 0
            raise OSError('Fork failed.')


    for pid in child_processes:
        print(f'Child process PID: {pid} found {child_list}')
        os.waitpid(pid, 0)
        exit(0)




    # for i, pid in enumerate(child_processes, start=1):
    #     if pid == 0:
    #         pass
    #     elif pid > 0:
    #         child_list = []
    #         for n in range(9 + i, number + 1, processes):
    #             digits = str(n)
    #             num_length = len(digits)
    #             candidate_sum = 0
    #             for digit in digits:
    #                 candidate_sum += int(digit) ** num_length
    #             if candidate_sum == n:
    #                 child_list.append(n)
    #         if child_list:
    #             print(f'Child process PID: {pid} found {child_list}')
    #             # self.write_child_nums_to_file(pid, child_list)
    #         if os.waitpid(pid, 0):
    #             child_processes.remove(pid)
    #             if not child_processes:
    #                 runtime = round((time.time() - start_time) * 1000)
    #                 print(f'Armstrong took {runtime} milliseconds')
    #     else:  # pid < 0
    #         raise OSError('Fork failed.')

def write_child_nums_to_file(pid, child_nums):
    with open(f'nums/{pid}.txt', 'w') as f:
        f.write(f'[')
        for num in child_nums:
            f.write(f'{num}, ')
        f.write(f']')

def get_input():
    # add input validation
    num = int(input(f'Welcome to the Armstrong number calculator.\n'
            f'Please enter the maximum number to calculate '
            f'Armstrong numbers to (10 to 100,000,000): '))

    # add input validation
    proc = int(input(f'Please enter the number of processes to use: '))
    print(f'Numbers per process: {round(num / proc)}')

    return num, proc


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import time


def main():
    num, proc = get_input()
    start_time = time.time()
    child_processes = []
    child_list = []
    for p in range(1, proc + 1):
        pid = os.fork()
        if pid < 0:
            raise OSError(f'Fork failed')
            exit(1)
        elif pid == 0:
            for n in range(9 + p, num + 1, proc):
                digits = str(n)
                num_length = len(digits)
                candidate_sum = 0
                for digit in digits:
                    candidate_sum += int(digit) ** num_length
                if candidate_sum == n:
                    child_list.append(n)
            if child_list:
                write_child_nums_to_file(os.getpid(), child_list)
                print(f'Child process PID: {os.getpid()} found {child_list}')
            ##### CITATION #####
            # Used the link below to find this code snippet
            # https://www.petercollingridge.co.uk/tutorials/python/running-multiple-processes-python/
            os._exit(0)
            ##### END CITATION #####
        else:  # pid > 0
            child_processes.append(pid)

    for pid in child_processes:
        os.waitpid(pid, 0)

    program_runtime = round((time.time() - start_time) * 1000)
    print(f'It took {program_runtime} milliseconds to complete this task.\n')
    print(f'Armstrong numbers found: {read_child_nums_from_file()}')
    clear_child_nums_files()


def write_child_nums_to_file(pid, child_nums):
    if not os.path.exists(f'nums'):
        os.mkdir(f'nums')
    with open(f'nums/{pid}.txt', 'w') as f:
        for num in child_nums:
            f.write(f'{num}\n')


def read_child_nums_from_file():
    all_nums = []
    for file in os.listdir(f'nums/'):
        if file == '.DS_Store':
            continue
        else:
            with open(f'nums/{file}', 'r') as r:
                nums = r.readlines()
                for num in nums:
                    # all_nums += f'{num[:-2]}'
                    all_nums.append(int(num))
    all_nums.sort()
    return str(all_nums)[1:-1]


def clear_child_nums_files():
    for file in os.listdir(f'nums/'):
        if file != '.DS_Store':
            try:
                os.remove(f'nums/{file}')
            except OSError as e:
                print(f'Problem deleting {file} at file path: nums/{file}.')


def get_input():
    print(f'Welcome to the Armstrong number calculator.')
    while True:
        try:
            num = int(input(f'Please enter the maximum number to calculate '
                            f'Armstrong numbers to (10 to 100,000,000): '))
            if num < 10 or num > 100_000_000:
                raise ValueError
            break
        except ValueError as e:
            print(f'You entered an invalid input.')

    while True:
        try:
            proc = int(input(f'Please enter the number of processes to use: '))
            break
        except ValueError as e:
            print(f'You entered an invalid input.')

    print(f'Numbers per process: {round((num - 9)/ proc)}')  # nums doesn't include 1-9

    return num, proc


if __name__ == "__main__":
    main()

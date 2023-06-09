import os
import sys

import time

class Armstrong:
    def __init__(self):
        self.a_nums_found = []

    def calculate(self, number, processes):
        for i in range(10, number + 1):
            digits = str(i)
            num_length = len(digits)
            sum = 0
            for digit in digits:
                sum += int(digit) ** num_length

            if sum == i:
                self.a_nums_found.append(i)

    def get_input(self):
        number = int(input(f'Please enter the maximum number to calculate '
                       f'Armstrong numbers to (10 to 100,000,000): '))
        processes = int(input(f'Please enter the number of processes to use: '))

        return number, processes

    def print_output(self):
        print(self.a_nums_found)

if __name__ == "__main__":
    a = Armstrong()
    num, proc = a.get_input()
    start_time = time.time()
    a.calculate(num, proc)
    program_runtime = round((time.time() - start_time) * 1000)
    a.print_output()
    print(f'It took {program_runtime} milliseconds to complete'
          f' this task.')
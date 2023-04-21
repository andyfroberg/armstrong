import os
import sys
import time

class ArmstrongParallel:
    def __init__(self):
        self.a_nums_found = []
        self.start_time = None
        self.num, self.proc = self.get_input()
        self.calculate(self.num, self.proc)
        # self.display_output(self.all_nums)

    def calculate(self, number, processes):
        self.start_time = time.time()
        for p in range(1, processes + 1):
            pid = os.fork()
            if pid == 0:
                pass
            elif pid > 0:
                child_list = []
                for n in range(9 + p, number + 1, processes):
                    digits = str(n)
                    num_length = len(digits)
                    sum = 0
                    for digit in digits:
                        sum += int(digit) ** num_length
                    if sum == n:
                        child_list.append(n)
                if child_list:
                    ArmstrongParallel.print_child_process_list_to_console(
                        os.getpid(), child_list)
                if child_list:
                    self.a_nums_found.append(child_list)
                os.waitpid(pid, 0)
                program_runtime = round((time.time() - self.start_time) * 1000)
                print(f'It took {program_runtime} milliseconds to complete'
                      f' this task.')
                print(f'Armstrong numbers found: {self.a_nums_found}')
                return self.a_nums_found
                exit(1)
            else:  # pid < 0
                raise OSError('Fork failed.')

    @staticmethod
    def print_child_process_list_to_console(pid, child_list):
        print(f'Child process PID: {pid} found {child_list}')


    def get_input(self):
        # add input validation
        number = int(input(f'Welcome to the Armstrong number calculator.\n'
                f'Please enter the maximum number to calculate '
                f'Armstrong numbers to (10 to 100,000,000): '))

        # add input validation
        processes = int(input(f'Please enter the number of processes to use: '))
        print(f'Numbers per process: {round(number / processes)}')

        return number, processes

    def display_output(self, child_lists):
        all_armstrong_nums = []
        for l in child_lists:
            for sl in l:
                all_armstrong_nums.append(sl)

        print(all_armstrong_nums.sort())


if __name__ == "__main__":
    a = ArmstrongParallel()

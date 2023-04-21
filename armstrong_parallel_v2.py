import os
import sys
import time

class ArmstrongParallel:
    def __init__(self):
        self.a_nums_found = []
        self.start_time = None

    def assign_processes(self, number, processes):
        for p in range(1, processes + 1):
            pid = os.fork()
            for n in range(9 + p, number + 1, processes):
                if pid == 0:  # child process
                    child_list = []
                    digits = str(n)
                    num_length = len(digits)
                    sum = 0
                    for digit in digits:
                        sum += int(digit) ** num_length

                    if sum == n:
                        child_list.append(n)
                        self.a_nums_found.append(n)
                    if child_list:
                        print(f'Child process PID: {os.getpid()} found {child_list}')
                elif pid > 0:  # parent process
                    os.waitpid(pid, 0)
                    exit(1)
                else:  # pid < 0
                    raise OSError('Fork failed.')

    def calculate(self, number, processes):
        self.start_time = time.time()
        for p in range(1, processes + 1):
            pid = os.fork()
            if pid == 0:  # child process
                pass
                # child_list = []
                # for n in range(9 + p, number + 1, processes):
                #     digits = str(n)
                #     num_length = len(digits)
                #     sum = 0
                #     for digit in digits:
                #         sum += int(digit) ** num_length
                #
                #     if sum == n:
                #         child_list.append(n)
                #         self.a_nums_found.append(n)
                # if child_list:
                #     ArmstrongParallel.print_child_process_list_to_console(os.getpid(), child_list)
            elif pid > 0:  # parent process
                child_list = []
                for n in range(9 + p, number + 1, processes):
                    digits = str(n)
                    num_length = len(digits)
                    sum = 0
                    for digit in digits:
                        sum += int(digit) ** num_length

                    if sum == n:
                        child_list.append(n)
                        self.a_nums_found.append(n)
                if child_list:
                    ArmstrongParallel.print_child_process_list_to_console(
                        os.getpid(), child_list)
                os.waitpid(pid, 0)
                # if n == number:
                program_runtime = round((time.time() - self.start_time) * 1000)
                print(f'It took {program_runtime} milliseconds to complete'
                      f' this task.')
                print(f'Armstrong numbers found: {self.a_nums_found}')
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


if __name__ == "__main__":
    a = ArmstrongParallel()
    num, proc = a.get_input()
    # start_time = time.time()
    a.calculate(num, proc)
    # program_runtime = round((time.time() - start_time) * 1000)
    # print(f'It took {program_runtime} milliseconds to complete'
    #       f' this task.')
    # print(f'Armstrong numbers found: {a.a_nums_found}')
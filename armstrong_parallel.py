import os
import sys
import time

class ArmstrongParallel:
    def __init__(self):
        self.a_nums_found = []

    def calculate(self, number, processes):
        # process_lists = [[] for _ in range(processes + 1)]

        # for p in range(1, processes + 1):
        #     child_id = os.fork()
        #     child_list = []
        #
        #     if child_id < 0:
        #         raise OSError('Fork failed.')
        #     elif child_id == 0:
        #         # child process
        #         for i in range(9 + p, number + 1, processes):
        #             digits = str(i)
        #             num_length = len(digits)
        #             sum = 0
        #             for digit in digits:
        #                 sum += int(digit) ** num_length
        #
        #             if sum == i:
        #                 child_list.append(i)
        #                 self.a_nums_found.append(i)
        #     else:  # parent process
        #         os.waitpid(child_id, 0)  # maybe not needed
        #         pass
        # return child_list

        # for p in range(1, processes + 1):
        #     pid = os.fork()
        #     child_list = []
        #     for n in range(9 + p, number + 1, processes):
        #         if pid == 0:
        #             digits = str(n)
        #             num_length = len(digits)
        #             total = 0
        #             for digit in digits:
        #                 total += int(digit) ** num_length
        #             if total == n:
        #                 child_list.append(n)
        #                 self.a_nums_found.append(n)
        #         elif pid > 0:  # parent
        #             wval = os.waitpid(pid, 0)
        #             print(child_list)
        #             print(self.a_nums_found.sort())
        #         else:  # child_id < 0
        #             raise OSError(f'Fork failed.')
        # return child_list

        for p in range(1, processes + 1):
            pid = os.fork()

            if pid < 0:
                raise OSError('Fork failed.')
            elif pid == 0:
                # child process
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
                    print(f'Child process PID: {os.getpid()} found {child_list}')
            else:  # parent process
                os.waitpid(pid, 0)
                exit(1)

    def get_input(self):
        # add input validation
        number = int(input(f'Welcome to the Armstrong number calculator.\n'
                f'Please enter the maximum number to calculate '
                f'Armstrong numbers to (10 to 100,000,000): '))

        # add input validation
        processes = int(input(f'Please enter the number of processes to use: '))
        print(f'Numbers per process: {round(number / processes)}')

        return number, processes

    # def print_output(self):
    #     print(self.a_nums_found)

if __name__ == "__main__":
    a = ArmstrongParallel()
    num, proc = a.get_input()
    start_time = time.time()
    a.calculate(num, proc)
    program_runtime = round((time.time() - start_time) * 1000)
    print(f'It took {program_runtime} milliseconds to complete'
          f' this task.')
    print(f'Armstrong numbers found: {a.a_nums_found}')
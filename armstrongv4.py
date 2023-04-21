import os
import sys
import time

class Armstrong:
    def __init__(self):
        self.a_nums_found = []
        self.start_time = None
        self.num, self.proc = 0, 0
        self.get_input()
        self.calculate(self.num, self.proc)

    def calculate(self, number, processes):
        self.start_time = time.time()
        for p in range(1, processes + 1):
            pid = os.fork()
            if pid == 0:
                for n in range(9 + p, number + 1, processes):
                    digits = str(n)
                    num_length = len(digits)
                    candidate_sum = 0
                    for digit in digits:
                        candidate_sum += int(digit) ** num_length
                    if candidate_sum == n:
                        self.a_nums_found.append(n)
                print(f'Child process PID: {os.getpid()} found {self.a_nums_found}')
            elif pid > 0:
                # for n in range(9 + p, number + 1, processes):
                #     digits = str(n)
                #     num_length = len(digits)
                #     candidate_sum = 0
                #     for digit in digits:
                #         candidate_sum += int(digit) ** num_length
                #     if candidate_sum == n:
                #         self.a_nums_found.append(n)
                program_runtime = round((time.time() - self.start_time) * 1000)
                print(f'It took {program_runtime} milliseconds to complete'
                      f' this task.')
                os.waitpid(pid, 0)
                # print(f'Child process PID: {pid} found {self.a_nums_found}')
                # return self.a_nums_found
                exit(1)
            else:  # pid < 0
                raise OSError('Fork failed.')

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

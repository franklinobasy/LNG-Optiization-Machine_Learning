from typing import Any, Callable, Tuple, Union
import numpy as np
class Optimize:
        '''A class that helps optimize output to a function


        '''
        def __init__(self, func, input_, spaces, output) -> None:
                '''Initialize object

                func: model or function to optimize. Requires a single list type arg
                input: Arg to the function. List or tuple type
                spaces: search space. A list of tuple element where each tuple contains a lower limit and an upper limit.
                output: initial func output. This is the value that is meant to be optimize.
                '''

                assert len(input_) == len(spaces), "input and spaces must be iterables of equal length"

                self.func = func
                self.input = input_ #np.reshape(np.array(input), (1, -1))
                self.spaces = spaces
                self.output= output

        

        def maximize(self) -> Tuple[list, np.array, int]:
                '''This method finds the inputs that maximizes func
                '''
                iteration = 0
                n = len(self.input)
                print("maximizing...")
                for i in range(n):
                        temp = self.input.copy()
                        sp = self.spaces[i]
                        if not sp:
                                input[i] = temp[i]
                                continue
                        else:
                                up = sp[0]
                                down = sp[1]
                                search_space = np.linspace(up, down, 1000)

                                np.random.shuffle(search_space)
                                for j in search_space:
                                        temp[i] = j
                                        new_output = self.func([temp])
                                        iteration += 1
                                        if new_output[0, 0] > self.output[0, 0]:
                                                self.output = new_output
                                                self.input[i] = j
                                                break
                print("number of iterations = ", iteration)
                return self.input, self.output, iteration

# Python_BI_2022

In this homework, the following functions were implemented:
- __sequential_map__: the function must take as arguments any number of functions (positional arguments, NOT a list) and a container with some values. The function must return a list of the results of successively applying the passed functions to the values in the container. For example, `sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5])` -> [1, 8, 27, 64, 125]

- __consensus_filter__: The function must accept any number of functions as arguments (
positional arguments, NOT a list), returning True or False, and a container with some values. The function must return a list of values that evaluate `True` when passed to all functions. For example: `consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11])` -> [6]

- __conditional_reduce__: The function must take two functions and a container with values. The first function must take one argument and return `True` or `False`; the second also takes two arguments and returns a value (as in the normal reduce function). conditional_reduce must return a single value - the result of reducing, skipping the values with which the first function returned False. For example, `conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10])` -> 4

- __func_chain__: The function must take any number of functions as arguments (positional arguments, NOT a list). The function must return a function concatenating all passed by sequential execution. For example, `my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4))`. `my_chain(37)` -> (9.75, 9).

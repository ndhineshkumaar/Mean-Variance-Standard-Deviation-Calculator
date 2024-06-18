import numpy as np

def calculate(list1):
    if len(list1) != 9:
        raise ValueError("The list must contain exactly 9 elements.")
    inp = np.array(list1).reshape(3, 3)
    calculation = {}

    # mean
    meanlst = [list(np.mean(inp, axis=0)), list(np.mean(inp, axis=1)), np.mean(inp)]
    calculation['mean'] = meanlst

    # variance
    variancelst = [list(np.var(inp, axis=0)), list(np.var(inp, axis=1)), np.var(inp)]
    calculation['variance'] = variancelst

    # SD
    sd = [list(np.std(inp, axis=0)), list(np.std(inp, axis=1)), np.std(inp)]
    calculation['standard deviation'] = sd

    # max
    max_val = [list(np.max(inp, axis=0)), list(np.max(inp, axis=1)), np.max(inp)]
    calculation['max'] = max_val

    # min
    min_val = [list(np.min(inp, axis=0)), list(np.min(inp, axis=1)), np.min(inp)]
    calculation['min'] = min_val

    # sum
    sum_val = [list(np.sum(inp, axis=0)), list(np.sum(inp, axis=1)), np.sum(inp)]
    calculation['sum'] = sum_val

    print(calculation)

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

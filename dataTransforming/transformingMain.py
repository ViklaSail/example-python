
import numpy as np
def transformationForData(cell):
    # Should return transformed data, this one works line by line modifying data. Now t
    #transformedData="something"
    result = np.square(cell) if cell.name == 'A' else cell
    result2 = result + 10 if cell.name == 'B' else result
    return result2

def transformationTestingWithApply(cell):
    #https://thispointer.com/pandas-apply-a-function-to-single-or-selected-columns-or-cells-in-dataframe/
    # so called ternary if operations used in example, makes also code more readable as well as short
    result = np.square(cell) if cell.name == 'A' else cell
    result2 = columnBHandling(cell) if cell.name == 'B' else result
    return result2

def columnBHandling(cell):
    result = cell - 5
    return result


def transformFoo():
    return "something"

# REAL FUNCTIONS BELOW THIS FILE

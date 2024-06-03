# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def calculate(arrayNum):
    if(len(arrayNum)< 9):
        raise Exception("List must contain nine numbers")
    # Use a breakpoint in the code line below to debug your script.
    myDict = {}
    matrixNum = np.array(arrayNum)
    matrixNum = matrixNum.reshape(3, 3)

    # obtain mean of each axis and general
    data = []
    data.append(np.array(matrixNum.mean(axis=0)).tolist())
    data.append(np.array(matrixNum.mean(axis=1)).tolist())
    data.append(matrixNum.mean())

    myDict["mean"] = data

    ##VARIANCE
    data = []
    data.append(np.array(matrixNum.var(axis=0)).tolist())
    data.append(np.array(matrixNum.var(axis=1)).tolist())
    data.append(matrixNum.var())

    myDict["variance"] =data

    ##standard deviation
    data = []
    data.append(np.array(matrixNum.std(axis=0)).tolist())
    data.append(np.array(matrixNum.std(axis=1)).tolist())
    data.append(matrixNum.std())
    myDict["standard deviation"] = data

    ##MAX
    data = []
    data.append(np.array(matrixNum.max(axis=0)).tolist())
    data.append(np.array(matrixNum.max(axis=1)).tolist())
    data.append(matrixNum.max())
    myDict["max"] = data

    ##MIN
    data = []
    data.append(np.array(matrixNum.min(axis=0)).tolist())
    data.append(np.array(matrixNum.min(axis=1)).tolist())
    data.append(matrixNum.min())
    myDict["min"] = data

    ##SUM
    data = []
    data.append(np.array(matrixNum.sum(axis=0)).tolist())
    data.append(np.array(matrixNum.sum(axis=1)).tolist())
    data.append(matrixNum.sum())
    myDict["sum"] = data

    print(myDict)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate([0,1,2,3,4,5,6,7,8])


from multiprocessing import Process, Manager
import numpy as np
from scipy.stats import logistic
import argparse
import time

# gradient descent to update theta
def gradientDescent(parameters, result):
	for parameter in parameters:
	    summition = 0
	    for sample in data_array:
	        summition += (hypothesis(sample[:-1], theta) - sample[-1]) * sample[parameter] 
        # regularization to avoid Overfitting
	    if parameter != 0:
	        summition += 10000 * theta[parameter]
	    result[parameter] = learning_rate * summition / number_of_examples

# logistic function
def sigmoid(value):
    return logistic.cdf(value)

def hypothesis(X, theta):
    hx = np.dot(theta, X)
    return sigmoid(hx)

#Initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="input file name")
parser.add_argument("-l", "--learning_rate", type=float, help="learning rate")
parser.add_argument("-i", "--iterations", type=int, help="number of iteration")
args = parser.parse_args()
if args.filename:
    filename = args.filename
else:
    print('Please specify a file name')
    print('Execute "python logistic.py -h" for help')
    exit()

if args.learning_rate:
    learning_rate = args.learning_rate
else:
    learning_rate = 1
    print('Using default learning rate', learning_rate)

if args.iterations:
    iterations = args.iterations
else:
    iterations = 100
    print('Using default iterations', iterations)

# read data file
data_array = np.loadtxt(filename, delimiter=',')
# number of training examples and features
number_of_examples = data_array.shape[0] 
number_of_parameters = data_array.shape[1]
# add column of ones to dataframe  make looping symmetric 
ones = np.ones(number_of_examples)
data_array = np.insert(data_array, 0, values=ones, axis=1)
# initialize theta to zeroes array
theta = np.zeros(number_of_parameters)
parameters_split = np.array_split(list(range(len(theta))), 4)

if __name__ == '__main__':
    manager = Manager()
    results = manager.dict()
    start = time.time()
    for i in range(iterations):
        processes = []
        # multiple process to caculate theta (4 sublist of theta)
        for j in range(len(parameters_split)):
            processes.append(Process(target=gradientDescent, args=(parameters_split[j], results)))
        theta_diff = []
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        # here to merge
        for j in range(len(theta)):
            theta_diff.append(results[j])
        theta = theta - theta_diff
        print("round: ", i)
    end = time.time()
    #print total time
    print(end - start)

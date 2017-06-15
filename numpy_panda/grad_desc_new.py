import numpy
import pandas

import numpy
import pandas

def normalize_features(array):
    array_normalized = (array-array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()
    
    return array_normalized, mu, sigma



def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
 
    sum_of_square_errors = numpy.square(numpy.dot(features, theta)- values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    count = 0
    cost_history = []
    m = len(values)
    
    while count < num_iterations:
        if theta is not None:
            predicted_values = numpy.dot(features,theta)
            theta = theta - alpha / m * numpy.dot((predicted_values - values),features) 
        else:
            theta = - alpha / m * numpy.dot(values,features)
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
    return theta, pandas.Series(cost_history)


data = pandas.read_csv('../t-tests/baseball_data.csv')
features = data[['height','weight']].fillna(0)
values = data[['HR']].fillna(0)
m = len(values)
#features, mu, sigma = normalize_features(features)
#theta = numpy.array([0,0]).reshape(2,1)
#values = numpy.array(values)


print(gradient_descent(features, values,None, 0.07, 10)[0])

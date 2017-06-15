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
    theta_flipped = numpy.array(theta).reshape(numpy.size(theta,1),numpy.size(theta,0))
    sum_of_square_errors = numpy.square(numpy.dot(features, theta_flipped)- values).sum()
    cost = sum_of_square_errors / (2*m)
    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    count = 0
    cost_history = []
    m = len(values)
    values_flipped = numpy.array(values).reshape(numpy.size(values,1),numpy.size(values,0))

    while count < num_iterations:
        
        if theta is not None:
            theta_flipped = numpy.array(theta).reshape(numpy.size(theta,1),numpy.size(theta,0))
            predicted_values = numpy.dot(features,theta_flipped)
            theta = theta - (alpha / m ) * numpy.dot((predicted_values - values_flipped),features) 
        else:

            ndot = numpy.dot(-values_flipped, features.astype(float))
            theta = - (alpha / m) * ndot
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
        count = count+1
    return theta, pandas.Series(cost_history)

MAX_SIZE = 100
MAX_ITER = 50
data = pandas.read_csv('baseball_stats.csv')
features_s = data.loc[0:MAX_SIZE,['height','weight']].fillna(0)
features = features_s.apply(pandas.to_numeric,errors='coerce').fillna(0)
values = data.loc[0:MAX_SIZE,['avg']].fillna(0)
values = numpy.array(values)
print(features)
print(values)
result = gradient_descent(features, values,None, +0.00000001, MAX_ITER)
print(result[1])
print(result[0])

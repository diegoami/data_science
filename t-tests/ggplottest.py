data = pandas.read_csv('baseball_data.csv')
features = data[['height','weight']].fillna(0)
values = data[['avg']].fillna(0)
values = numpy.array(values)

result = gradient_descent(features, values,None, +0.00000001, 5000)
print( result)
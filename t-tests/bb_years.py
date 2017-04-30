from pandas import *
from ggplot import *


data = pandas.read_csv('hr_year.csv')
gg = ggplot(data, aes('yearID', 'HR')) + geom_point(color = 'red') + geom_line(color='red') + \
    ggtitle('title') + xlab('yearID') + ylab('HR')

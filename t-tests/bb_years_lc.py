from pandas import *
from ggplot import *


data = pandas.read_csv('bb_years_hr.csv')

gg = ggplot(data, aes('yearID', 'HR', color='teamID')) +  geom_line() + geom_point() + ggtitle('title') + xlab('yearID') + ylab('HR')
print(gg)
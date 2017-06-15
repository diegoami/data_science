from pandas import *
from ggplot import *
from numpy import *


weather_data = pandas.read_csv('turnstile_data_master_with_weather.csv')
sample_data = weather_data.sample(frac=0.1).fillna(0)
#print(sample_data.describe()) 
gg = ggplot(weather_data , aes('Hour', 'ENTRIESn_hourly')) +  geom_line() + geom_point() + ggtitle('title') + xlab('Hour') + ylab('ENTRIESn_hourly')
gg.make()
print(gg)
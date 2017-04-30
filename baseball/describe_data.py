import pandas

def describe_data(path_to_csv):
    data = pandas.read_csv(path_to_csv)
    print( data.describe() )
   
path_to_csv = "Master.csv"
describe_data(path_to_csv)
    
    

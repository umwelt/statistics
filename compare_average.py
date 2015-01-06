import numpy
import scipy.stats
import pandas


def compare_averages(filename):
    filename = "../statistics/baseball_data.csv"
    baseball_data = pandas.read_csv(filename)
    righthand = baseball_data[baseball_data['handedness'] == 'R']
    lefthand = baseball_data[baseball_data['handedness'] == 'L']
    
    result = scipy.stats.ttest_ind(righthand['avg'], lefthand['avg'], equal_var=False)
    
    if result[1] >= 0.95:
        return(True, result)
    else:
        return(False, result)

if __name__ == '___main__':
    result = compare_averages()
    print result
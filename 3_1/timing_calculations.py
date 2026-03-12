import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as lr
import time
import math


def measure_time(func):
    # Decorator that measures and reports the time taken by a given function
    def wrap(*args, **kwargs):
        ################################################################
        # WRITE CODE HERE TO FIX 'start_time' AND 'total_time'
        start_time = time.time()
        result = func(*args, **kwargs)  # This line does not need fixing
        total_time = time.time() - start_time
        ################################################################
        print("Function '{}' took approximately {:.5f} seconds.".format(func.__name__, total_time))
        return result

    return wrap


@measure_time
def calculate_mean_manually(column):
    # Gets parameter 'column' as a list, returns its arithmetic mean
    # Calculations are done manually / "by hand" (not using external libraries)
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    mean = sum(column) / len(column)
    ###############################
    return mean


@measure_time
def calculate_sd_manually(column):
    # Gets parameter 'column' as a list, returns its standard deviation
    # Calculations are done manually / "by hand" (not using external libraries)
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    mean = calculate_mean_manually(column)
    square_sum = 0
    for grade in column:
        grade_diff = grade - mean
        square_sum += grade_diff * grade_diff
    temp = square_sum / len(column)
    sd = math.sqrt(temp)
    #############################
    return sd


@measure_time
def calculate_linreg_manually(column1, column2):
    # Gets parameters 'column1' and 'column2' as lists, returns the intercept and slope of their OLS regression
    # Calculations are done manually / "by hand" (not using external libraries)
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    n = len(column1)
    sum_x = sum(column1)
    sum_y = sum(column2)
    sum_xx = sum([x**2 for x in column1])
    sum_xy = sum([x*y for (x,y) in zip(column1,column2)])

    div = n * sum_xx - sum_x**2
    intercept = ((sum_y * sum_xx) - (sum_x * sum_xy)) / div
    slope = (n * sum_xy - sum_x * sum_y) / div
    ################################################
    return intercept, slope


@measure_time
def calculate_mean_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its arithmetic mean
    # Calculations are done using external libraries
    ###############################
    # WRITE CODE HERE TO FIX 'mean'
    mean = np.mean(column)
    ###############################
    return mean


@measure_time
def calculate_sd_automatically(column):
    # Gets parameter 'column' as a Pandas Series object (i.e. DataFrame column), returns its standard deviation
    # Calculations are done using external libraries
    #############################
    # WRITE CODE HERE TO FIX 'sd'
    sd = np.std(column)
    #############################
    return sd


@measure_time
def calculate_linreg_automatically(column1, column2):
    # Gets parameters 'column1' and 'column2' as separate Pandas DataFrame objects,
    # returns the intercept and slope of their OLS regression
    # Calculations are done using external libraries
    ################################################
    # WRITE CODE HERE TO FIX 'intercept' AND 'slope'
    model = lr()
    model.fit(column1,column2)
    intercept, slope = model.intercept_.item(), model.coef_[0][0].item()
    ################################################
    return intercept, slope


def main():
    print("Comparison of processing times between manual calculations and libraries")

    # Generates a semi-random DataFrame with two columns and between 500 000 and 2 000 000 rows
    # Both columns consist of integers normally distributed around a random value between 0 and 100
    # Some level of covariance between the two columns is randomly created
    seed = int(input('\nEnter a seed for generating the random DataFrame:\n'))
    np.random.seed(seed)
    means = np.array([np.random.randint(0, 100), np.random.randint(0, 100)])
    covariance = np.random.rand() * 2 - 1
    covariance_matrix = np.array([[1, covariance], [covariance, 1]])
    df = pd.DataFrame(np.random.multivariate_normal(means, covariance_matrix, size=np.random.randint(500000, 2000000)),
                      columns=['A', 'B'])
    print("Created a DataFrame of {} columns and {} rows.".format(df.shape[1], df.shape[0]))

    # Calculates statistics using the "manual" (non-library) functions
    print('\nCalculating statistics manually...')
    manual_results = {}
    manual_results['mean'] = calculate_mean_manually(df['A'].tolist())
    manual_results['sd'] = calculate_sd_manually(df['A'].tolist())
    manual_results['intercept'], manual_results['slope'] = calculate_linreg_manually(df['A'].tolist(), df['B'].tolist())

    # Calculates statistics using the "automatic" (library) functions
    print('\nCalculating statistics using the libraries...')
    library_results = {}
    library_results['mean'] = calculate_mean_automatically(df['A'])
    library_results['sd'] = calculate_sd_automatically(df['A'])
    library_results['intercept'], library_results['slope'] = calculate_linreg_automatically(df[['A']], df[['B']])

    # Checks if the results do not match sufficiently accurately (0.1 % tolerance)
    # Prints error message if results do not match; prints results if they do match
    for key in manual_results:
        if not math.isclose(manual_results[key], library_results[key], rel_tol=0.001):
            print("\nDifferences found between the '{}' results – at least one calculation is incorrect.".format(key))
            break
    else:
        print("\nThe arithmetic mean of Column A is {:.4f}.".format(manual_results['mean']))
        print("The standard deviation of Column A is {:.4f}.".format(manual_results['sd']))
        print("The linear regression relationship between Columns A and B is roughly 'B = {:.4f} + {:.4f} × A'."
              .format(manual_results['intercept'], manual_results['slope']))


if __name__ == "__main__":
    main()
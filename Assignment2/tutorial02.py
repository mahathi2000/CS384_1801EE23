# All decimal 3 places
import math

# Function to compute mean


def mean(first_list):
    # mean Logic
    mean_value = summation(first_list)/len(first_list)
    return round(mean_value, 6)


# Function to compute median. You cant use Python functions
def median(first_list):
   # median Logic
    sorted_list = sorting(first_list)
    for i in first_list:
        if (isinstance(i, (int, float)) == False):
            return 0
    n = len(sorted_list)
    if n % 2 == 0:
        median1 = sorted_list[n//2]
        median2 = sorted_list[n//2 - 1]
        median_value = (median1 + median2)/2
    else:
        median_value = sorted_list[n//2]
    return round(median_value, 6)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    standard_deviation_value = math.sqrt(variance(first_list))
    return round(standard_deviation_value, 6)


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    n = len(first_list)
    avg_val = mean(first_list)
    a = []
    for i in range(n):
        if (isinstance(i, (int, float)) == False):
            return 0
        a.append((first_list[i]-avg_val)*(first_list[i]-avg_val))
    variance_value = summation(a)/n

    return round(variance_value, 6)


# Function to compute RMSE. You cant use Python functions
# def rmse(first_list, second_list):
    # RMSE Logic
#    rmse_value = math.sqrt(mse(first_list, second_list))
#    return round(rmse_value, 6)


# Function to compute mse. You cant use Python functions
# def mse(first_list, second_list):
    # mse Logic
#    if (len(first_list) != len(second_list)):
#        return 0

#    for i, j in zip(first_list, second_list):
#        if (isinstance(i, (int, float)) == False or isinstance(j, (int, float)) == False):
#            return 0

#    new_list = []

#    for i, j in zip(first_list, second_list):
#        new_list.append((i - j)*(i-j))
#
#    mse_val = summation(new_list) / len(first_list)

#    mse_value = round(mse_val, 6)
#    return mse_value


# Function to compute mae. You cant use Python functions
# def mae(first_list, second_list):
    # mae Logic
#    if (len(first_list) != len(second_list)):
#        return 0

#    for i, j in zip(first_list, second_list):
#        if (isinstance(i, (int, float)) == False or isinstance(j, (int, float)) == False):
#            return 0

#    new_list = []

#    for i, j in zip(first_list, second_list):
#        new_list.append(abs(i - j))

#    mae_val = summation(new_list) / len(first_list)

#    mae_value = round(mae_val, 6)

#    return mae_value


# Function to compute NSE. You cant use Python functions
# def nse(first_list, second_list):
    # nse Logic
#    num = []
#    den = []
#    x_mean = mean(first_list)
#    for i, j in zip(first_list, second_list):
#        if (isinstance(i, (int, float)) == False or isinstance(j, (int, float)) == False):
#            return 0
#        num.append((i-j)**2)
#        den.append((i-x_mean)**2)
#    nse_value = 1-(summation(num)/summation(den))
#    return round(nse_value, 6)


# Function to compute Pearson correlation coefficient. You cant use Python functions
# def pcc(first_list, second_list):
    # nse Logic
#    x_mean = mean(first_list)
#    y_mean = mean(second_list)
#    num = []
#    den1 = []
#    den2 = []
#    for i, j in zip(first_list, second_list):
#        if (isinstance(i, (int, float)) == False or isinstance(j, (int, float)) == False):
#            return 0
#        num.append((i-x_mean)*(j-y_mean))
#        den1.append((i-x_mean)**2)
#        den2.append((j-y_mean)**2)
#    pcc_value = summation(num)/(math.sqrt(summation(den1)*summation(den2)))
#    return round(pcc_value, 6)


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    #    # Skewness Logic
    x_mean = mean(first_list)
    sd = standard_deviation(first_list)
    a = []
    for i in range(len(first_list)):
        if (isinstance(i, (int, float)) == False):
            return 0
        a.append(((first_list[i]-x_mean)/sd) *
                 ((first_list[i]-x_mean)/sd)*((first_list[i]-x_mean)/sd))
    skewness_value = (summation(a)/len(first_list))
    return round(skewness_value, 6)


def sorting(first_list):
    # Sorting Logic
    sorted_list = first_list
    n = len(sorted_list)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]

    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
# def kurtosis(first_list):
    # Kurtosis Logic
#    x_mean = mean(first_list)
#    sd = standard_deviation(first_list)
#    a = []
#    for i in range(len(first_list)):
#        if (isinstance(i, (int, float)) == False):
#            return 0
#        a.append(((first_list[i]-x_mean)/sd)**4)
#    kurtosis_value = (summation(a)/len(first_list))

#    return round(kurtosis_value, 6)


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for i in first_list:
        if isinstance(i, (int, float)) == False:
            return 0
        else:
            summation_value = summation_value + i
    return round(summation_value, 6)
    return summation_value

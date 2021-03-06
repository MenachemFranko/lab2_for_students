from math import sqrt


def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values)/2) # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values)%2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum/(len(list_of_values)-1)


def covariance(first_list_of_values, second_list_of_values):
    """
    receive two lists of nums and calculate the covariance between them
    :param first_list_of_values: first list
    :param second_list_of_values: second list
    :return: the covariance
    """
    result = 0
    for i in range(len(first_list_of_values)):
        delta_x = (first_list_of_values[i] - mean(first_list_of_values))
        delta_y = (second_list_of_values[i] - mean(second_list_of_values))
        result = result + delta_x * delta_y
    result = result / (len(first_list_of_values)-1)

    return result


def correlation(first_list_of_values, second_list_of_values):
    """
    receive two lists and calculate the correlation between them, by using the covariance and variance methods
    :param first_list_of_values: first list
    :param second_list_of_values: second list
    :return: the correlation
    """
    result = 0
    standard_deviation_x = sqrt(variance(first_list_of_values))
    standard_deviation_y = sqrt(variance(second_list_of_values))
    result = covariance(first_list_of_values, second_list_of_values)
    result = result / (standard_deviation_x * standard_deviation_y)
    return result


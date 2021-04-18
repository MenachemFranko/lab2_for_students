from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:3.2f}, Std: {:3.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values) ** 0.5))
    # here you should compute correlations. Be careful, pair should be sorted before printing
    high_correlation = 0.0
    low_correlation = 1.0
    strongest_pair = ("aaa", "bbb")
    weakest_pair = ("aaa", "bbb")
    for outer_index, outer in enumerate(sorted(data.items())):
        for inner_index, inner in enumerate(sorted(data.items())):
            inner_name = inner[0]
            inner_values = inner[1]
            outer_name = outer[0]
            outer_values = outer[1]
            if outer_index <= inner_index:
                continue
            temp = correlation(inner_values, outer_values)
            if abs(temp) > abs(high_correlation):
                strongest_pair = (min(outer_name, inner_name), max(outer_name, inner_name))
                high_correlation = temp
            if abs(temp) < abs(low_correlation):
                weakest_pair = min(outer_name, inner_name), max(outer_name, inner_name)
                low_correlation = temp
    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    run_analysis()

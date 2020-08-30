import pandas

registered_functions = dict()


def alter_data(func):
    """ Decorator to modify data in dataframe. The modified data will then be stored in a new column inside the data frame.
    
    :param func: function which will be decorated
    :type func: callable function
    :return: extended data frame
    :rtype: pandas.DataFrame
    """
    def wrapper(data: pandas.DataFrame, *args, **kwargs) -> dict:
        # get newly calculated data
        new_data = func(data, *args, **kwargs)

        # get number of data points in data frame
        data_length = len(data.index)
        # store new data as new column(s)
        for k, v in new_data.items():
            # if newly created data is not enough pad it with zeros
            if data_length > len(v):
                v.extend([0] * (data_length - len(v)))

            data[k] = v[0:data_length]

        return data

    return wrapper


# @alter_data
# def test_alter_data(data: pandas.DataFrame) -> dict:
#     return {
#         'third' : [1,3,4,5,4,1,1,1,1,1,1,1,1,1,1],
#         'fourth': [1,2,3,4,5]
#     }

# t = {
#     'first' : [1,3,4,5,3,2,2,3],
#     'second' : [5,3,3,5,3,9,2,3]
# }
# a = pandas.DataFrame.from_dict(t)
# print(test_alter_data(a))


def extra_info(func):
    def wrapper(data: pandas.DataFrame, *args, **kwargs):
        result = func(data, *args, **kwargs)

        registered_functions[func.__name__] = func
        return result

    return wrapper


@extra_info
def test(data: pandas.DataFrame):
    some_var = 1
    return some_var


print(registered_functions)
test('hallo')
print(registered_functions)
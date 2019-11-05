import pathlib
import pandas as pd

def read(file_path, pos_file = None) -> pd.DataFrame:
    """ Reads a raw measurement data file and turns it into a pandas.DataFrame.
    
    :param file_path: path to raw data file
    :type file_path: pathlib.Path
    :param pos_file: path to the position data file, defaults to None
    :type pos_file: pathlib.Path, optional
    :return: cleaned data
    :rtype: pd.DataFrame

    .. todo:: Using meta or storing it?

    .. todo:: Fixing the desc => hardcoding?

    .. todo:: Adding doctests to :code:`read()`

    .. note:: :code:`readlines()` not really performant if files get too large.
    """
    # check if file exists
    if not file_path.exists:
        raise FileNotFoundError


    with open(file_path, 'r') as f:
        data = f.readlines()

    # getting rid off meta data
    [data.pop(0) for _ in range(3)]

    # splitting header by : and stripping all spaces
    desc = [_.strip() for _ in data[0].split(':')]
    # splitting header by , and then flatten list again :(
    desc = [item for sublist in [_.split(',') for _ in desc] for item in sublist]
    data.pop(0)

    data = [[float(number) for number in line.split()] for line in data]

    #print(desc)
    #print(data)

    data_dict = dict()

    for k,v in zip(desc, zip(*data)):
        data_dict[k] = v


    return pd.DataFrame(data_dict)


if __name__ == "__main__":
    p = pathlib.Path('../../testfiles/polarimeter/2019_02_20_1325_dc2x_scan.dat')
    o = read(p)
    print(o)
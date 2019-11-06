import pathlib
import pandas as pd
import fire

def read(file_path, pos_file = None) -> pd.DataFrame:
    """ Reads a raw measurement data file and turns it into a pandas.DataFrame.
    
    :param file_path: path to raw data file
    :type file_path: pathlib.Path
    :param pos_file: path to the position data file, defaults to None
    :type pos_file: pathlib.Path, optional
    :return: cleaned data
    :rtype: pd.DataFrame

    .. todo:: Using meta or storing it?

    .. note:: :code:`readlines()` not really performant if files get too large.

    >>> print(read(pathlib.Path('../../testfiles/polarimeter/2019_02_20_1325_dc2x_scan.dat')))
        I Scan (mA)  Detector (cnts)  Monitor Max (cnts/s)  Monitor Min (cnts/s)  Norm (1/s)  Err (1/s)  FlippRatio  ErrFlippRatio
    0       -1500.0           3748.8                   5.0                   0.0   22.858537   1.823577    0.004225       0.000380
    1       -1350.0           2703.8                   4.0                   0.0   16.190419   1.290964    0.005965       0.000537
    2       -1200.0           2048.8                   5.0                   0.0   12.885535   1.060801    0.007494       0.000692
    3       -1050.0           1730.8                   4.0                   0.0   10.489697   0.854661    0.009206       0.000843
    4        -900.0           1871.8                   4.0                   0.0   12.908966   1.112780    0.007481       0.000717
    5        -750.0           2427.8                   4.0                   0.0   16.977622   1.460954    0.005688       0.000544
    6        -600.0           3440.8                   5.0                   0.0   20.727711   1.647133    0.004659       0.000418
    7        -450.0           4528.8                   3.0                   0.0   30.808163   2.581924    0.003135       0.000294
    8        -300.0           5488.8                   4.0                   0.0   34.305000   2.751293    0.002815       0.000255
    9        -150.0           6168.8                   4.0                   0.0   36.287059   2.821178    0.002661       0.000235
    10          0.0           6447.8                   5.0                   0.0   44.776389   3.772802    0.002157       0.000203
    11        150.0           6171.8                   3.0                   0.0   45.049635   3.891333    0.002144       0.000206
    12        300.0           5442.8                   4.0                   0.0   34.667516   2.806390    0.002786       0.000254
    13        450.0           4514.8                   4.0                   0.0   28.042236   2.249098    0.003444       0.000311
    14        600.0           3331.8                   4.0                   0.0   23.969784   2.075067    0.004029       0.000387
    15        750.0           2467.8                   4.0                   0.0   13.710000   1.058495    0.007044       0.000618
    16        900.0           1889.8                   5.0                   0.0   11.182249   0.897811    0.008636       0.000782
    17       1050.0           1694.8                   4.0                   0.0   11.608219   1.001229    0.008319       0.000797
    18       1200.0           2071.8                   4.0                   0.0   16.060465   1.457403    0.006013       0.000601
    19       1350.0           2738.8                   4.0                   0.0   18.018421   1.501495    0.005359       0.000500
    20       1500.0           3835.8                   7.0                   0.0   23.824845   1.916661    0.004053       0.000367
    """
    # check if file exists
    if not file_path.exists:
        raise FileNotFoundError

    with open(file_path, 'r') as f:
        data = f.readlines()

    # getting rid off meta data
    [data.pop(0) for _ in range(3)]

    # splitting header by : and stripping all spaces
    #desc = [_.strip() for _ in data[0].split(':')]
    # splitting header by , and then flatten list again :(
    #desc = [item for sublist in [_.split(',') for _ in desc] for item in sublist]
    data.pop(0)

    # hardcoded variant, because original heading not optimal
    desc = [
        'I Scan (mA)',
        'Detector (cnts)',
        'Monitor Max (cnts/s)',
        'Monitor Min (cnts/s)',
        'Norm (1/s)',
        'Err (1/s)',
        'FlippRatio',
        'ErrFlippRatio'
    ]
    data = [[float(number) for number in line.split()] for line in data]

    data_dict = dict()
    for k,v in zip(desc, zip(*data)):
        data_dict[k] = v

    return pd.DataFrame(data_dict)


if __name__ == "__main__":
    # TODO: remove for production
    import doctest
    doctest.testmod()

    fire.Fire(read)
import pathlib
import pandas as pd


def read(file_path: pathlib.Path) -> pd.DataFrame:
    """ Reads a raw measurement data file and turns it into a pandas.DataFrame.
    
    :param file_path: path to raw data file
    :type file_path: pathlib.Path
    :return: cleaned data
    :rtype: pd.DataFrame

    >>> print(read(pathlib.Path('../../../testfiles/interferometer/IFM_20190314_131927_180_Apert10x10.log')))
        PhaseShifterPosition  Period  O_Counts  H_Counts  O+H  O_AUX_Counts  H_AUX_Counts  O_AUX+H_AUX  Monitor_Counts
    0                   0.60     180        29       136  165            55           385          440             450
    1                   0.75     180        32       103  135            92           305          397             452
    2                   0.90     180        44       111  155           105           311          416             451
    3                   1.05     180        36       109  145           130           262          392             438
    4                   1.20     180        51       105  156           135           266          401             460
    5                   1.35     180        35       107  142           112           271          383             463
    6                   1.50     180        44       124  168            81           332          413             497
    7                   1.65     180        26       145  171            54           350          404             480
    8                   1.80     180        21       126  147            43           368          411             411
    9                   1.95     180        31       128  159            73           368          441             443
    10                  2.10     180        29       119  148           103           338          441             436
    11                  2.25     180        47       114  161            93           289          382             475
    12                  2.40     180        47        91  138           128           263          391             481
    13                  2.55     180        48        93  141           141           219          360             436

    """
    # check if file exists
    if not file_path.exists:
        raise FileNotFoundError

    return pd.read_csv(file_path, sep='\t')


if __name__ == "__main__":
    # TODO: remove doctest for production
    import doctest
    doctest.testmod()

    import fire
    fire.Fire(read)
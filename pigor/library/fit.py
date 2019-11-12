import lmfit
import pandas


def fit(data: pandas.DataFrame, fit_config: dict) -> [lmfit.model.ModelResult]:
    """ Performs a fit using lmfit.
    
    :param data: data to fit
    :type data: pandas.DataFrame
    :param fit_config:  describes what columns are used for 
                        x- and y-axis and how they should be
                        fitted, for example {'column1':'x',
                        'column2':lmfit.models.GaussianModel, 
                        'column3':lmfit.models.LinearModel},
                        where column1 etc. are the actual
                        names (or numbers) of the pandas data
                        frame columns
    :type fit_config: dict
    :return: list of finished fits
    :rtype: [lmfit.model.ModelResult]
    """
    # TODO!
    x = fit_config
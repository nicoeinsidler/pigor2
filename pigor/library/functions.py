import pathlib
import importlib


def is_plugin(path: pathlib.Path) -> bool:
    """ Verifies if path matches all criteria for a plugin:

    1. must be a directory
    2. directory must contain an __init__.py file
    3. must have an adapter.py file
    4 :code:`read(file_path: pathlib.Path) -> pandas.DataFrame` function in adapter.py 
    
    :param path: path to the plugin folder
    :type path: pathlib.Path
    :return: returns :code:`True` if path points to a valid plugin, otherwise :code:`False`
    :rtype: bool

    .. todo:: Check if read function takes a pathlib.Path object as first argument and returns a pandas data frame object.
    """
    # believe path points to module if not otherwise proven wrong
    result = True

    # try to import checking criteria 1) & 2)
    try:
        plugin = importlib.import_module('pigor.plugins.' + path.name)
    except ModuleNotFoundError:
        plugin = None
        result = False

    # see if adapter.py exists, cirterion 3)
    if not path.joinpath('adapter.py').exists():
        result = False

    # check for the existance of read() function
    if plugin and not 'read' in dir(plugin):
        result = False

    return result
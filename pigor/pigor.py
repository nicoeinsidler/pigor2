#!/usr/bin/env python3
import re
import sys
import pathlib
import pandas
import importlib

# add root to pigor for relative imports
PIGOR_ROOT_PATH = pathlib.Path('../').resolve().absolute()
if str(PIGOR_ROOT_PATH) not in sys.path:
    sys.path.insert(0, str(PIGOR_ROOT_PATH))

# regex pattern to identify __pychache__
PYTHON_DIR_PATTERN = re.compile('__[A-Za-z0-9._-]*__')
# path were all plugins are located
PATH_TO_PLUGINS = pathlib.Path('./plugins')

all_plugins = [
    entry for entry in PATH_TO_PLUGINS.glob('*')
    if entry.is_dir() and not re.match(PYTHON_DIR_PATTERN, entry.name)
]


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


class Measurement(object):
    """ Combines all the functionality of PIGOR (or its parts) into a handy
    class. This is especially useful when working with Jupyter.
    
    :raises ModuleNotFoundError: if module (plugin) cannot be found

    .. todo:: List all public methods and instance variables. See https://www.python.org/dev/peps/pep-0257/.
    """
    def __init__(self, file_path: pathlib.Path, plugin: str, **kwargs) -> None:
        """ Initializes the class instance.
        
        :param file_path:             path to the file to read the data from
        :type file_path:              pathlib.Path
        :param plugin:                plugin/module which should be used for the data, e.g.
                                      the experiment in which the data was produced
        :type plugin:                 str
        :raises ModuleNotFoundError:  if plugin could not be found
        :return:                      returns nothing
        :rtype:                       None
        """
        # save file path
        self.file_path = pathlib.Path(file_path)

        # check if plugin is valid plugin
        if not is_plugin(PATH_TO_PLUGINS.joinpath(plugin)):
            raise ModuleNotFoundError(
                f'Either the plugin "{plugin}" does not exist or it is missing something. Please refer to the docs (pigor.org/2) for more help.'
            )

        # import plugin
        self.plugin = importlib.import_module('pigor.plugins.' + plugin)

        # import data into data frame
        self.data = self.plugin.read(self.file_path.absolute(), **kwargs)


if __name__ == "__main__":
    p = pathlib.Path(
        '../testfiles/polarimeter/2018-11-22-1125-degree-of-polarisation.dat')
    plugin = 'polarimeter'
    m = Measurement(p, plugin)
    print(m.data)

    # import fire
    # fire.Fire(Measurement)
import sys
import pathlib

PATH_TO_PLUGINS = pathlib.Path('../..').resolve().absolute()
if str(PATH_TO_PLUGINS) not in sys.path:
    sys.path.insert(0, str(PATH_TO_PLUGINS))


import pigor.plugins


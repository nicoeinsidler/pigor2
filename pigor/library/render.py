import sys
import pathlib

PATH_TO_PLUGINS = pathlib.Path('../plugins').resolve().absolute()
print(PATH_TO_PLUGINS)
if str(PATH_TO_PLUGINS) not in sys.path:
    sys.path.insert(0, str(PATH_TO_PLUGINS))
# sys.path.append(os.path.abspath(os.path.join('..', 'plugins')))
print(sys.path)

from plugins.polarimeter.functions import *

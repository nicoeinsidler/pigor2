import re
import sys
from types import FunctionType
import inspect
import pathlib
import importlib

PATH_TO_PLUGINS = pathlib.Path('../..').resolve().absolute()
if str(PATH_TO_PLUGINS) not in sys.path:
    sys.path.insert(0, str(PATH_TO_PLUGINS))
import pigor.plugins as plugins


[print(module) for module in dir(plugins) if inspect.ismodule(module)]

p = pathlib.Path('../plugins')

if p.is_dir():
    print(p)




test = importlib.import_module('pigor.plugins.polarimeter')
print(dir(test))

def render(template: pathlib.Path, plot_function: FunctionType, extra_info_functions: [FunctionType]):
    pass

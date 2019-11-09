import re
import sys
import inspect
import pathlib

PATH_TO_PLUGINS = pathlib.Path('../..').resolve().absolute()
if str(PATH_TO_PLUGINS) not in sys.path:
    sys.path.insert(0, str(PATH_TO_PLUGINS))
import pigor.plugins as plugins


[print(module) for module in dir(plugins) if inspect.ismodule(module)]

p = pathlib.Path('../plugins')

if p.is_dir():
    print(p)

PYTHON_DIR_PATTERN = re.compile('__[A-Za-z0-9._-]*__')

a = [entry for entry in p.glob('*') if entry.is_dir() and not re.match(PYTHON_DIR_PATTERN, entry.name)]
print(a)
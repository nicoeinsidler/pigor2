#!/usr/bin/env python3
import re
import pathlib

# regex pattern to identify __pychache__
PYTHON_DIR_PATTERN = re.compile('__[A-Za-z0-9._-]*__')
# path were all plugins are located
PATH_TO_PLUGINS = pathlib.Path('./plugins')

all_plugins = [entry for entry in PATH_TO_PLUGINS.glob('*') if entry.is_dir() and not re.match(PYTHON_DIR_PATTERN, entry.name)]


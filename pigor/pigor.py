#!/usr/bin/env python3

import pathlib
import pkgutil

import .plugins

# get all available experiments in plugins
experiments_list = []
for importer, modname, ispkg in pkgutil.iter_modules(plugins.__path__):
    if ispkg:
        experiments_list.append(modname)

print(experiments_list)
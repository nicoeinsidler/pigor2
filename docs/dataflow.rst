Data Flow
=========

This document describes the basic data flow from function to function and file to file within PIGORv2.

.. mermaid::

    graph LR
        adapter
        functions
        fit
        plot
        render
        pigor((pigor))

        adapter -->|data| pigor
        pigor -->|data| plot
        pigor -->|data| functions
        pigor -->|data| fit
        pigor -->|data, fit, paths| render
        functions --> |result| render
        fit -->|"fit (parameters, fit function)"| pigor
        plot -->|"path(s) to image"| pigor
        render -->|path to file| pigor


Plugin management (selecting the plugin) is done only by ``pigor.py``. The selected plugin is indicated by a string, which is the name of the plugin.

Essential Functions
-------------------

In ``functions.py`` from a plugin:

.. code::

    def read(file_path: pathlib.Path) --> pandas.DataFrame:
        # your code here
        pass

.. code::

    def render(template: pathlib.Path, plot_function: FunctionType, extra_info_functions: [FunctionType]):
        pass

.. todo:: Still figuring out the best way of implementation. Maybe inside of ``pigor.py`` a Measurement class that combines all different data?!


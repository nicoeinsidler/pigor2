Structure
=========

The Basic Idea
--------------

The basic idea behind PIGORv2 is illustrated below:

.. mermaid::

    graph TB
        files[various data text files] --> adapter("Adapter")
        adapter --> pddf(("Pandas Data Frame"))
        pddf --> cf("Custom Functions")
        cf -->|if custom function creates new data row| pddf
        pddf --> fit("lmfit")
        pddf --> plot
        cf -->|supplies extra info| export
        subgraph Export
        fit --> plot("matplotlib")
        plot --> export("Jinja2")
        end

The main goal is to write intermediaries to bring the data into a shared :class:`pandas.DataFrame` format. These intermediary files will be called adapters.


PIGOR
-----

PIGOR binds all of this together. It has to manage different tasks and usage scenarios.

Usages
''''''

- CLI

    - CLI with arguments: take the arguments (first one is the file to read) and create the plot image and the export meta file
    - CLI without arguments: starts a minimal interface to batch process files
- Jupyter Lab & Notebook: when PIGOR is loaded as a module it provides the user with some simple code to create a :class:`pandas.DataFrame` object act upon it

.. note:: The CLI interface allows the user to create custom batch scripts.

Tasks
'''''

- returning DataFrame, when input is a path to a raw data file
- loading all extra functions
- exporting an image
- exporting a meta data file via Jinja2
- peforming a fit with lmfit

Plugins
-------

Each experiment will create its own plugin. Plugins will be stored in the `./plugins` folder. A plugin folder contains:

- __init__.py
- adapter.py
- (optional) template.*
- (optional) functions.py

__init__.py
'''''''''''

Whis will make the plugin a Python package. At some point PIGOR will import the plugin (the Python package) and implicitly executed.

For most plugins this file only contains the relative import statements. If your plugin is called 'experiment1' and possesses a ``plugins/experiment1/functions.py`` file, the ``__init__.py`` file will look like this:

.. code::

    from .functions import *
    from .adapter import *

.. note:: The ``__init__.py`` file in the parent plugin directory should not be removed or touched when writing a new plugin for PIGOR as it creates a list of all plugins available to use.

adapter.py
''''''''''

The `adapter.py` file specifies how the raw data should be read, cleaned up and stored into a :class:`pandas.DataFrame`. Arbitrary Python code can be contained within this file, but one function is necessary::

    def read(pathlib.Path) --> pandas.DataFrame:
        # your code here


template.*
''''''''''

Because PIGOR uses Jinja2 as the templating engine, the template can be any file type. Most often it will be HTML.

.. note:: If no template file is specified, the default template.html file in the `./plugins` directory will be used instead.


functions.py
''''''''''''

This file is optional and can contain code that alters the data. There are two options for the output:

- **Altering the datapoints**: The function that you want to apply to the data in the :class:`pandas.DataFrame` alters all data points. These points are then being saved as a new column in the :class:`pandas.DataFrame`. Ultimately these new data points can be plotted.
- **Combined data**: If the data points are to calculate few new measures, like statistical analysis, extreme points and so on, it is supplied as extra information to Jinjer2.

Programmatically speaking these two options manifest in two decorators, registering one function to use in production:

- :code:`@alter_data`: Checks if wrapped function returns an array of data and adds it into new column of the :class:`pandas.DataFrame`. If the number of entries in the given array equals the numbers of rows in the :class:`pandas.DataFrame`, it is written as a new column, if the number is smaller, the data points are doubled in order to be able to write a new column, if the number is greater, all data points exeeding will be cut.
- :code:`@extra_info`: Registers the function, so that it will be run before exporting the meta data with Jinja2.

.. note:: In order to use the decorators, the following module must be imported: :code:`import ..library.decorators`.


Registering a Plugin
--------------------

In order for PIGOR to be able to find (and import) a plugin, an additional entry in the ``plugins/__init__.py`` file has to be created. If the plugin's name is 'experiment1' for example, the line to be added is:

.. code::

    from .experiment1 import *


File System Manifestation
-------------------------

PIGORv2 will have the following file structure:

.. code-block:: bash

    plugins/

        experiment1/
            __init__.py
            adapter.py
            template.html

        experiment2/
            __init__.py
            adapter.py
            functions.py
            template.md

        __init__.py

    library/

        functions.py
        template.html

        fit
        plot
        render
        decorators

    __init__.py
    pigor.py
    config.json


Each experiment will have its own plugin. If any plugin does not provide a template file, the template HTML file in the `plugins` folder will be used instead.

The :code:`functions.py` in :code:`plugins/` is used to provide basic functions for every experiment, which will be loaded *additionally*.

.. todo:: Custom fit functions will be written in functions, but need an extra decorator for registering them.



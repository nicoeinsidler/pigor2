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

For most plugins this file is empty.

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


function.py
'''''''''''

This file is optional and can contain code that alters the 
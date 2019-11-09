Creating a new Plugin
=====================

New plugins can be created using PIGOR itself. This will create the necessary folder structure and write the needed import statements into the files. In particular, these things are taken care of:

- creating a new directory inside of ``plugins/``
- creating an ``__init__.py`` file within the newly created directory

    - adding line: ``from .adapter import *``
    - adding line: ``from .functions import *``

- creating ``adapter.py``, writing:

    .. code::

        def read(file_path: pathlib.Path) --> pandas.DataFrame:
            # your code here
            pass

- creating ``functions.py``, writing: :code:`import ..library.decorators`



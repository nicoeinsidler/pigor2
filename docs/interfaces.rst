Interfaces
==========


CLI 
---

Standard (with Arguments)
'''''''''''''''''''''''''

Usage pattern:

.. code::bash

    python pigor.py measurement-1.txt measurement-2.txt ...


.. note::

    Because PIGORv2 is using :class:`fire.Fire` to expose its classes and functions, the CLI interactive mode can be entered via the flag ``-i``.


Batch Processing (without Arguments)
''''''''''''''''''''''''''''''''''''

.. todo:: Write section on how the batch processing CLI interface should behave and look like.

.. note:: Maybe this can be ditched entirely and be replaced by the ``-i`` flag when using fire.


Jupyter
-------

.. code::

    import pigor

    # loads the measurement into Measurement instance
    m1 = pigor.Measurement('measurement-1.txt')

    # plots inline
    m1.plot()

    # functions in functions.py are exposed by @alter_data and @extra_info
    # where @alter_data alters the data frame and @extra_info returns something
    m1.contrast()

    # This function can be used to find all files. When no argument is given,
    # the arguments are taken from config.json
    files = find_all_files(recursive=True, file_extention='.dat')




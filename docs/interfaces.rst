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




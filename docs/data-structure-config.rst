Data Structure Config File
==========================

The data structure config file (``structure.json``) defines which axes are used as an x- and y-axis. Each plot can have one x-axis, but many y-axis. In each y-axis further configuration used by the fitting and plotting routines may be defined.

Example:

.. code:: json

    {
        "column1": {
            "column3": {
                "fit_model": "lmfit.models.LinearModel"
            },
            "column5": {}
        },
        "1": {
            "column2": {},
            "column5": {},
            "10": {}
        }
    }

.. note:: Columns in the data can either be addressed by using their names or their index number. Mixing of both is allowed.

.. todo:: Specifying what extra info can be added to a y-axis for fitting and plotting.

.. todo:: Deciding how fitting and plotting extra info should be handled: Either using two dicts ("plot" and "fit") inside a y-axis or using the convention "plot\_" or "fit\_".


Structure
---------

.. code:: json

    {
        COLUMN: {
            COLUMN: {
                FEATURE : SETTING
            }
        }
    }

At first all columns are listed that are 


Valid Entries
-------------

- ``COLUMN``: Should be of type ``str`` containing, either the index number of the column or the unambiguous name of the column.
- ``FEATURE``: Here is a list of all available features. Additional features can be registered via the ``@alter_data`` 

    - 




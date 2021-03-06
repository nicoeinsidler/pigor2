functions.py
============

Altering Data
-------------

.. note:: When using the :code:`@alter_data` decorator.

A function that alters the whole data frame or just a column, should probably receive the :code:`@alter_data` decorator. Most common example for when to use this would be if data from one column is ran through some function. These new data points are then being stored in a new column inside the dataframe.

There are the following rules that functions decorated by :code:`@alter_data` should have implemented. 

- **argument data:** the function's first argument must be :code:`data: pandas.DataFrame`
- **return value:** the function must return a dictionary containing one or multiple entries.

.. note:: If the dimensions of the new data points (return value of function) and the existing data frames do not match, either zeros are inserted or data will be cut off and lost.


Creating additional Info
------------------------

.. note:: When using the :code:`@extra_info` decorator.


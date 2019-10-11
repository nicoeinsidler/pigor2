Structure
=========

The basic idea behind PIGORv2 is illustrated below:

.. mermaid::

    graph LR
        files[various data text files] --> adapter("Adapter")
        adapter --> pddf(("Pandas Data Frame"))
        extra("Extra Code") --> pddf
        pddf --> pconf("Plot Config")
        pddf --> econf("Export Config")
        pconf --> plot["Plot"]
        econf --> html
        plot --> html["HTML and/or MD file"]

The main goal is to write intermediaries to bring the data into a shared :class:`pandas.DataFrame` format. These intermediary files will be called adapters.

After creating a :class:`pandas.DataFrame` two configuration files (one for the plot image and one for the HTML or MD file) are necessary to create. These configuration files will be separated into two main parts, first a simple text file and second python code to be able to define functions and perform custom calculations on the data before plotting and exporting.

It will be useful to bundle all those files into plugin modules. Each experiment can then have its own plugin.

.. autoclasstree:: sphinx.util sphinx
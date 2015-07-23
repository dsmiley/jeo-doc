.. _csv:

Comma Separated Value
=====================

The `Comma Separated Value <https://en.wikipedia.org/wiki/Comma-separated_values>`_ (CSV) format is
a commonly used format for storing spatial data, especially points.

.. code-block:: java

       // csv file options
       CSVOpts opts = new CSVOpts()
        .delimiter(',')
        .header(true)
        .xy("lat", "lon");

       VectorDataset points = CSV.open(Paths.get('points.csv'), opts);

Connection Options
------------------

The following connection options are supported by the CSV driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to CSV file.
      -  Yes
      -
      -
   *  -  delim
      -  Column delimiter.
      -  No
      -  `,` (comma)
      -
   *  -  header
      -  Whether the CSV file has a header row or not.
      -  No
      -  true
      -
   *  -  x
      -  Name or index of column representing x values.
      -  No
      -
      -
   *  -  y
      -  Name or index of column representing y values.
      -  No
      -
      -

Driver Aliases
--------------

The CSV driver is identified by the name ``csv``.

Driver Capabilities
-------------------

The CSV driver does not support any native capabilities.
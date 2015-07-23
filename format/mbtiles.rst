.. _mbtiles:

MBTiles
=======

`MBTiles <https://github.com/mapbox/mbtiles-spec>`_ is a specification for storing tiled map data in 
SQLite databases. It is developed and maintained by MapBox.

.. code-block:: java

    TileDataset tiles = MBTiles.open(Paths.get('ne.mbtiles'));

Connection Options
------------------

The following connection options are supported by the MBTiles driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to MBTiles database.
      -  Yes
      -
      -

Driver Aliases
--------------

The MBTiles driver is identified by the name ``mbtiles`` but can also be referenced as:

* ``mbt``
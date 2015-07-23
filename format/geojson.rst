.. _geojson:

GeoJSON
=======

`GeoJSON <GeoJSON is a format for encoding a variety of geographic data structures.>`_ is a format 
for encoding a variety of geographic data structures.

.. code-block:: java

       VectorDataset points = GeoJSON.open(Paths.get('points.json'));

Connection Options
------------------

The following connection options are supported by the GeoJSON driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to GeoJSON file.
      -  Yes
      -
      -

Driver Aliases
--------------

The CSV driver is identified by the name ``geojson`` but can also be referenced as:

* ``json``

Driver Capabilities
-------------------

The GeoJSON driver does not support any native capabilities.
.. _shapefile:

Shapefile
=========

`ESRI Shapefile <https://en.wikipedia.org/wiki/Shapefile>`_ is the most widely used format for 
storing and exchanging geospatial vector data. This driver is implemented the 
`OGR Shapefile driver <http://www.gdal.org/drv_shapefile.html>`_ via the GDAL/OGR Java bindings.

.. code-block:: java

       VectorDataset states = Shapefile.open(Paths.get("states.shp"));

Connection Options
------------------

The following connection options are supported by the Shapefile driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to Shapefile.
      -  Yes
      -
      -

Driver Aliases
--------------

The Shapefile driver is identified by the name ``shapefile`` but can also be referenced as:

* ``shp``

Driver Capabilities
-------------------

The following table summarizes the native capabilities of the Shapefile driver.

.. list-table::
   :header-rows: 1

   *  -  Capability
      -  Supported
      -  Notes
   *  -  Dataset Creation
      -  No
      -
   *  -  Write Support
      -  No
      -
   *  -  Bounds Filtering
      -  Yes
      -
   *  -  Property Filtering
      -  No
      -
   *  -  Limit
      -  No
      -
   *  -  Offset
      -  No
      -
   *  -  Field Selection
      -  No
      -
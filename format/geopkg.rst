.. _geopkg:

GeoPackage
==========

GeoPackage is an open, standards-based, platform-independent, portable, self-describing, compact 
format for transferring geospatial information.

.. code-block:: java

       // connect
       Workspace db = GeoPackage.open(Paths.get("gis.gpkg"));

       // list datasets (tables)
       for (Handle<Dataset> dataset : db.list()) {
         System.out.println(dataset.name());
       }

       // load a dataset
       VectorDataset roads = db.get("roads");
       TileDataset tiles = db.get("tiles");

Connection Options
------------------

The following connection options are supported by the GeoPackage driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to GeoPackage file.
      -  Yes
      -
      -

Driver Aliases
--------------

The GeoPackage driver is identified by the name ``geopackage`` but can also be referenced as:

* ``geopkg``
* ``gpkg``

Driver Capabilities
-------------------

The following table summarizes the native capabilities of the GeoPackage driver.

.. list-table::
   :header-rows: 1

   *  -  Capability
      -  Supported
      -  Notes
   *  -  Dataset Creation
      -  Yes
      -
   *  -  Write Support
      -  Yes
      -
   *  -  Bounds Filtering
      -  Yes
      -
   *  -  Property Filtering
      -  Partial
      -  Spatial filters, Mixed and Self expressions not handled
   *  -  Limit
      -  Yes
      -
   *  -  Offset
      -  Yes
      -
   *  -  Field Selection
      -  Yes
      -
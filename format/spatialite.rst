.. _spatialite:

SpatiaLite
==========

`SpatiaLite <http://www.gaia-gis.it/gaia-sins/>`_ is a spatial extension to SQLite, providing vector 
geodatabase functionality.

.. code-block:: java

       // connect
       Workspace db = SpatiaLite.open(Paths.get("gis.db"));

       // list datasets (tables)
       for (Handle<Dataset> dataset : db.list()) {
         System.out.println(dataset.name());
       }

       // load a dataset
       VectorDataset roads = db.get("roads");

Connection Options
------------------

The following connection options are supported by the SpatiaLite driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to SpatiaLite database file.
      -  Yes
      -
      -

Driver Aliases
--------------

The SpatiaLite driver is identified by the name ``spatialite``.

Driver Capabilities
-------------------

The following table summarizes the native capabilities of the SpatiaLite driver.

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
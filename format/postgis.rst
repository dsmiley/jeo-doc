.. _postgis:

PostGIS
=======

PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support 
for geographic objects allowing location queries to be run in SQL.

.. code-block:: java

       // create connection options
       PostGISOpts opts = new PostGISOpts("gis")
         .host("localhost")
         .port(5432)
         .schema("public")
         .user("bob")
         .passwd("...");

       // connect
       Workspace db = PostGIS.open(opts);

       // list datasets (tables)
       for (Handle<Dataset> dataset : db.list()) {
         System.out.println(dataset.name());
       }

       // load a dataset
       VectorDataset roads = db.get("roads");


Connection Options
------------------

The following connection options are supported by the PostGIS driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  db
      -  Name of the database to connect to
      -  Yes
      -
      -
   *  -  host
      -  Hostname or IP address of the database server
      -  No
      -  localhost
      -
   *  -  port
      -  Port number database server is listening on
      -  No
      -  5432
      -
   *  -  schema
      -  Name of database schema to load tables from
      -  No
      -
      - :ref:`schemas <schemas>`
   *  -  user
      -  Name of user to connect as
      -  No
      -  ``user.name`` system property
      -
   *  -  passwd
      -  Password of user connecting
      -  No
      -
      -

Driver Aliases
--------------

The PostGIS driver is identified by the name ``postgis`` but can also be referenced as:

* ``pg``
* ``pgsql``

.. _schemas:

Database Schemas
----------------

The PostGIS driver accepts an optional "schema" connection option. When a value is specified only 
tables from that schema will be available. When no value is specified all tables in all schemas are 
made available. In this mode dataset names may contain a reference to the schema. For example.

.. code-block:: java

     db.get("osm.roads");

Driver Capabilities
-------------------

The following table summarizes the native capabilities of the PostGIS driver.

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
      -  Most
      -  Mixed and Self expressions not handled
   *  -  Limit
      -  Yes
      -
   *  -  Offset
      -  Yes
      -
   *  -  Field Selection
      -  Yes
      -

.. _overview_data:

Working with Data
=================

In jeo the :jeoref:`data.Driver` interface is the abstraction for a spatial data format. A driver
is responsible for reading (and optionally writing) data in a  specific format. This list of 
supported drivers can be found in the :ref:`formats` section.

.. todo:: Create list of all supported formats.

For instance to read GeoJSON data the :jeoref:`geojson.GeoJSON` driver is used. The following
example reads a file named :file:`points.json`. 

.. code-block:: java

   GeoJSON.open(new File("points.json"));

The type of object returned from `open` depends on the driver. In the above example an instance of 
the :jeoref:`VectorDataset` interface is returned. This class is the abstraction for vector datasets 
and  provides a number of data access methods.

.. code-block:: java

  // read the data
  VectorDataset data = GeoJSON.open(Paths.get("points.json"));

  // get the spatial bounds
  Bounds bbox = data.bounds();

  // count the number of features
  data.count(new VectorQuery());

  // iterate over the features
  for (Feature f : data.read(new VectorQuery())) {
    System.out.println(f);
  }

  // dispose
  data.close();

The above code snippet introduces two new classes. The :jeoref:`vector.VectorQuery` class is used to 
query a vector data set and controls what data is returned from the query. The 
:jeoref:`vector.Feature` class represents an object in a vector data set. Both of these concepts are 
covered in greater detail in the :ref:`overview_data_vector` section.

.. todo:: vector data section

In the previous GeoJSON example the driver was used to open a specific data set. Other types of 
formats are containers for multiple datasets. An example is a PostGIS database.

.. code-block:: java

   // specify connection options
   PostGISOpts opts = new PostGISOpts("usa")
    .host("localhost")
    .port(5432)
    .user("bob");

   // open
   Workspace db = PostGIS.open(opts);


In this example the result of `open` returns an instance of the :jeoref:`data.Workspace` class. A 
workspace is a container for data sets. 

.. code-block:: java

   // iterate over layers in the workspace
   for (Handle<Dataset> ds : db.list()) {
      System.out.println(ds);
   }

   // get a specific dataset
   Dataset data = db.get("states");

   // dispose the workspace
   db.close();

.. note::

   All data objects such as workspaces and datasets should be disposed after use. These objects 
   extend from `java.io.Closeable` and are usable within a Java 7 "try-with" block.

.. _overview_data_vector:

Vector Data
-----------

In the previous section the :jeoref:`vector.VectorDataset` interface was introduced. This  interface 
is the primary abstraction used for access to a vector data set.

Features
^^^^^^^^

A vector dataset is a collection of :jeoref:`vector.Feature` objects. A feature is essently a map of 
named  attributes, any of which can be a geometry object.

.. code-block:: java

   // grab a feature
   Feature f = ...;

   // get some attributes
   f.get("name");
   f.get("location")

   // set some attributes
   f.set("name", "foo")
   f.set("location", Geom.point(0,0));

Typically a feature object has a single geometry object. It is not uncommon for a feature to contain 
multiple geometry objects, but in this case one is designated the default. The 
:jeoref:`vector.Feature#geometry` method is used to obtain the default geometry of a feature. It is 
also perfectly valid for a feature to have no geometry attribute, in which case the 
`Feature.geometry()` returns null.

.. code-block:: java

   // grab a feature
   Feature f = ...;

   // get the default geometry
   Geometry g = f.geometry();

   // set the default geometry
   f.put(Geom.point(0,0));

.. note::

   Typically the default geometry of a feature is the first one encountered when iterating through 
   the feature attributes, whatever order they may be in.

A feature :jeoref:`vector.Schema` is used to describe the structure and attributes of a feature 
object. A schema is a collection of :jeoref:`vector.Field` objects, each field containing a name, 
a type, and an optional coordinate reference system.

.. code-block:: java

   // grab a dataset
   VectorDataset data = ...;

   // gets its schema
   Schema schema = data.schema();

   // iterate over all fields
   for (Field fld : schema) {
     System.out.println(fld.name());
     System.out.println(fld.type());
     Systme.out.println(fld.crs());
   }

.. todo:: feature crs

Queries
^^^^^^^

The :jeoref:`vector.VectorQuery` class is used to obtain features from a  vector dataset. A query 
contains a number of properties that control what features are returned in a result set. This 
includes:

* bounding box - Spatial extent from which to return features
* attribute filter - Attribute predicate for which returned features must match
* limit - Maximum number of features to return
* offset - Offset into result set from which to start returning features

Additionally a query can specify options that transform returned features such as:

* re-projection - Reproject geometries to a specified crs
* simplification - Simplify geometries with a specified tolerance

As an example:

.. code-block:: java

   // grab all features
   VectorQuery q = new VectorQuery();

   // grab all features in a specific area
   VectorQuery q = new VectorQuery().bounds(new Bounds(...));

   // grab all features with some specific attributes
   VectorQuery q = new VectorQuery().filter("SAMP_POP > 2000000");

   // paged result set
   VectorQuery q = new VectorQuery().offset(100).limit(10);

   // reproject
   VectorQuery q = new VectorQuery().reproject("epsg:900913");

   // chain them all together
   VectorQuery q = new VectorQuery()
      .bounds(new Bounds(...))
      .filter("SAMP_POP > 2000000")
      .offset(100)
      .limit(10)
      .reproject("epsg:900913");

.. todo:: sorting

The static method :jeoref:`VectorQuery#all()` can be used as shorthand for a query with no 
constraints.

.. code-block:: java

   import static io.jeo.vector.VectorQuery.all;

   // read everything
   VectorDataset data = ...;

   data.read(all());

Cursors
^^^^^^^

The :jeoref:`vector.FeatureCursor` class is used to return a result set  of feature objects from a 
query. A cursor is for the most part an iterator in the normal java sense.

.. todo:: should rewrite this once cursor vs stream is sorted out

.. code-block:: java

   // get a dataset
   VectorData dataset = ...;

   // query it
   FeatureCursor c = dataset.read(new VectorQuery());

   // iterate
   while (c.hasNext()) {
     Feature f = c.next();
     System.out.println(f);
   }

   // close the cursor
   c.close();

A cursor implements `java.util.Iterable` and so the java for each provides a shorthand for iterating t
hrough a cursor.

.. code-block:: java

   for (Feature f : dataset.read(new VectorQuery())) {
     System.out.println(f);
   }

Cursors also provide stream like methods suitable for usage with Java 8 lambda syntax.  

.. code-block:: java

   dataset.read(new VectoryQuery()).each((f) -> System.out.println(f));

.. warning::

   It is important that a cursors `Cursor.close` method be called when it is
   no longer needed. When a cursor is used with a for-each as above the close 
   method will be called automatically upon loop completion. However if an
   exception or some other control flow event occurs causing the loop to 
   terminate prematurely it is up to the application to ensure close is 
   called. 

Cursors can also be used to write to a vector dataset. The subclass :jeoref:`vector.FeatureWriteCursor`
provides two additional methods:

* :jeoref:`vector.FeatureWriteCursor#write()` for updating/appending features
* :jeoref:`vector.FeatureWriteCursor#remove()` for removing features.

.. code-block:: java

   // update every attribute value to a specific value
   FeatureWriteCursor c = dataset.update(new VectorQuery().filter("name = 'bar'"));
   while (c.hasNext()) {
     Feature f = c.next();
     f.set("name", "foo");
     c.write();
   }

   // remove a feature
   FeatureWriteCursor c = dataset.update(new VectorQuery());
   c.next();
   c.remove();

   // add a new feature to the dataset
   FeatureWriteCursor c = dataset.append(new VectorQuery()));
   Feature f = c.next();
   f.set("name", "bar");
   c.write();


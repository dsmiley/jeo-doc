.. _overview_geom:

Geometries
==========

jeo utilizes the `JTS <http://tsusiatsoftware.net/jts/main.html>`_ library for geometry support. 

The :jeoref:`geom.Geom` class adds additional convenience methods for working with geometry 
objects such as methods for quickly building commonly used geometry types.

.. code-block:: java

    Point point = Geom.point(30,10);

    LineString line = Geom.lineString(30,10, 10,30, 40,40);

    Polygon poly = Geom.polygon(30,10, 40,40, 20,40, 10,20, 30,10);  


The :jeoref:`geom.GeomBuilder` class provides a convenient builder for composing more complex 
geometry types.

.. code-block:: java

   MultiPolygon multiPoly = Geom.build()
     .points(40,40, 20,45, 45,30, 40,40).ring()
     .points(20,35, 10,30, 10,10, 30,5, 45,20, 20,35)
        .polygon()
     .points(30,20, 20,15, 20,25, 30,20)
        .polygon()
     .toMultiPolygon();

.. The `build()` method 

.. {% highlight java %}
.. // build a polygon with a hole
.. Geom.build().points(0,0,10,0,10,10,0,10,0,0).ring()
..    .points(4,4,6,4,6,6,4,6,4,4).ring().toPolygon();
.. {% endhighlight %}

.. {% include api.html class="Geom" package="org.jeo.geom"  description="Geometry utility class" %}

.. The `Geom.iterate` method makes it easy to iterate over geometry collections.

.. {% highlight java %}
.. MultiPoint mp = Geom.build().points(0,0, 1,1, 2,2, 3,3).toMultiPoint();
.. for (Point p : Geom.iterate(mp)) {
..   // do something with p
.. }
.. {% endhighlight %}

.. _geobuf:

Geobuf
======

`Geobuf <https://github.com/mapbox/geobuf>`_ is a compact binary encoding for geographic data based 
on `Google Protocol Buffers <https://developers.google.com/protocol-buffers/>`_. It is developed and
maintained by Mapbox.

.. code-block:: java

       VectorDataset points = Gbf.open(Paths.get('points.pbf'));

Connection Options
------------------

The following connection options are supported by the Geobuf driver.

.. list-table::
   :header-rows: 1

   *  -  Key
      -  Description
      -  Required
      -  Default
      -  Notes
   *  -  file
      -  Path to Geobuf file.
      -  Yes
      -
      -

Driver Aliases
--------------

The Geobuf driver is identified by the name ``geobuf`` but can also be referenced as:

* ``gbf``
* ``pbf``

Driver Capabilities
-------------------

The Geobuf driver does not support any native capabilities.
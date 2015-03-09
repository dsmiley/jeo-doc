.. _cli_usage:

Using the CLI
=============

The CLI comes as a single command with a number of sub-commands. Running the :command:`jeo` 
command displays the synopsis. 

.. code-block:: bash

   $ jeo

   usage: jeo <command> [<args>]

    Commands:

        drivers      List available format drivers
        info         Get information about a data source
        query        Run a query against a data set
        transform    Transforms a result set

    For detailed help on a specific command use jeo <command> -h

Commands
--------

This section describes available commands.

- :ref:`drivers`
- :ref:`info`
- :ref:`query`
- :ref:`transform`

.. _cli_drivers:

drivers
^^^^^^^

The :command:`drivers` command displays information about all available drivers.

When run with no arguments the command lists all available drivers.

.. code-block:: bash

   $ jeo drivers
   [{
      "name": "GeoJSON",
      "enabled": "true"
    },{
      "name": "PostGIS",
      "enabled": "true"
    },{
      "name": "MongoDB",
      "enabled": "true"
    },{
      "name": "GeoPackage",
      "enabled": "true"
    },,{
      "name": "GeoTIFF",
      "enabled": "true"
    }, ...
   ]

The command takes a single argument, the name of a driver, and displays more detailed information
about that specific driver, such as the connection parameters for the driver, and any aliases for 
it.

.. code-block:: bash

   $ jeo drivers postgis
   {
     "name": "PostGIS",
     "enabled": "true",
     "aliases": [
       "pg"
     ],
     "type": "workspace",
     "keys": {
       "db": {
         "type": "String"
       },
       "schema": {
         "type": "String"
       },
       "host": {
         "type": "String",
         "default": "localhost"
       },
       "port": {
         "type": "Integer",
         "default": 5432
       },
       "user": {
         "type": "String",
         "default": "jdeolive"
       },
       "passwd": {
         "type": "Password"
       }
     }
   }

.. _info:

info
^^^^

The :command:`info` command provides summary information about a data source. 

The command takes a single argument in the form of a URI specifying the data source to summarize.
When run with a workspace URI the command lists the contents of the workspace.

.. code-block:: bash

   $ jeo info pg://usa
   {
     "type": "workspace",
     "driver": "PostGIS",
     "datasets": [
       "cities",
       "counties",
       "states"
     ]
   }

When run with a data set URI the command summarizes the contents of the dataset.

.. code-block:: bash

   $ jeo info pg://usa#states
   {
      "name": "states",
      "type": "vector",
      "driver": "PostGIS",
      "bbox": [
        -124.731422,
        24.955967,
        -66.969849,
        49.371735
      ],
      "crs": [
        "+proj=longlat",
        "+datum=WGS84",
        "+no_defs"
      ],
      "count": 49,
      "schema": {
        "geometry": "MultiPolygon",
        "STATE_NAME": "String",
        "STATE_FIPS": "String",
        "SUB_REGION": "String",
        ...
      }
   }

See :ref:`data_uri` for more details of the data source URI syntax.

.. _query:

query
^^^^^

The :command:`query` command runs a query against a vector data set.

The command takes a number of arguments that specify query constraints, as well as input / output:

.. code-block:: bash

   $ jeo query -h

   Usage: jeo query [options]
   Options:
    -i, --input
       Input data set
    -o, --output
       Output for results
       Default: geojson
    -b, --bbox
       Bounding box (xmin,ymin,xmax,ymax)
    -f, --filter
       Predicate used to constrain results
    -l, --limit
       Maximum number of results to return
    -p, --props
       Feature properties to include, comma separated
    -s, --skip
       Number of results to skip over
    -c, --crs
       Projection of input


- ``-i`` specifies the input data set to query as a data source URI. When not specified the query
  command will read data from stdin. See :ref:`cli_pipes` for more details.

- ``-o`` specifies the output format with with to encode query results. The output can be given as 
  one of the following:

  * The value "geojson" or "json" specifying the query should be output as GeoJSON. This is the 
    default.
  * The value "pbf" specifying the query should output as a protocol buffer stream. This value is 
    when piping the output of a query to another command. See :ref:`cli_pipes` for more details.
  * A data source URI specifying a data set to write results to

- ``-c`` overrides or sets the projection of the query input. This option is used when the query 
  input does not have a recognizable projection.

- ``-b`` supplies a bounding box constraint to the query. The bounding box is specified as a comma
  separated list of ``x1``, ``y1``, ``x2``, ``y2``

- ``-f`` supplies a feature property constraint to the query. The constraint is specified as 
  :ref:`CQL <>`

- ``-p`` specifies the names of feature properties to include in query results. Properties are 
  specified as a comma separated list of names.

- ``-l`` specifies the maximum number of features to return from the query. It is the logical 
  equivalent of the "LIMIT" clause of an SQL query.

- ``-s`` Number of features to skip before returning results from the query. It is the logical 
  equivalent of the "OFFSET" clause of an SQL query.

.. todo:: document cql syntax
.. todo:: document crs syntax

Some examples of the query command can be found :ref:`here <cli_examples>`.

.. _transform:

transform
^^^^^^^^^

The :command:`transform` command runs a transform on a vector data set.

.. code-block:: bash

   $ jeo transform -h

   Usage: jeo transform [options]
   Options:
     -i, --input
        Input data set
     -o, --output
        Output for results
        Default: geojson
     -s, --script
        Transform script

- ``-i`` and ``-o`` specifies the input and output of the transform using the same syntax as the 
  :command:`query` command.
- ``s`` specifies the transform as a Javascript function in a script file.

For example:

.. code-block:: bash

   $ jeo transform -i points.shp -s buffer.js

The script file contains a Javascript function named ``transform`` that accepts a feature cursor
as an argument. The function must return a feature cursor. For example:

.. code-block:: javascript

   function transform(cursor) {
      return cursor.map(function(f) {
        return f.put(f.geometry().buffer(1));
      });
   }

.. _cli_data_uri:

Data Source URIs
----------------

Most CLI commands take a data source as input. The data source is specified with a URI of the 
general form::

    [<driver>://][<primary-option>][?<secondary-options>]*][#<dataset>]

Where:

- ``driver`` is the name or alias of the data source driver, specified as the "scheme" of the URI
- ``primary-option`` is the "main" connection option of the driver, specified as the "path" of the URI
- ``secondary-options`` is a set of key value pairs of secondary connection options, specified as 
  as the "query string" of the URI
- ``dataset`` is the name of a dataset within a workspace, specified as the "fragment" of the URI

The following is an example of a PostGIS data source URI::

    postgis://usa?host=localhost&port=5432&user=bob#states

Where:

- "postgis" is the driver name
- "usa" is the primary connection option, in this case the name of the database to connect to
- "host", "port", and "user" are secondary connection options
- "states" is the name of a table / data set of the workspace

For file based data the URI can be specified simply as a regular file path. For example::

   /data/states.json

The file name extension is used to identify the driver and must match the name of the driver or one
of its aliases.

.. _cli_pipes:

Pipes
-----

Modeled after the Unix philosophy, the jeo CLI is capable of piping the output of one command to 
the input of another command. Piping requires the "source" command to output using the protocol 
buffer (pbf) format. For example:

.. code-block:: bash

   $ jeo query -i states.shp -f "POPULATION > 1E6" -o pbf | jeo transform -s buffer.js

In the command above commands the source `query` command specifies the "pbf" output option. The 
destination `transform` command does not specify input causing it to read the protocol buffer stream
from stdin.

Debugging
---------

All driver commands accept the ``-x`` option which enables debug mode. In debug mode the command 
outputs verbose information such as debug logs. It also enables full stack trace of any errors that
occur while executing the command.

.. _cli_examples:

Examples
--------

List all supported drivers.

.. code-block:: bash

   $ jeo drivers


Info about a PostGIS workspace with all of the defaults.

.. code-block:: bash

   $ jeo info pg://usa


Info about PostGIS workspace with explicit options.

.. code-block:: bash

   $ jeo info pg://usa?user=bob&host=localhost&port=5432


Info about a specific data set in a PostGIS workspace

.. code-block:: bash

   $ jeo info pg://usa#states


Query by spatial extent.

.. code-block:: bash

   $ jeo query -b -124.731422,24.955967,-66.969849,49.371735 pg://usa#states


Query by property filter.

.. code-block:: bash

   $ jeo query -f "STATE_NAME = 'New York'" pg://usa#states.json


Convert a PostGIS table to GeoJSON

.. code-block:: bash

   $ jeo query -i pg://usa#states -o states.json

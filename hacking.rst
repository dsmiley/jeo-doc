.. _hacking:

Hackers Guide
=============

Guide to contributing to the jeo library.

Infrastructure
--------------

The jeo project uses `GitHub <http://github.com/jeo>`_ for source control, issue tracking, and wiki 
space.

A google group exists for general discussion.

`TravisCI <https://travis-ci.org/jeo/jeo>`_ is used continuous integration.

The `Boundless maven repository <http://repo.boundlessgeo.com/main>`_  is used for hosting build 
artifacts.

.. todo:: Link to google group.

Contributing
------------

Like most open projects jeo welcomes contributions from developers using the  library. The best way 
to submit a contribution is through a GitHub pull request.

Below are some general guidelines for contributors to ensure a successful  contribution to the 
library. If not familiar with how the open source development process works a great read is 
`this guide <http://people.redhat.com/~rjones/how-to-supply-code-to-open-source-projects/>`_ to 
contributions. 

Clean Patches
^^^^^^^^^^^^^

When submitting a patch it is important to make the patch easy to understand for the reviewer. Some 
things to avoid are:

- introducing code formatting changes that aren't relevant to the change
- using tabs instead of spaces for indentation

Copyright
^^^^^^^^^

Code contributed to the project must be owned by the project meaning contributors must be willing to 
give up copyright. At this time there is no official contributor agreement but any non-trivial 
contribution will require verbal agreement from the contributor. 

All new files require the following copyright header.

.. code-block:: java

   /* Copyright 2015 The jeo project. All rights reserved.
    *
    * Licensed under the Apache License, Version 2.0 (the "License");
    * you may not use this file except in compliance with the License.
    * You may obtain a copy of the License at
    *
    *      http://www.apache.org/licenses/LICENSE-2.0
    *
    * Unless required by applicable law or agreed to in writing, software
    * distributed under the License is distributed on an "AS IS" BASIS,
    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    * See the License for the specific language governing permissions and
    * limitations under the License.
    */

Module Structure
----------------

The jeo library is broken up into a number of modules, the primary module being the `core` module. 
The core module is intended to be the home for very fundamental and commonly used features of the 
library. Outside of the core module are modules for specific purposes. 

Modules implementing support for spatial formats are grouped under the `format` directory. 

The `util` directory is the place for "utility modules". These are modules that are used to 
implement other non-core modules. They are generally not a module that end-user would interact with 
directly. 

Aside from that are modules for specific purposes such as the `cli` and `nano` modules.

When contributing to the library the first thing is to determine what module the
code should reside in. The following are some general guidelines to use to make
that decision. 

* If the code provides a very common and core function, it should go in core
* If the code adds a new third party dependency then it must go in a new module
* If the code adds support for a new format then it must go in a new module 
  under the `format` directory

But if all else fails or it is still unclear just `ask <mailto:jeo-dev@googlegroups.com>`_ first.

Contrib Modules
---------------

For the most part the core of jeo contains stable modules. The 
`contrib <http://github.com/jeo/jeo-contrib>`_ repository is a place for experimental or 
incomplete modules.

Coding Guidelines
-----------------

Formatting
^^^^^^^^^^

The project doesn't have very strict code formatting guidelines. The only real rule is to 
ensure that indentation is set to use *spaces* for tabs rather than the tab character. The 
recommended tab width is 4 spaces.

The following are additional recommendations:

* Ensure the IDE is not configured to auto-group individual imports into wildcard imports as this
  leads to formatting cruft in patches

Logging
^^^^^^^

jeo uses the `SLF4J <http://www.slf4j.org/>`_ for all logging. Use it as opposed to using built-in 
java logging. 

In general don't log anything above the DEBUG level. This may sound counter intuitive but overusing 
higher levels can lead to logs that are hard to read as well as crowd output of the CLI. In general 
let the end application control whether debug logs are shown or not.

Dependencies
^^^^^^^^^^^^

jeo is very careful about how it manages third party dependencies. The core module depends only on 
JTS, Proj4J, and SLF4J. There are no exceptions to this rule. Code that requires a third party 
library (such as a jdbc driver) must go in a separate module.

This includes utility libraries like guava and commons. While it is very tempting to utilize these 
libraries in the core we avoid doing so. Any library dependency makes the library less portable and 
increases the overall footprint. By taking such a strict stance when it comes to third party 
dependencies we ensure that jeo remains lightweight and portable between Java virtual machine
implementations. This is especially important for being supported on Android.

That said the core module may utilize utility libraries for writing tests. 
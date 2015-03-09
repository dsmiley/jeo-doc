.. cli_install:

Installing the CLI
==================

Requirements
------------

Java
^^^^

The only hard requirement for running the CLI is a Java 8+ virtual machine. It is recommended that 
an Oracle or OpenJDK virtual machines be used.

Because installing Java often varies even on a single platform native packages don't declare a 
dependency on native Java packages even when they are available for a specific platform. 

Once Java 8 is installed on the system either one of two things must hold true:

#. The :command:`java` command must be on the `PATH`
#. The `JAVA_HOME` environment variable is set

If running the :command:`jeo` command results in an error message that looks like the following then 
it means another Java version is being picked up::

   Exception in thread "main" java.lang.UnsupportedClassVersionError: org/jeo/cli/JeoCLI : Unsupported major.minor version 52.0

GDAL
^^^^

In order to enable many formats the GDAL libraries must be installed on the system. Version 1.11+ is
recommended although older versions are known to work as well.

Like Java, GDAL installations often vary as well. Due to the wide variety of optional formats GDAL
is often manually compiled on a system. For these reasons native packages don't declare a dependency
on GDAL even when a package is available.

In order for jeo to pick up the GDAL libraries on the system one of two conditions must be met:

#. The libraries are located on a well known library path (for example :file:`/usr/lib`)
#. The `LD_LIBRARY_PATH` (`DYLD_LIBRARY_PATH` on osx) points to the libraries

.. todo:: Update for Windows

Installation
------------

Packages are available for a number of platforms.

Mac OSX
^^^^^^^

Mac OSX users can install with `Homebrew <http://brew.sh>`_ via the jeo tap.

.. code-block:: bash

   $ brew tap jeo/jeo
   $ brew install jeo

.. note::

   The `Cask <http://caskroom.io>`_ project provides an easy way to install Java 8.

   .. code-block:: bash

      $ brew cask install java

.. note::

   If GDAL is not already installed on the system then installing it also via Homebrew is the 
   easiest way to get it.

   .. code-block:: bash

      $ brew install gdal

Ubuntu
^^^^^^

Debian packages are provided for 64-bit Ubuntu systems. Versions 12.04 (Precise) and 14.04 (Trusty)
are the officially testing and supported versions, although other versions are expected to work.

Download 
`jeo_0.5_amd64.deb <http://github.com/jeo/jeo-cli/releases/download/0.5/jeo_0.5_amd64.deb>`_ and 
install with the :command:`dpkg` command:

.. code-block:: bash

   $ wget http://github.com/jeo/jeo-cli/releases/download/0.5/jeo_0.5_amd64.deb
   $ sudo dpkg -i jeo_0.5_amd64.deb

.. note::

   The webupd8 package repository provides an easy way to install Java 8.

   .. code-block:: bash

      $ sudo add-apt-repository ppa:webupd8team/java
      $ sudo apt-get update
      $ sudo apt-get install oracle-java8-installer

Fedora
^^^^^^

RPM packages are provided for 64-bit Fedora systems. The packages are built and verified for Fedora 
21 but are expected to work on a number other versions as well.

Download 
`jeo-0.5-1.fc21.x86_64.rpm <http://github.com/jeo/jeo-cli/releases/download/0.5/jeo-0.5-1.fc21.x86_64.rpm>`_ 
and install with the :command:`rpm` command:

.. code-block:: bash

   $ wget http://github.com/jeo/jeo-cli/releases/download/0.5/jeo-0.5-1.fc21.x86_64.rpm
   $ sudo rpm -ivh jeo-0.5-1.fc21.x86_64.rpm

.. warning::

   Even though the jeo rpm declares no dependency on GDAL the package manager will complain about an 
   unsatisfied dependency if libgdal is not present on the system. Options are:

   * Install gdal. Fedora provides recent gdal packages out of the box.

     .. code-block:: bash

        $ yum install gdal

   * Or force install the rpm with ... 

.. todo:: Figure out what command to force is
.. todo:: Show example of error

.. note::

   Fedora distributions provide Java 8 out of the box via OpenJDK:

   .. code-block:: bash

      $ sudo yum install java-1.8.0-openjdk

CentOS
^^^^^^

RPM packages are provided for 64-bit CentOS systems. The packages are built and verified for CentOS 
6.5 but are expected to work on other versions as well.

Download 
`jeo-0.5-1.el6.x86_64.rpm <http://github.com/jeo/jeo-cli/releases/download/0.5/jeo-0.5-1.el6.x86_64.rpm>`_ 
and install with the :command:`rpm` command:

.. code-block:: bash

   $ wget http://github.com/jeo/jeo-cli/releases/download/0.5/jeo-0.5-1.el6.x86_64.rpm
   $ sudo rpm -ivh jeo-0.5-1.el6.x86_64.rpm

.. warning::

   Even though the jeo rpm declares no dependency on GDAL the package manager will complain about an 
   unsatisfied dependency if libgdal is not present on the system. Options are:

   * Install gdal. Unfortunately installing gdal on CentOS requires some work:

     .. code-block:: bash


   * Or force install the rpm with ... 

.. todo:: Updated gdal instructions for fedora
.. todo:: Figure out what command to force is
.. todo:: Show example of error

.. note::

   The easiest way to install Java 8 on CentOS is to download packages from 
   `Oracle <http://www.oracle.com/technetwork/java/javase/downloads/>`_.


Windows
^^^^^^^

No native Windows packaging is available at this time. See the next section for platform independent
installation instructions.

Other Platforms
^^^^^^^^^^^^^^^

The CLI can also be installed manually using the platform dependent binary package.

#. Download and unpack 
   `jeo-0.5-cli.zip <http://github.com/jeo/jeo-cli/releases/download/0.5/jeo-0.5-cli.zip>`_
#. Update the `PATH` environment variable to include the :file:`bin` directory of the unpacked 
   archive.
#. Ensure the `JAVA_HOME` environment variable points to a Java 8 installation.

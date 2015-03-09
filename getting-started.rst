.. _getting_started:

Getting Started
===============

The easiest way to start using jeo is by declaring a dependency with your build tool of choice.

Maven
-----

Applications using the `Maven <http://maven.apache.org/>`_ build system must first add the Boundless 
maven repository the project :file:`pom.xml`.

.. code-block:: xml

   <repositories>
     <repository>
       <id>boundless</id>
       <name>Boundless Maven Repository</name>
       <url>http://repo.boundlessgeo.com/main</url>
     </repository>
   </repositories>

And then declare the dependency on jeo.

.. code-block:: xml

   <dependency>
     <groupId>org.jeo</groupId>
     <artifactId>jeo</artifactId>
     <version>0.5</version>
   </dependency>

Gradle
------

Applications using the `Gradle <http://www.gradle.org>`_ build system must add the Central and 
Boundless maven repositories to :file:`build.gradle`.

.. code-block:: groovy

   repositories {
     mavenCentral()
     maven {
       url 'http://repo.boundlessgeo.com/main'
     }
   }

And then declare the dependency on jeo.

.. code-block:: groovy

   dependencies {
     compile group: 'org.jeo', name: 'jeo', version: '0.5'
   }


SBT
---

Applications using the `sbt <http://www.scala-sbt.org>`_ build system must add  the Boundless maven 
repository to :file:`build.sbt`.

.. code-block:: scala

   resolvers += "boundless" at "http://repo.boundlessgeo.com/main"

And then declare the library dependency no jeo.

.. parsed-literal::

   libraryDependencies += "org.jeo" % "jeo" % "0.5"

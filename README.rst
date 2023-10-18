==================
j2y - A Jinja2 CLI
==================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
    :alt: Code Style: Black

|

Render Jinja2 templates on the command line using a YAML_, JSON_ or HCL_ file
as input for the render context.

This is a fork of `Christian Haudum`_'s great Jinja2 CLI tool j2y_.
The purpose of this fork is to provide active maintenance, bug fixes and new features.

Installation
============

``j2y`` is installed using ``pip``::

  $ pip install -e git+https://github.com/crate/j2y.git@master#egg=j2y

.. Note::

   The name of this Python package is ``j2y``, but it will be renamed to
   ``j2-cli`` with the next major release.

Usage
=====

By default, the ``j2cli`` command takes a YAML_ file as input::

  $ j2cli template.j2 < values.yaml

Alternatively you can use JSON_ or HCL_ as input format::

  $ j2cli template.j2 -f json < values.json
  $ j2cli template.j2 -f hcl < values.hcl

It's also possible to provide multiple input files::

  $ j2cli template.j2 --context v1.yaml --context v2.yaml

Run ``j2cli -h`` to see all available options.

Template Variables
------------------

Additionally to the variables provided by the input file, ``j2cli`` also
provides built-in default variables. These variables are:

:meta.date:
  Type:  ``datetime``

  Value: Current UTC datetime object

:meta.platform:
  Type:  ``dict``

  Value: Output of ``platform.uname()``

:env:
  Type:  ``dict``

  Value: All environment variables (output of ``os.environ``).


Documentation
.............

The tests located in the ``docs/`` folder can also be built into HTML using
Sphinx_::

  (env) $ sphinx-build -E -W docs/ _build/


.. _YAML: http://yaml.org/spec/
.. _JSON: https://www.json.org/
.. _HCL: https://github.com/hashicorp/hcl
.. _black: https://github.com/ambv/black
.. _Sphinx: http://www.sphinx-doc.org/en/master/
.. _Christian Haudum: https://github.com/chaudum
.. _j2y: https://github.com/chaudum/j2y

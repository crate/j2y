===============
Developer Guide
===============


Local Development
=================

Bootstrapping
-------------

Create a virtualenv_ and install the package as develop egg::

  $ python -m venv env
  $ source env/bin/activate

Before installing any other dependencies, make sure ``pip`` and ``wheel`` are
up to date::

  $ (env) python -m pip install -U pip wheel

Then install the dependencies using ``pip``::

  $ (env) python -m pip install -e .

Tests
-----

At the moment there are very simple test cases only. Test are written as
Python doctests and run using pytest_::

  $ (env) python -m pip install -e ".[test]"
  $ (env) pytest

Pytest additionally runs the black_ linter and mypy_ static type checker.

Pre-commit hooks
----------------

This project uses `pre-commit`_ to ensure proper linting, code formatting, and
type checking. Tools, such as ``black``, ``flake8``, ``isort``, and ``mypy``
should be run as hooks upon committing or pushing code.
When at least one of the hooks fails, committing or pushing changes is aborted
and manual intervention is necessary. For example, an ill-formatted piece of
Python code that is staged for committing with Git, would be cleaned up by the
``black`` hook. It's then up to the developer to either amend the changes or
stage them as well.

Install ``pre-commit`` for your user and verify that the installation worked::

    $ python -m pip install --user pre-commit

Once you've confirmed the successful installation of ``pre-commit``, install
the hooks for this project::

    $ pre-commit install -t pre-commit -t pre-push --install-hooks
    pre-commit installed at .git/hooks/pre-commit
    pre-commit installed at .git/hooks/pre-push
    ...

From now on, each time you run ``git commit`` or ``git push``, ``pre-commit``
will run "hooks" defined in the ``.pre-commit-config.yaml`` file on the staged
files.

Release
=======

#. Create a new branch named ``<prefix>/prepare-x.y.z``.

#. Update the ``__version__`` in ``setup.py``.

#. Add new section to ``CHANGES.rst`` with the version and release date in the
   format ``yyyy/mm/dd x.y.z``.

#. Create a PR against ``master`` or version branch (e.g. ``0.1``).

#. After PR is merged, tag the release by running::

    ./dev/tools/create_tag.sh


.. _virtualenv: https://docs.python.org/3/tutorial/venv.html
.. _pytest: https://docs.pytest.org/en/latest/
.. _black: https://github.com/ambv/black
.. _mypy: https://github.com/python/mypy
.. _pre-commit: https://pre-commit.com

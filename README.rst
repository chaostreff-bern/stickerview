===========
STICKERVIEW
===========


INSTALL
=======
Install this repository into a virtualenv with python 3.

.. code-block:: Bash

  git clone git@github.com:keachi/stickerview.git /opt/stickerview
  cd /opt/stickerview
  virtualenv -p /usr/bin/python3 .venv
  . .venv/bin/activate
  pip install .


USAGE
=====
First, create the data directory, and after the database.

.. code-block:: Bash

  cd /opt/stickerview
  mkdir -p data
  ./manage.py migrate
  ./manage.py collectstatic

And then start the application.

.. code-block:: Bash

  ./manage.py runserver


LICENSE
=======

Copyright (C) 2016-2017  Tobias Rueetschi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see `<http://www.gnu.org/licenses/>`_.


.. vim: set spell spelllang=en sw=2 ts=2 et wrap tw=76 :

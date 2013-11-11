.. Flask-Scrypt documentation master file, created by
   sphinx-quickstart on Sun Nov 10 21:24:55 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Flask-Scrypt
============

Flask-Scrypt is a `Flask`_ extension used to generate scrypt password hashes and random salts. For those looking for extra security compared to
SHA-1 and MD5 encryption. Flask-Scrypt depends on `py-scrypt`_ which should install automatically but can be installed manually using 
pip install scrypt

.. _py-scrypt: https://bitbucket.org/mhallin/py-scrypt/src
.. _Flask: http://flask.pocoo.org

.. toctree::
   :maxdepth: 2

Installation
------------

Install the extension with one of the following commands::

    $ pip flask-scrypt

or alternatively if you must::

    $ easy_install install flask-scrypt


Usage
-----



>>> from flask.ext.scrypt import generate_random_salt, generate_password_hash, check_password_hash
>>> salt = generate_password_salt() #: You can also provide the byte length to return: salt = generate_password_salt(32)
>>> password_hash = generate_password_hash('mypassword', salt)

Remember you sould store the generated salt and hash in your database with each user to use with check_password_hash().

>>> check_password_hash('mypassword', password_hash, salt) # if password matches password used to generate_password_hash function will return True.

API
---

.. automodule:: flask_scrypt
    :members:

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


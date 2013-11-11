.. Flask-Scrypt documentation master file, created by
   sphinx-quickstart on Sun Nov 10 21:24:55 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-Scrypt's documentation!
========================================

.. toctree::
   :maxdepth: 2
   Usage
   API


Flask-Scrypt is a flask extension used to generate scrypt password hashes and random salts. For those looking for extra security compared to
SHA-1 and MD5 encryption. Flask-Scrypt depends on scrypt >= 0.6.1 which should install automatically but can be installed manually using 
pip install scrypt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Usage
=====

>>> from flask.ext.scrypt import generate_random_salt, generate_password_hash, check_password_hash
>>> salt = generate_password_salt() #: You can also provide the byte length to return: salt = generate_password_salt(32)
>>> password_hash = generate_password_hash('mypassword', salt)

Remember you sould store the generated salt and hash in your database with each user to use with check_password_hash().

>>> check_password_hash('mypassword', password_hash, salt) # if password matches password used to generate_password_hash function will return True.

API
===

.. automodule:: flask_scrypt
    :members:

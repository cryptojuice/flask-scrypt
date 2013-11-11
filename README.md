##Flask-Scrypt
============

Flask-Scrypt flask extension provides scrypt password hashing and random salt generation.

## Installation

    $ pip install flask-scrypt

## Usage

    from flask.ext.scrypt import generate_password_hash, generate_random_salt, check_password_hash

Generate random salt for use with the generate_password_hash function. You will want to store this salt with the rest of your users database information. This salt along with the generated hash will be used to check the password later on.

    salt = generate_random_salt()
    password_hash = generate_password_hash('mypassword', salt)
    
Pull stored salt and password_hash from database:

    salt = 'Users salt you stored in database'
    password_hash = 'Hash you stored in database'
    
Check if password matches hash/salt combo:

    check_password_hash('mypassword', password_hash, salt) 
check_password_hash() returns True is password checks out, otherwise returns False.

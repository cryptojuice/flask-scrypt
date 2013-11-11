##Flask-Scrypt

Flask-Scrypt flask extension provides scrypt password hashing and random salt generation.

## Installation

    $ pip install flask-scrypt

## Usage

    from flask.ext.scrypt import generate_password_hash, generate_random_salt, check_password_hash

    salt = generate_random_salt()
    password_hash = generate_password_hash('mypassword', salt)

    check_password_hash('mypassword', password_hash, salt) # Returns True is password checks out otherwise returns False.

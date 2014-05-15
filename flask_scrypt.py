#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask-Scrypt flask extension provides scrypt password hashing and random salt generation.
Hashes and Salts are base64 encoded.
"""
from __future__ import print_function, unicode_literals
import sys
import base64
import hmac
from os import urandom

try:
    from itertools import izip
except ImportError:
    izip = zip

_builtin_safe_str_cmp = getattr(hmac, 'compare_digest', None)

__version_info__ = ('0', '1', '3', '6')
__version__ = '.'.join(__version_info__)
__author__ = 'Gilbert Robinson'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013 Gilbert Robinson, Copyright (c) 2014 Samuel Marks'
__all__ = ['generate_password_hash', 'generate_random_salt',
           'check_password_hash', 'enbase64', 'debase64']

try:
    from scrypt import hash as scrypt_hash
except ImportError as err:
    print('Please install py-scrypt package. Error: ', err)
    raise err

PYTHON2 = sys.version_info < (3, 0)


def enbase64(byte_str):
    """
    Encode bytes/strings to base64.

    Args:
        - ``byte_str``:  The string or bytes to base64 encode.

    Returns:
        - byte_str encoded as base64.
    """

    # Python 3: base64.b64encode() expects type byte
    if isinstance(byte_str, str) and not PYTHON2:
        byte_str = bytes(byte_str, 'utf-8')
    return base64.b64encode(byte_str)


def debase64(byte_str):
    """
    Decode base64 encoded bytes/strings.

    Args:
        - ``byte_str``:  The string or bytes to base64 encode. 

    Returns:
        - decoded string as type str for python2 and type byte for python3.
    """
    # Python 3: base64.b64decode() expects type byte
    if isinstance(byte_str, str) and not PYTHON2:
        byte_str = bytes(byte_str, 'utf-8')
    return base64.b64decode(byte_str)


def generate_password_hash(password, salt, N=1 << 14, r=8, p=1, buflen=64):
    """
    Generate password hash givin the password string and salt.

    Args:
        - ``password``: Password string.
        - ``salt`` : Random base64 encoded string.

    Optional args:
        - ``N`` : the CPU cost, must be a power of 2 greater than 1, defaults to 1 << 14.
        - ``r`` : the memory cost, defaults to 8.
        - ``p`` : the parallelization parameter, defaults to 1.

    The parameters r, p, and buflen must satisfy r * p < 2^30 and
    buflen <= (2^32 - 1) * 32.

    The recommended parameters for interactive logins as of 2009 are N=16384,
    r=8, p=1. Remember to use a good random salt.

    Returns:
        - base64 encoded scrypt hash.
    """
    if PYTHON2:
        password = password.encode('utf-8')
        salt = salt.encode('utf-8')
    pw_hash = scrypt_hash(password, salt, N, r, p, buflen)
    return enbase64(pw_hash)


def generate_random_salt(byte_size=64):
    """
    Generate random salt to use with generate_password_hash().

    Optional Args:
        - ``byte_size``: The length of salt to return. default = 64.

    Returns:
        - str of base64 encoded random bytes.
    """
    return enbase64(urandom(byte_size))


def check_password_hash(password, password_hash, salt, N=1 << 14, r=8, p=1, buflen=64):
    """
    Given a password, hash, salt this function verifies the password is equal to hash/salt.

    Args:
       - ``password``: The password to perform check on.

    Returns:
       - ``bool``
    """
    candidate_hash = generate_password_hash(password, salt, N, r, p, buflen)

    return safe_str_cmp(password_hash, candidate_hash)


def safe_str_cmp(a, b):
    """This function compares strings in somewhat constant time. This
    requires that the length of at least one string is known in advance.

    Returns `True` if the two strings are equal, or `False` if they are not.

    From: https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/security.py
    """
    if _builtin_safe_str_cmp is not None:
        return _builtin_safe_str_cmp(a, b)
    elif len(a) != len(b):
        return False
    rv = 0
    if not PYTHON2 and isinstance(a, bytes) and isinstance(b, bytes):
        for x, y in izip(a, b):
            rv |= x ^ y
    else:
        for x, y in izip(a, b):
            rv |= ord(x) ^ ord(y)
    return rv == 0

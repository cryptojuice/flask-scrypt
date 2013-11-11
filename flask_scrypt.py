""" Create base64 encode Scrypt hashes and random salts
"""
import sys
import base64
from os import urandom

__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = 'Gilbert Robinson'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013 Gilbert Robinson'
__all__ = ['generate_password_hash', 'generate_random_salt', \
        'check_password_hash', 'enbase64', 'debase64']

try:
    import scrypt
except ImportError as err:
    print('Please install py-scrypt package. Error: ', err)
    raise(err)

PYTHON3 = sys.version_info >= (3, 0)


def enbase64(byte_str):
    """
    Encode bytes to base64
        Args:
            byte_str : bytes to encode

    """
    return base64.b64encode(byte_str)


def debase64(byte_str):
    """
    Decode base64 encoded bytes
        Args:
            byte_str : bytes to decode
    """
    if PYTHON3 and isinstance(byte_str, str):
        byte_str = bytes(byte_str, 'utf-8')
    return base64.b64decode(byte_str)


def generate_password_hash(password, salt, N=1 << 14, r=8, p=1, buflen=64):
    """ Returns a base64 encoded password hash

        Args:
            password (str): Password string
            salt : Random base64 encoded string
            N : the CPU cost, must be a power of 2 greater than 1, defaults to 1 << 14
            r : the memory cost, defaults to 8
            p : the parallelization parameter, defaults to 1

            The parameters r, p, and buflen must satisfy r * p < 2^30 and
            buflen <= (2^32 - 1) * 32.

            The recommended parameters for interactive logins as of 2009 are N=16384,
            r=8, p=1. Remember to get a good random salt.
    """
    password = password.encode('utf-8')
    scrypt_hash = scrypt.hash(password, salt, N, r, p, buflen)
    return enbase64(scrypt_hash)


def generate_random_salt(byte_size=64):
    """ Generate random salt
        Args:
            byte_size (int): The length of salt to return. default = 64
    """
    return enbase64(urandom(byte_size))


def check_password_hash(password, password_hash, salt):
    """ Given a password, hash, salt this function verifies the password
        is equal to hash/salt.

        Args:
            password (str): The password to check.
    """


    if PYTHON3 and isinstance(salt, bytes):
        password = str(password)
        salt = salt.decode('utf-8')
    else:
        password = password.encode('utf-8')
        salt = salt.encode('utf-8')

    scrypt_hash_base64 = generate_password_hash(password, salt)

    if password_hash == scrypt_hash_base64:
        return True

    return False

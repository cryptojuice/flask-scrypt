#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main as unittest_main
import sys

from flask_scrypt import generate_random_salt, generate_password_hash, check_password_hash

PYTHON2 = sys.version_info <= (3, 0)

class ScryptTestCase(TestCase):
    def setUp(self):
        self.salt = generate_random_salt()
        self.password = 'mypassword'
        self.password_hash = generate_password_hash(self.password, self.salt)

    def test_check_password_correct(self):
        password = 'mypassword'
        salt = self.salt
        password_hash = generate_password_hash(password, salt)
        self.assertTrue(check_password_hash(password, password_hash, salt))

    def test_check_password_incorrect(self):
        incorrect_password = 'notmypassword'
        salt = self.salt
        password_hash = self.password_hash
        self.assertFalse(check_password_hash(incorrect_password, password_hash, salt))

    def test_check_password_correct_with_none_default_params(self):
        password = 'mypassword'
        salt = self.salt
        password_hash = generate_password_hash(password, salt, r=10)
        self.assertTrue(check_password_hash(password, password_hash, salt, r=10))

    def test_throws_attribute_error_when_salt_none(self):
        try:
            generate_password_hash(self.password, None)
        except AttributeError as err:
            self.assertEqual(err.message, u"Error encoding salt, please make sure salt is not None.")

    def test_password_fail_with_incorrect_salt(self):
        password = self.password
        password_hash = self.password_hash
        salt = generate_random_salt()
        self.assertFalse(check_password_hash(password, password_hash, salt))

    if PYTHON2:
        def test_accept_unicode_str_python2(self):
            salt = generate_random_salt()
            password = unicode(self.password)
            password_hash = generate_password_hash(password, salt)
            self.assertTrue(check_password_hash(password, password_hash, salt))


if __name__ == '__main__':
    unittest_main()

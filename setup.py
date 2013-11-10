"""
    Flask-Scrypt
    ------------

    Flask-Scrypt flask extension provides scrypt password hashing and
    random salt generation.

    Links
    `````
    * `development version <https://github.com/grobins2/flask-scrypt>`_
"""
from setuptools import setup, find_packages


setup(name='Flask-Scrypt',
        description='Flask extention to generate scrypt password hashes\
                and random salts',
        version='0.1',
        url='http://github.com/grobins2/flask-scrypt',
        packages=find_packages(),
        license='MIT',
        author='Gilbert(Nick) Robinson',
        author_email='grobins2@gmail.com',
        long_description=__doc__,
        py_modules=['flask_scrypt'],
        platforms='any',
        install_requires=['Flask'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Lisense :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
            ])

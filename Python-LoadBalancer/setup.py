#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':

    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except:
        long_description = "See README"

    setup(name='PynocoLB',
            version='2.0.0',
            scripts=['PynocoLB.py'],
            packages=['pynocolb'],
            author='Team NeoTechies',
            author_email='',
            maintainer='',
            maintainer_email='',
            provides=['PynocoLB'],
            description='A simple, fast, pure-python load balancer',
            url='',
            long_description=long_description,
            license='GPLv3',
            keywords=['load balancer', 'load balance', 'python', 'balance', 'lb', 'http', 'socket', 'port', 'forward', 'tcp', 'fast', 'server', 'network'],
            classifiers=['Development Status :: 4 - Beta',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3.4',
                         'Programming Language :: Python :: 3.5',
                         'Topic :: Internet',
                         'Topic :: Internet :: WWW/HTTP',
                         'Topic :: System :: Distributed Computing',
                         'Topic :: System :: Networking',
            ]
    )

#!/usr/bin/env python
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


setup(
    name='kombu-django-json-serializer',
    version='0.1.2',
    description="A JSON serializer for Kombu that makes use of Django's extended JSON serializers",
    long_description=open('README.rst').read(),
    author="Anentropic",
    author_email="ego@anentropic.com",
    url="https://github.com/anentropic/kombu-django-json-serializer",
    packages=['kombu_django'],
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    entry_points={
        'kombu.serializers': [
            'django_json = kombu_django.serializer:register_args'
        ]
    },
    tests_require=[
        'tox>=1.8',
    ],
    cmdclass={'test': Tox},
)

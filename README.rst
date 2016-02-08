=================
kombu-django-json-serializer
=================

|Build Status| |PyPi Version|

.. |Build Status| image:: https://travis-ci.org/anentropic/kombu-django-json-serializer.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/anentropic/kombu-django-json-serializer
.. |PyPi Version| image:: https://badge.fury.io/py/kombu-django-json-serializer.svg
    :alt: Latest PyPI version
    :target: https://pypi.python.org/pypi/kombu-django-json-serializer/

Tested against same versions of Python that Django supports:

=========== ======= ======= ======= ======= ======= =======
     x       Py2.6   Py2.7   Py3.2   Py3.3   Py3.4   Py3.5 
=========== ======= ======= ======= ======= ======= =======
Django 1.4   *       *                                     
Django 1.5   *       *       *       *                     
Django 1.6   *       *       *       *                     
Django 1.7           *       *       *       *             
Django 1.8           *       *       *       *       *     
Django 1.9           *                       *       *     
=========== ======= ======= ======= ======= ======= =======


A JSON serializer for Kombu that makes use of Django's extended JSON serializers

.. code:: bash

    pip install kombu-django-json-serializer


Makes a ``'django_json'`` serializer type available, for example:

.. code:: python

	>>> producer = Producer(channel,
	                        exchange=exchange,
	                        routing_key=rkey,
	                        serializer="django_json")
	>>> producer.publish(MyModel.objects.get(pk=3))

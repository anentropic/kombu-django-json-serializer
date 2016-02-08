# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from datetime import date, datetime
from decimal import Decimal

import pytest
import pytz

from kombu_django.serializer import base_encoder, base_decoder

from testapp.factories import ExampleFactory


def test_string():
    obj = 'whatever 🚀'
    encoded = base_encoder(obj)
    assert base_decoder(encoded) == obj


def test_dict():
    obj = {'val': 'whatever 🚀'}
    encoded = base_encoder(obj)
    assert base_decoder(encoded) == obj


def test_list():
    obj = ['whatever 🚀']
    encoded = base_encoder(obj)
    assert base_decoder(encoded) == obj


def test_decimal():
    obj = Decimal('3.25')
    encoded = base_encoder(obj)
    # can't know from JSON that it was Decimal
    assert base_decoder(encoded) == '3.25'


def test_datetime():
    obj = datetime.now()
    encoded = base_encoder(obj)
    # TODO: decode datetime strings
    expected = obj.isoformat()
    if obj.microsecond:
        expected = expected[:23] + expected[26:]
    assert base_decoder(encoded) == expected


def test_datetime_timezone():
    obj = datetime.now().replace(tzinfo=pytz.timezone('US/Pacific'))
    encoded = base_encoder(obj)
    # TODO: decode datetime strings
    expected = obj.isoformat()
    if obj.microsecond:
        expected = expected[:23] + expected[26:]
    assert base_decoder(encoded) == expected


def test_datetime_timezone_utc():
    obj = datetime.now().replace(tzinfo=pytz.UTC)
    encoded = base_encoder(obj)
    # TODO: decode datetime strings
    expected = obj.isoformat()
    # ECMA-262 specifies milliseconds only and 'Z' rather than +00:00
    if obj.microsecond:
        expected = expected[:23] + expected[26:]
    if expected.endswith('+00:00'):
        expected = expected[:-6] + 'Z'
    assert base_decoder(encoded) == expected


def test_date():
    obj = date.today()
    encoded = base_encoder(obj)
    # TODO: decode date strings
    expected = obj.isoformat()
    assert base_decoder(encoded) == expected


def test_time():
    obj = datetime.now().time()
    encoded = base_encoder(obj)
    # TODO: decode date strings
    expected = obj.isoformat()
    # ECMA-262 specifies milliseconds only (and no timezone - will error)
    if obj.microsecond:
        expected = expected[:12]
    assert base_decoder(encoded) == expected


def test_model():
    obj = ExampleFactory.build()
    # Django serializers are designed for querysets
    # normal json fallback can't cope with a model instance
    with pytest.raises(TypeError):
        base_encoder(obj)


@pytest.mark.django_db
def test_model_list():
    obj = ExampleFactory()
    encoded = base_encoder([obj])
    assert (
        [d.object for d in base_decoder(encoded)] ==
        [obj]
    )


@pytest.mark.django_db
def test_model_queryset():
    obj = ExampleFactory()
    encoded = base_encoder(ExampleFactory._meta.model.objects.all())
    assert (
        [d.object for d in base_decoder(encoded)] ==
        [obj]
    )

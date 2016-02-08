import json

from django.core.serializers import serialize, deserialize
from django.core.serializers.json import DjangoJSONEncoder


def base_encoder(obj):
    try:
        return serialize('json', obj)
    except Exception:
        # not an iterable of Model instances
        # we can still be useful... (handle date/time & Decimal)
        return json.dumps(obj, cls=DjangoJSONEncoder)


def base_decoder(data):
    try:
        return [o for o in deserialize('json', data)]
    except Exception:
        # TODO: implement a DjangoJSONDecoder
        return json.loads(data)


register_args = (base_encoder, base_decoder, 'application/json', 'utf-8')

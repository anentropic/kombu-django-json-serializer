import json


def base_encoder(obj):
    from django.core.serializers import serialize
    from django.core.serializers.json import DjangoJSONEncoder
    try:
        return serialize('json', obj)
    except Exception:
        # not an iterable of Model instances
        # we can still be useful... (handle date/time & Decimal)
        return json.dumps(obj, cls=DjangoJSONEncoder, separators=(',', ':'))


def base_decoder(data):
    from django.core.serializers import deserialize
    try:
        return [o for o in deserialize('json', data)]
    except Exception:
        # TODO: implement a DjangoJSONDecoder
        return json.loads(data)


register_args = (base_encoder, base_decoder, 'application/json', 'utf-8')

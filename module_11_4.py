import inspect

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': [x for x in dir(obj) if not callable(getattr(obj, x))],
        'methods': [x for x in dir(obj) if callable(getattr(obj, x))],
        'module': inspect.getmodule(obj)
    }

number_info = introspection_info(42)
print(number_info)
import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = []
    for attr in dir(obj):
        if not inspect.isroutine(getattr(obj, attr)) and not attr.startswith("__"):
            attributes.append(attr)

    methods = []
    for method in dir(obj):
        if inspect.isroutine(getattr(obj, method)) and not method.startswith("__"):
            methods.append(method)

    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello")
print(string_info)

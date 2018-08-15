def jsonMap(fn, json_obj):
    """Apply function `fn` to each value in `json_obj`.
    json_obj is not a json string, but something that could be the result of
    json.load() - an object consisting of maps, lists and simple values.
    Example:
    In []: util.jsonMap(string.upper, {'keyA': 'value', 'keyB': ['a', 'b', 'c']})
    Out[]: {'keyA': 'VALUE', 'keyB': ['A', 'B', 'C']}
    Args:
        fn: callable taking one argument and returning one argument
        json_obj: an object consisting of maps, lists and simple values.
    """
    def _fn(val):
        if val is None:
            return None
        elif isinstance(val, dict):
            return {k: _fn(v) for k, v in val.items()}
        elif isinstance(val, list):
            return map(_fn, val)
        else:
            return fn(val)
    return _fn(json_obj)

from json import loads, dumps
import difflib
import sys


if sys.version[0] == '3':
    unicode = str


def isstr(string):
    return isinstance(string, str) or isinstance(string, unicode)


def is_dict_or_list(obj):
    return isinstance(obj, dict) or isinstance(obj, list)


def pretty(json_text):
    """
    Takes a JSON string and outputs an ordered, indented JSON string.
    """
    return dumps(loads(json_text), indent=4, sort_keys=True, separators=(',', ': '))


def diff(json_texta, json_textb):
    """
    Diff two json strings, giving a sensible prettified result.
    """
    return '\n'.join(
        difflib.unified_diff(
            pretty(json_texta).split("\n"),
            pretty(json_textb).split("\n")
        )
    )


def _selector(keys):
    sel = ""
    for key in keys:
        if isinstance(key, int):
            sel = sel + u"[{0}]".format(key)
        else:
            sel = sel + u"['{0}']".format(key)
    return sel


def _results(value, search, key_hierarchy):
    results = []
    if isinstance(value, dict):
        results.extend(_grep_dict(value, search, keys=key_hierarchy))
    elif isinstance(value, list):
        results.extend(_grep_list(value, search, keys=key_hierarchy))
    else:
        if isstr(value):
            value = value
        else:
            value = str(value)
        if search.lower() in value.lower():
            results.append((_selector(key_hierarchy), value))
    return results


def _grep_list(parsed, search, keys=None):
    results = []
    if keys is None:
        keys = []
    for index, value in enumerate(parsed):
        key_hierarchy = list(keys) + [index, ]
        results.extend(_results(value, search, key_hierarchy))
    return results


def _grep_dict(parsed, search, keys=None):
    results = []
    if keys is None:
        keys = []
    for key, value in parsed.items():
        key_hierarchy = list(keys) + [key, ]
        results.extend(_results(value, search, key_hierarchy))
    return results


def find(json, search_text):
    """
    Takes a JSON string and a search string and output a list of
    matching keys, values and text.
    """
    assert isstr(json) or is_dict_or_list(json)
    assert isstr(search_text)
    if sys.version[0] == '2' and type(search_text) is str:
        search_text = search_text.decode('utf8')
    parsed = json if is_dict_or_list(json) else loads(json)
    return _grep_dict(parsed, search_text) if isinstance(parsed, dict) else\
        _grep_list(parsed, search_text)


def grep(json, search_text):
    import sys
    sys.stdout.write(
        '\n'.join([
            u"{0}: {1}".format(keys, text)
            for keys, text in find(json, search_text)])
    )
    sys.stdout.flush()

from json import loads
import difflib
import json
import sys


if sys.version[0] == '3':
    unicode = str


def isstr(string):
    return isinstance(string, str) or isinstance(string, unicode)


def pretty(json_text):
    """
    Takes a JSON string and outputs an ordered, indented JSON string.
    """
    return json.dumps(loads(json_text), indent=4, sort_keys=True, separators=(',', ': '))


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


def _grep_list(parsed, search, keys=None):
    results = []
    if keys is None:
        keys = []
    for index, value in enumerate(parsed):
        key_hierarchy = list(keys) + [index, ]
        if isinstance(value, dict):
            results.extend(_grep_dict(value, search, keys=key_hierarchy))
        if isstr(value):
            if search in value:
                results.append(u'{0}: "{1}"'.format(_selector(key_hierarchy), value))
    return results


def _grep_dict(parsed, search, keys=None):
    results = []
    if keys is None:
        keys = []
    for key, value in parsed.items():
        key_hierarchy = list(keys) + [key, ]
        if isinstance(value, dict):
            results.extend(_grep_dict(value, search, keys=key_hierarchy))
        if isinstance(value, list):
            results.extend(_grep_list(value, search, keys=key_hierarchy))
        if isstr(value):
            if search in value:
                results.append(u'{0}: "{1}"'.format(_selector(key_hierarchy), value))
        if search in key:
            results.append(u'{0}: "{1}"'.format(_selector(key_hierarchy), value))
    return results


def grep(json_text, search):
    """
    Takes a JSON string and a search string and output a list of
    matching keys, values and text.
    """
    assert isstr(json_text)
    assert isstr(search)
    if sys.version[0] == '2' and type(search) is str:
        search = search.decode('utf8')
    parsed = loads(json_text)
    return "\n".join(
        _grep_dict(parsed, search) if isinstance(parsed, dict) else _grep_list(parsed, search)
    )

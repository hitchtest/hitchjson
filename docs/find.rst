Grep JSON
=========

.. code-block:: python

  >>> from hitchjson import find
  >>> from json import loads

.. code-block:: python

  >>> find(buried_text_dict, "buried") == [(u"['x']['somek\xe9y']", u'text with buried string')]
  True

.. code-block:: python

  >>> find(loads(buried_text_dict), "buried") == [(u"['x']['somek\xe9y']", u'text with buried string')]
  True

.. code-block:: python

  >>> find(buried_text_list, "buriéd") == [(u"[2]['é'][2]", u"buriéd text")]
  True

.. code-block:: python

  >>> find(loads(buried_text_list), "buriéd") == [(u"[2]['é'][2]", u"buriéd text")]
  True


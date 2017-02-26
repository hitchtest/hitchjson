Find JSON
=========

Find text buried in enormous JSON structures and
get a selector that you can use to look up that data.


.. code-block:: python

  >>> from hitchjson import find
  >>> from json import loads

.. code-block:: python

  >>> find(buried_text_dict, "Buried") == [(u"['x']['somekéy']", u'text with buried string')]
  True

.. code-block:: python

  >>> find(buried_text_dict, "3") == [(u"['c']", u'3')]
  True

.. code-block:: python

  >>> find(loads(buried_text_dict), "Buried") == [(u"['x']['somekéy']", u'text with buried string')]
  True

.. code-block:: python

  >>> find(buried_text_list, "buriéd") == [(u"[2]['é'][2]", u"buriéd text")]
  True

.. code-block:: python

  >>> find(loads(buried_text_list), "buriéd") == [(u"[2]['é'][2]", u"buriéd text")]
  True

.. code-block:: python

  >>> find(buried_text_list, "3") == [(u"[2]['c']", u"3")]
  True


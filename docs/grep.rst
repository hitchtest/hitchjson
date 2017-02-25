Grep JSON
=========

.. code-block:: python

  >>> from hitchjson import grep
  >>> from json import loads

.. code-block:: python

  >>> grep(buried_text_dict, "buried") == results_dict.strip()
  True

.. code-block:: python

  >>> grep(loads(buried_text_dict), "buried") == results_dict.strip()
  True

.. code-block:: python

  >>> grep(buried_text_list, "buriéd") == results_list.strip()
  True

.. code-block:: python

  >>> grep(loads(buried_text_list), "buriéd") == results_list.strip()
  True


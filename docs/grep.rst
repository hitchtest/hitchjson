Grep JSON
=========

.. code-block:: python

  >>> from hitchjson import grep

.. code-block:: python

  >>> grep(buried_text_dict, "buried") == results_dict.strip()
  True

.. code-block:: python

  >>> grep(buried_text_list, "buriéd") == results_list.strip()
  True


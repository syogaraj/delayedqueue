.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/delayedqueue.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/delayedqueue
    .. image:: https://readthedocs.org/projects/delayedqueue/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://delayedqueue.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/delayedqueue/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/delayedqueue
    .. image:: https://img.shields.io/conda/vn/conda-forge/delayedqueue.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/delayedqueue
    .. image:: https://pepy.tech/badge/delayedqueue/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/delayedqueue
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/delayedqueue

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

.. image:: https://img.shields.io/pypi/v/delayedqueue.svg
   :alt: PyPI-Server
   :target: https://pypi.org/project/delayedqueue/

***********
delayedqueue
***********


    Delay Queue Implementation in Python

----
Usage
----

Example::
   from delayedqueue import DelayedQueue
   delay_queue = DelayedQueue()
   delay_queue.put("an item", 30)

   delay_queue.get()
   # Waits for 30seconds before returning "an item". If any other item is added via another thread and if the delay preceeds of that item, then that item will be returned first.


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.

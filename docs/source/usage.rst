Usage
=====

.. _installation:

Installation
------------

To use georapid, first install it using pip:

.. code-block:: console

   (.venv) $ pip install georapid

Creating clients
----------------

To authorize against the endpoints being hosted on Rapid API you need to use your own Rapid API Key.
The default client factory reads the API key from an environment variable named 'x-rapidapi-key'.

Creating a client for a specific host,
you can use the ``georapid.environment.EnvironmentClientFactory.create_client_with_host()`` function:

.. autofunction:: georapid.environment.EnvironmentClientFactory.create_client_with_host

The ``host`` parameter must target the specific host like ``"geoprotests.p.rapidapi.com"``.
Otherwise, :py:func:`georapid.environment.EnvironmentClientFactory.create_client_with_host` will raise an exception.

.. autoexception:: ValueError

For example:

>>> from georapid.client import GeoRapidClient
>>> from georapid.factory import EnvironmentClientFactory
>>> from georapid.protests import articles
>>> client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
>>> articles(client)
"articles": [{ 
   "url": "https://www.tt.com/artikel/18526556/traenengaseinsatz-gegen-demonstranten-im-sudan", 
   "urlmobile": "", 
   "title": "Tränengaseinsatz gegen Demonstranten im Sudan | Tiroler Tageszeitung Online", 
   "seendate": "20211231T003000Z", 
   "socialimage": "", 
   "domain": "tt.com", 
   "language": "German", 
   "sourcecountry": "Austria"},
   ...
]
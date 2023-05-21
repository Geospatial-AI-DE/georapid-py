Guides
======
We provide learning paths for best guidance leveling up your Geospatial Intelligence skills.

Learning path for geoprotests
-----------------------------
Analyze the broadcasted news related to protests, and identify hot- and cold spots.

Ramp up your development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Setup your development environment and start with the first tutorial activating your Geospatial Intelligence skills.
You will learn how to analyse the broadcasted news of the last 24 hours.

We are ging to use the `ArcGIS API for Python <https://developers.arcgis.com/python>`__ which enables access to ready-to-use maps and curated geographic data from Esri and other authoritative sources, and works with your own data as well. 
It integrates well with the scientific Python ecosystem and includes rich support for Pandas and Jupyter notebook.

Step 1: Create a dedicated environment
""""""""""""""""""""""""""""""""""""""
Choose your favourite enironment e.g. conda or pip and create a dedicated environment.
Enter the following at the prompt:

*Using conda:*

.. code-block:: console

   conda create -n geoint

**Activate the dedicated environment:**

.. code-block:: console

   conda activate geoint

*Using pipenv:*

.. code-block:: console

   python -m venv geoint

**Activate the dedicated environment:**

*Using pipenv on Linux:*

.. code-block:: console

   source geoint/bin/activate

*Using pipenv on Windows:*

.. code-block:: console

   geoint/Scripts/activate

Step 2: Install and Setup packages
""""""""""""""""""""""""""""""""""
The arcgis package is much more restrictive than our georapid package.
We start setting up arcgis first.
Follow the detailed steps at: `Install and Setup <https://developers.arcgis.com/python/guide/install-and-set-up>`__.

The georapid package only supports pipenv.
You can install any pip package from an activated conda environment, too.
Enter the following at the prompt:

.. code-block:: console

   pip install georapid

The default factory implementation reads the API key using the environment.
You need to set the environment variable ``x_rapidapi_key`` containing your Rapid API key.

After you installed the georapid and arcgis package, you need to verify it.

.. note::
    Make sure you set the environment variable ``x_rapidapi_key``.
    Otherwise, the default factory implementation will raise a :exc:`ValueError`.

Step 3: Verify your environment
"""""""""""""""""""""""""""""""
Navigate to the directory you want to work in.
Start a new Juypter notebook instance:

.. code-block:: console

   jupyter notebook

Create new notebook named ``Mapping Protests``.
Add the following imports and execute the cell:

>>> from arcgis import GIS
>>> from arcgis.features import FeatureSet
>>> from georapid.client import GeoRapidClient
>>> from georapid.factory import EnvironmentClientFactory
>>> from georapid.formats import OutFormat
>>> from georapid.protests import aggregate

Create a client instance:

>>> host = "geoprotests.p.rapidapi.com"
>>> client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)

.. warning::
    The ``host`` parameter must target the specific host like ``"geoprotests.p.rapidapi.com"``.
    Furthermore, the factory directly access ``os.environ['x_rapidapi_key']`` and uses the specified API key as a header parameter.
    Otherwise, :py:func:`georapid.factory.EnvironmentClientFactory.create_client_with_host` will raise a :exc:`ValueError`.

Connect to ArcGIS Online anonymously and display a map view:

>>> gis = GIS()
>>> world_map = gis.map()
>>> world_map

Step 4: Map the broadcasted news related to protests of the last 24 hours
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
You define some utility functions plotting the broadcasted news as aggregated polygon features.
Add the following utility function:

>>> def plot_aggregated(map_view, spatial_df, column='count'):
>>> """
>>> Plots the spatial dataframe as classified polygons using the specified map view.
>>> """
>>> if spatial_df.empty:
>>>     print("The dataframe is empty!")
>>> else:
>>>     spatial_df.spatial.plot(map_view,
>>>                             renderer_type='c', # for class breaks renderer
>>>                             method='esriClassifyNaturalBreaks', # classification algorithm
>>>                             class_count=5, # choose the number of classes
>>>                             col=column, # numeric column to classify
>>>                             cmap='YlOrRd', # color map to pick colors from for each class
>>>                             alpha=0.35 # specify opacity
>>>     )

We want to query the aggregated broadcasted news as an Esri FeatureSet and plot it using a map view.
Add the following code-block and execute the cell:

>>> world_map = gis.map()
>>> protests_featureset = FeatureSet.from_dict(aggregate(client, format=OutFormat.ESRI))
>>> plot_aggregated(world_map, protests_featureset.sdf)
>>> world_map

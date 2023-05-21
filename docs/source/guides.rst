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

Using conda:

.. code-block:: console

   conda create -n geoint

Using pipenv:

.. code-block:: console

   python -m venv geoint

Activate the dedicated environment:

Using conda:

.. code-block:: console

   conda activate geoint

Using pipenv on Linux:

.. code-block:: console

   source geoint/bin/activate

Using pipenv on Windows:

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
Start a new Juypter notebook instance:

.. code-block:: console

   jupyter notebook

Step 4:
"""""""
Lets see.

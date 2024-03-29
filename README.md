[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Geospatial-AI-DE/georapid-py)](https://pypi.org/project/georapid)
![GitHub License](https://img.shields.io/github/license/Geospatial-AI-DE/georapid-py)
[![Read the Docs](https://img.shields.io/readthedocs/georapid)](https://georapid.readthedocs.io/en/latest)
[![Tweet Me](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%2Fgeorapid-py)](https://twitter.com/intent/tweet?text=Outstanding:&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%2Fgeorapid-py)

# Geospatial Knowledge supporting Intelligence workflows
Query broadcasted news worldwide and visualize them using spatial aggregations. This modern Python module represents an idiomatic client accessing the [Geospatial Knowledge APIs](https://geospatial-ai.de/?rara_portfolio_categories=api-services) being hosted on [Rapid API Hub](https://rapidapi.com/hub). 

## Why is it important?
Geospatial Knowledge refers to semantic information about specific locations on the Earth's surface. 
It includes location-enabled things - not strings - like physical features of the landscape, the location of cities or in general human activities, and their spatial distribution. 
Various sources like satellite imagery, location-enabled datasets, and most important any location-enabled information in the context of Open Source Intelligence (OSINT) are used to create Geospatial Knowledge. 
By analyzing location-enabled things an analyst is empowered to gain insights into various aspects of human activities. 

## Next steps
Please, check out the [RapidAPI Account Creation and Management Guide](https://docs.rapidapi.com/docs/account-creation-and-settings).

Start with the [Usage](https://georapid.readthedocs.io/en/latest/usage.html) section for further information, including
how to install the Python module.

## Features
### [geoprotests API](https://rapidapi.com/gisfromscratch/api/geoprotests/)
*Query protests worldwide and visualize them using spatial aggregations.*
### [geoconflicts API](https://rapidapi.com/gisfromscratch/api/geoconflicts/)
*Query armed conflict events worldwide and visualize them using spatial aggregations.*
### [geofires API](https://rapidapi.com/gisfromscratch/api/geofires/)
*Query wildfires worldwide and visualize them using spatial aggregations.*
### [geojoins API](https://rapidapi.com/gisfromscratch/api/geojoins/)
*Joins two spatially enabled feature collections based on their relative spatial locations.*
### [geodetic API](https://rapidapi.com/gisfromscratch/api/geodetic/)
*Enables various geodetic functions like buffers, points from distance and direction, points along path and wedge construction.*

## Ready to use
The geoprotests and geofires services offer ready-to-use geospatial features representing broadcasted news related to various themes. The underlying serverless cloud-backend analyses raw geospatial locations of news articles provided by the [Global Database of Events, Language and Tone (GDELT) Project](https://www.gdeltproject.org/).

The geoconflicts service offer ready-to-use geospatial features representing armed conflicts since 2020-01-01. The underlying serverless cloud-backend analyses raw armed conflicts of the [Upsalla Conflict Data Program (UCDP)](https://ucdp.uu.se/downloads/index.html#candidate).

Please cite:
* Hegre, Håvard, Mihai Croicu, Kristine Eck, and Stina Högbladh (July 2020)
Introducing the UCDP Candidate Events Dataset. Research & Politics

Every geospatial result support the GeoJSON and Esri FeatureSet format out of the box. All endpoints support a date parameter for filtering the geospatial features. For best sustainability, the serverless cloud-backend queries the articles from the knowledge graph and calculates the geospatial features on-the-fly. You can use these geospatial features to build various mapping and geospatial applications.

# georapid-py
Query broadcasted news worldwide and visualize them using spatial aggregations.

## Ready to use
The [geospatial knowledge APIs](https://geospatial-ai.de/?rara-portfolio=geoint-api-services) offer ready-to-use geospatial features representing broadcasted news related to various themes. You can use these geospatial features to build various mapping and geospatial applications. The underlying serverless cloud-backend analyses raw geospatial locations of news articles provided by the Global Database of Events, Language and Tone (GDELT) Project (https://www.gdeltproject.org/).

Every geospatial result support the GeoJSON and Esri FeatureSet format out of the box. All endpoints support an optional date parameter for filtering the results. For best sustainability, the serverless cloud-backend queries the articles from the knowlegde graph and calculates the geospatial features on-the-fly.

# Copyright (C) 2022 Jan Tschada (gisfromscratch@live.de)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from georapid.client import GeoRapidClient
from georapid.factory import EnvironmentClientFactory
from georapid.protests import aggregate as aggregate_protests, articles as articles_protests, hotspots as hotspots_protests
from georapid.fires import aggregate as aggregate_fires, articles as articles_fires, query as query_fires
from georapid.joins import contains, covers, crosses, intersects, overlaps, touches
import unittest



class TestConnect(unittest.TestCase):

    def setUp(self) -> None:
        self._latitudes = [51.83864, 50.73438]
        self._longitudes = [12.24555, 7.09549]

    def test_create(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        self.assertIsNotNone(client, "Client must be initialized!")

    def test_protests_aggregate(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        geojson = aggregate_protests(client)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")

    def test_protests_articles(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        json = articles_protests(client)
        self.assertIsNotNone(json, "JSON response must be initialized!")

    def test_host_protests_articles(self):
        host = "geoprotests.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        json = articles_protests(client)
        self.assertIsNotNone(json, "JSON response must be initialized!")

    def test_protests_hotspots(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        geojson = hotspots_protests(client)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")

    def test_fires_aggregate(self):
        host = "geofires.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        geojson = aggregate_fires(client)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")

    def test_fires_articles(self):
        host = "geofires.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        json = articles_fires(client)
        self.assertIsNotNone(json, "JSON response must be initialized!")

    def test_fires_query(self):
        host = "geofires.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        geojson = query_fires(client)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")

    def test_joins_contains(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat = self._latitudes[0]
        lon = self._longitudes[0]
        delta = 0.1
        xmin, xmax, ymin, ymax = lon-delta, lon+delta, lat-delta, lat+delta
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[xmin, ymax], [xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]]]
                },
                "properties": {
                    "id": "left_polygon"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "id": "right_point"
                }
            }]
        }
        geojson = contains(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

    def test_joins_covers(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat = self._latitudes[0]
        lon = self._longitudes[0]
        delta = 0.1
        xmin, xmax, ymin, ymax = lon-delta, lon+delta, lat-delta, lat+delta
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[xmin, ymax], [xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]]]
                },
                "properties": {
                    "id": "left_polygon"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                },
                "properties": {
                    "id": "right_point"
                }
            }]
        }
        geojson = covers(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

    def test_joins_crosses(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat1_start = self._latitudes[0]
        lon1_start = self._longitudes[0]
        lat1_end = -lat1_start
        lon1_end = -lon1_start
        lat2_start = self._latitudes[1]
        lon2_start = self._longitudes[1]
        lat2_end = -lat2_start
        lon2_end = -lon2_start
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon1_start, lat1_start], [lon1_end, lat1_end]]
                },
                "properties": {
                    "id": "left_linestring"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon2_start, lat2_start], [lon2_end, lat2_end]]
                },
                "properties": {
                    "id": "right_linestring"
                }
            }]
        }
        geojson = crosses(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

    def test_joins_intersects(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat1_start = self._latitudes[0]
        lon1_start = self._longitudes[0]
        lat1_end = -lat1_start
        lon1_end = -lon1_start
        lat2_start = self._latitudes[1]
        lon2_start = self._longitudes[1]
        lat2_end = -lat2_start
        lon2_end = -lon2_start
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon1_start, lat1_start], [lon1_end, lat1_end]]
                },
                "properties": {
                    "id": "left_linestring"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon2_start, lat2_start], [lon2_end, lat2_end]]
                },
                "properties": {
                    "id": "right_linestring"
                }
            }]
        }
        geojson = intersects(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

    def test_joins_overlaps(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat1_start = self._latitudes[0]
        lon1_start = self._longitudes[0]
        lat1_end = self._latitudes[1]
        lon1_end = self._longitudes[1]
        lat2_start = self._latitudes[1]
        lon2_start = self._longitudes[1]
        lat2_end = self._latitudes[0]
        lon2_end = self._longitudes[0]
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon1_start, lat1_start], [lon1_end, lat1_end]]
                },
                "properties": {
                    "id": "left_linestring"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon2_start, lat2_start], [lon2_end, lat2_end]]
                },
                "properties": {
                    "id": "right_linestring"
                }
            }]
        }
        geojson = overlaps(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

    def test_joins_touches(self):
        host = "geojoins.p.rapidapi.com"
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        lat1_start = self._latitudes[0]
        lon1_start = self._longitudes[0]
        lat1_end = 0
        lon1_end = 0
        lat2_start = self._latitudes[1]
        lon2_start = self._longitudes[1]
        lat2_end = 0
        lon2_end = 0
        left = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon1_start, lat1_start], [lon1_end, lat1_end]]
                },
                "properties": {
                    "id": "left_linestring"
                }
            }]
        }
        right = { 
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[lon2_start, lat2_start], [lon2_end, lat2_end]]
                },
                "properties": {
                    "id": "right_linestring"
                }
            }]
        }
        geojson = touches(client, left, right)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        self.assertTrue('features' in geojson, "GeoJSON response must have features!")
        features = geojson['features']
        self.assertTrue(isinstance(features, list), "GeoJSON features must be an instance of list!")
        self.assertEqual(1, len(features), "One result feature was expected!")

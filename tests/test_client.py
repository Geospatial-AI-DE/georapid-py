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
from georapid.protests import aggregate
import unittest



class TestConnect(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_create(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        self.assertIsNotNone(client, "Client must be initialized!")

    def test_protests_aggregate(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        geojson = aggregate(client)
        self.assertIsNotNone(geojson, "GeoJSON response must be initialized!")
        
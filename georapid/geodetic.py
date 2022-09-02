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

import requests

from . client import GeoRapidClient
from . formats import OutFormat
from . units import LinearUnit



def create_points_along(client: GeoRapidClient, lat1: float, lon1: float, lat2: float, lon2: float, distances: list[float], offsets: list[float], unit: LinearUnit=LinearUnit.km, format: OutFormat=OutFormat.GEOJSON):
    """
    Creates points along the line defined by lat1, lon1 and lat2, lon2.
    The distances define the location along the line, and the offsets define the lateral offset.
    The number of distances must equal the number of offsets.
    A combination of distances=[0, <line length>] and offsets=[0, 0] creates a point at the start and another at the end location.
    The unit defines the linear unit e.g. 'km' for the distances and the offsets.
    The format can be GeoJSON or Esri.
    """
    endpoint = '{0}/along'.format(client.url)
    json = {
        'lat1': lat1,
        'lon1': lon1,
        'lat2': lat2,
        'lon2': lon2,
        'distances': distances,
        'offsets': offsets,
        'unit': str(unit),
        'format': str(format)
    }
    response = requests.request('POST', endpoint, headers=client.auth_headers, json=json)
    response.raise_for_status()
    return response.json()
# Copyright (C) 2023 Jan Tschada (gisfromscratch@live.de)
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

from datetime import datetime
import requests

from . client import GeoRapidClient
from . formats import OutFormat


def aggregate(client: GeoRapidClient, date: datetime = datetime(2022, 2, 24), format = OutFormat.GEOJSON):
    """
    Aggregates the armed conflict events using a spatial grid and returns the features as hexagonal bins.
    The underlying event database collects data since 2020-01-01. 
    The format can be GeoJSON or Esri JSON.
    """
    endpoint = '{0}/aggregate'.format(client.url)
    params = {
        'format': str(format)
    }
    if date:
        params['date'] = datetime.strftime(date, '%Y-%m-%d')

    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()
    return response.json()


def count(client: GeoRapidClient):
    """
    Returns the number of armed conflict events as a JSON result.
    """
    endpoint = '{0}/count'.format(client.url)
    response = requests.request('GET', endpoint, headers=client.auth_headers)
    response.raise_for_status()
    return response.json()
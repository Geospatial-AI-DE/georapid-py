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



def contains(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    endpoint = '{0}/contains'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right:': right_featurecollection
    }
    headers = client.auth_headers.copy()
    response = requests.request('POST', endpoint, headers=headers, json=json)
    return response.json()
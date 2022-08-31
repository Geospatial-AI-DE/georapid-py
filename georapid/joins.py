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
    """
    Joins the input features from 'left' with the matching target features from 'right' for all
    input features containing the target features. Therefore the target geometry 
    must be completely inside the input geometry. So that no points of the 
    target geometry lie in the exterior of the input geometry, and at least 
    one point of the interior of the target geometry lies in the interior of the input geometry.  
    """
    endpoint = '{0}/contains'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def covers(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    """
    Joins the input features from 'left' with the matching target features from 'right' for all
    input features covering the target features. Therefore no point of the target geometry must be 
    outside of the input geometry.
    """
    endpoint = '{0}/covers'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def crosses(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    """
    Joins the input features from 'left' with the matching target features from 'right' for all
    input features crossing the target features. Therefore the input and target geometry have some, 
    but not all interior points in common. So that the intersection of the input and target geometry 
    must be non-empty and must not equal the input nor the target geometry.
    """
    endpoint = '{0}/crosses'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def intersects(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    endpoint = '{0}/intersects'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def overlaps(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    endpoint = '{0}/overlaps'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def touches(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    endpoint = '{0}/touches'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()

def within(client: GeoRapidClient, left_featurecollection: dict, right_featurecollection: dict):
    endpoint = '{0}/within'.format(client.url)
    json = {
        'left': left_featurecollection,
        'right': right_featurecollection
    }
    return requests.request('POST', endpoint, headers=client.auth_headers, json=json).json()
    
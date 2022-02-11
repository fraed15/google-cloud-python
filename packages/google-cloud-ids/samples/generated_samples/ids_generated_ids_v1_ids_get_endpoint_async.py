# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for GetEndpoint
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-ids


# [START ids_generated_ids_v1_IDS_GetEndpoint_async]
from google.cloud import ids_v1


async def sample_get_endpoint():
    # Create a client
    client = ids_v1.IDSAsyncClient()

    # Initialize request argument(s)
    request = ids_v1.GetEndpointRequest(
        name="name_value",
    )

    # Make the request
    response = await client.get_endpoint(request=request)

    # Handle the response
    print(response)

# [END ids_generated_ids_v1_IDS_GetEndpoint_async]

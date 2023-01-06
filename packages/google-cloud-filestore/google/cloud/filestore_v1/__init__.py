# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.filestore import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_filestore_manager import (
    CloudFilestoreManagerAsyncClient,
    CloudFilestoreManagerClient,
)
from .types.cloud_filestore_service import (
    Backup,
    CreateBackupRequest,
    CreateInstanceRequest,
    DeleteBackupRequest,
    DeleteInstanceRequest,
    FileShareConfig,
    GetBackupRequest,
    GetInstanceRequest,
    Instance,
    ListBackupsRequest,
    ListBackupsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    NetworkConfig,
    NfsExportOptions,
    RestoreInstanceRequest,
    UpdateBackupRequest,
    UpdateInstanceRequest,
)

__all__ = (
    "CloudFilestoreManagerAsyncClient",
    "Backup",
    "CloudFilestoreManagerClient",
    "CreateBackupRequest",
    "CreateInstanceRequest",
    "DeleteBackupRequest",
    "DeleteInstanceRequest",
    "FileShareConfig",
    "GetBackupRequest",
    "GetInstanceRequest",
    "Instance",
    "ListBackupsRequest",
    "ListBackupsResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "NetworkConfig",
    "NfsExportOptions",
    "RestoreInstanceRequest",
    "UpdateBackupRequest",
    "UpdateInstanceRequest",
)
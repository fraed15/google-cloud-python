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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.routing.v2",
    manifest={
        "RouteLabel",
    },
)


class RouteLabel(proto.Enum):
    r"""Labels for the ``Route`` that are useful to identify specific
    properties of the route to compare against others.

    Values:
        ROUTE_LABEL_UNSPECIFIED (0):
            Default - not used.
        DEFAULT_ROUTE (1):
            The default "best" route returned for the
            route computation.
        DEFAULT_ROUTE_ALTERNATE (2):
            An alternative to the default "best" route. Routes like this
            will be returned when
            ``ComputeRoutesRequest.compute_alternative_routes`` is
            specified.
        FUEL_EFFICIENT (3):
            Fuel efficient route. Routes labeled with
            this value are determined to be optimized for
            Eco parameters such as fuel consumption.
    """
    ROUTE_LABEL_UNSPECIFIED = 0
    DEFAULT_ROUTE = 1
    DEFAULT_ROUTE_ALTERNATE = 2
    FUEL_EFFICIENT = 3


__all__ = tuple(sorted(__protobuf__.manifest))

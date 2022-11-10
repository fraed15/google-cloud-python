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
from google.type import postal_address_pb2  # type: ignore
import proto  # type: ignore

from google.maps.addressvalidation_v1.types import address as gma_address
from google.maps.addressvalidation_v1.types import geocode as gma_geocode
from google.maps.addressvalidation_v1.types import metadata_
from google.maps.addressvalidation_v1.types import usps_data as gma_usps_data

__protobuf__ = proto.module(
    package="google.maps.addressvalidation.v1",
    manifest={
        "ValidateAddressRequest",
        "ValidateAddressResponse",
        "ProvideValidationFeedbackRequest",
        "ProvideValidationFeedbackResponse",
        "ValidationResult",
        "Verdict",
    },
)


class ValidateAddressRequest(proto.Message):
    r"""The request for validating an address.

    Attributes:
        address (google.type.postal_address_pb2.PostalAddress):
            Required. The address being validated. Unformatted addresses
            should be submitted via
            [``address_lines``][google.type.PostalAddress.address_lines].

            The total length of the fields in this input must not exceed
            300 characters.

            Supported regions can be found in the
            `FAQ <https://developers.google.com/maps/documentation/address-validation/faq#which_regions_are_currently_supported>`__.

            The [language_code][google.type.PostalAddress.language_code]
            value in the input address is reserved for future uses and
            is ignored today. The validated address result will be
            populated based on the preferred language for the given
            address, as identified by the system.

            The Address Validation API ignores the values in
            [recipients][google.type.PostalAddress.recipients] and
            [organization][google.type.PostalAddress.organization]. Any
            values in those fields will be discarded and not returned.
            Please do not set them.
        previous_response_id (str):
            This field must be empty for the first address validation
            request. If more requests are necessary to fully validate a
            single address (for example if the changes the user makes
            after the initial validation need to be re-validated), then
            each followup request must populate this field with the
            [response_id][google.maps.addressvalidation.v1.ValidateAddressResponse.response_id]
            from the very first response in the validation sequence.
        enable_usps_cass (bool):
            Enables USPS CASS compatible mode. This affects *only* the
            [google.maps.addressvalidation.v1.ValidationResult.usps_data]
            field of
            [google.maps.addressvalidation.v1.ValidationResult]. Note:
            for USPS CASS enabled requests for addresses in Puerto Rico,
            a [google.type.PostalAddress.region_code] of the ``address``
            must be provided as "PR", or an
            [google.type.PostalAddress.administrative_area] of the
            ``address`` must be provided as "Puerto Rico"
            (case-insensitive) or "PR".

            It's recommended to use a componentized ``address``, or
            alternatively specify at least two
            [google.type.PostalAddress.address_lines] where the first
            line contains the street number and name and the second line
            contains the city, state, and zip code.
    """

    address = proto.Field(
        proto.MESSAGE,
        number=1,
        message=postal_address_pb2.PostalAddress,
    )
    previous_response_id = proto.Field(
        proto.STRING,
        number=2,
    )
    enable_usps_cass = proto.Field(
        proto.BOOL,
        number=3,
    )


class ValidateAddressResponse(proto.Message):
    r"""The response to an address validation request.

    Attributes:
        result (google.maps.addressvalidation_v1.types.ValidationResult):
            The result of the address validation.
        response_id (str):
            The UUID that identifies this response. If the address needs
            to be re-validated, this UUID *must* accompany the new
            request.
    """

    result = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ValidationResult",
    )
    response_id = proto.Field(
        proto.STRING,
        number=2,
    )


class ProvideValidationFeedbackRequest(proto.Message):
    r"""The request for sending validation feedback.

    Attributes:
        conclusion (google.maps.addressvalidation_v1.types.ProvideValidationFeedbackRequest.ValidationConclusion):
            Required. The outcome of the sequence of validation
            attempts.

            If this field is set to
            ``VALIDATION_CONCLUSION_UNSPECIFIED``, an
            ``INVALID_ARGUMENT`` error will be returned.
        response_id (str):
            Required. The ID of the response that this feedback is for.
            This should be the
            [response_id][google.maps.addressvalidation.v1.ValidateAddressRequest.response_id]
            from the first response in a series of address validation
            attempts.
    """

    class ValidationConclusion(proto.Enum):
        r"""The possible final outcomes of the sequence of address
        validation requests needed to validate an address.
        """
        VALIDATION_CONCLUSION_UNSPECIFIED = 0
        VALIDATED_VERSION_USED = 1
        USER_VERSION_USED = 2
        UNVALIDATED_VERSION_USED = 3
        UNUSED = 4

    conclusion = proto.Field(
        proto.ENUM,
        number=1,
        enum=ValidationConclusion,
    )
    response_id = proto.Field(
        proto.STRING,
        number=2,
    )


class ProvideValidationFeedbackResponse(proto.Message):
    r"""The response for validation feedback.
    The response is empty if the feedback is sent successfully.

    """


class ValidationResult(proto.Message):
    r"""The result of validating an address.

    Attributes:
        verdict (google.maps.addressvalidation_v1.types.Verdict):
            Overall verdict flags
        address (google.maps.addressvalidation_v1.types.Address):
            Information about the address itself as
            opposed to the geocode.
        geocode (google.maps.addressvalidation_v1.types.Geocode):
            Information about the location and place that
            the address geocoded to.
        metadata (google.maps.addressvalidation_v1.types.AddressMetadata):
            Other information relevant to deliverability.
        usps_data (google.maps.addressvalidation_v1.types.UspsData):
            Extra deliverability flags provided by USPS. Only provided
            in region ``US`` and ``PR``.
    """

    verdict = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Verdict",
    )
    address = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gma_address.Address,
    )
    geocode = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gma_geocode.Geocode,
    )
    metadata = proto.Field(
        proto.MESSAGE,
        number=4,
        message=metadata_.AddressMetadata,
    )
    usps_data = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gma_usps_data.UspsData,
    )


class Verdict(proto.Message):
    r"""High level overview of the address validation result and
    geocode.

    Attributes:
        input_granularity (google.maps.addressvalidation_v1.types.Verdict.Granularity):
            The granularity of the **input** address. This is the result
            of parsing the input address and does not give any
            validation signals. For validation signals, refer to
            ``validation_granularity`` below.

            For example, if the input address includes a specific
            apartment number, then the ``input_granularity`` here will
            be ``SUB_PREMISE``. If we cannot match the apartment number
            in the databases or the apartment number is invalid, the
            ``validation_granularity`` will likely be ``PREMISE`` or
            below.
        validation_granularity (google.maps.addressvalidation_v1.types.Verdict.Granularity):
            The granularity level that the API can fully **validate**
            the address to. For example, an ``validation_granularity``
            of ``PREMISE`` indicates all address components at the level
            of ``PREMISE`` or more coarse can be validated.

            Per address component validation result can be found in
            [google.maps.addressvalidation.v1.Address.address_components].
        geocode_granularity (google.maps.addressvalidation_v1.types.Verdict.Granularity):
            Information about the granularity of the
            [``geocode``][google.maps.addressvalidation.v1.ValidationResult.geocode].
            This can be understood as the semantic meaning of how coarse
            or fine the geocoded location is.

            This can differ from the ``validation_granularity`` above
            occasionally. For example, our database might record the
            existence of an apartment number but do not have a precise
            location for the apartment within a big apartment complex.
            In that case, the ``validation_granularity`` will be
            ``SUB_PREMISE`` but the ``geocode_granularity`` will be
            ``PREMISE``.
        address_complete (bool):
            The address is considered complete if there are no
            unresolved tokens, no unexpected or missing address
            components. See
            [``missing_component_types``][google.maps.addressvalidation.v1.Address.missing_component_types],
            [``unresolved_tokens``][google.maps.addressvalidation.v1.Address.unresolved_tokens]
            or
            [``unexpected``][google.maps.addressvalidation.v1.AddressComponent.unexpected]
            fields for more details.
        has_unconfirmed_components (bool):
            At least one address component cannot be categorized or
            validated, see
            [google.maps.addressvalidation.v1.Address.address_components]
            for details.
        has_inferred_components (bool):
            At least one address component was inferred (added) that
            wasn't in the input, see
            [google.maps.addressvalidation.v1.Address.address_components]
            for details.
        has_replaced_components (bool):
            At least one address component was replaced, see
            [google.maps.addressvalidation.v1.Address.address_components]
            for details.
    """

    class Granularity(proto.Enum):
        r"""The various granularities that an address or a geocode can have.
        When used to indicate granularity for an *address*, these values
        indicate with how fine a granularity the address identifies a
        mailing destination. For example, an address such as "123 Main
        Street, Redwood City, CA, 94061" identifies a ``PREMISE`` while
        something like "Redwood City, CA, 94061" identifies a ``LOCALITY``.
        However, if we are unable to find a geocode for "123 Main Street" in
        Redwood City, the geocode returned might be of ``LOCALITY``
        granularity even though the address is more granular.
        """
        GRANULARITY_UNSPECIFIED = 0
        SUB_PREMISE = 1
        PREMISE = 2
        PREMISE_PROXIMITY = 3
        BLOCK = 4
        ROUTE = 5
        OTHER = 6

    input_granularity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Granularity,
    )
    validation_granularity = proto.Field(
        proto.ENUM,
        number=2,
        enum=Granularity,
    )
    geocode_granularity = proto.Field(
        proto.ENUM,
        number=3,
        enum=Granularity,
    )
    address_complete = proto.Field(
        proto.BOOL,
        number=4,
    )
    has_unconfirmed_components = proto.Field(
        proto.BOOL,
        number=5,
    )
    has_inferred_components = proto.Field(
        proto.BOOL,
        number=6,
    )
    has_replaced_components = proto.Field(
        proto.BOOL,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

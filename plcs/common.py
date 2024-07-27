from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = (
    "http://standards.iso.org/iso/ts/10303/-3000/-ed-1/tech/xml-schema/common"
)


@dataclass
class BaseObject:
    """
    Base type for all objects.
    """

    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DataContainer:
    """A DataContainer is an abstract generalization of the root element of a data
    file.

    Only non-abstract specializations of the DataContainer can be
    instantiated.
    """


@dataclass
class NameAndAddress:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    address: Optional["NameAndAddress.Address"] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "",
        },
    )

    @dataclass
    class Address:
        address_line: List[str] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
                "namespace": "",
            },
        )


@dataclass
class Reference:
    """
    A reference to a Base Type object within the data file.
    """

    uid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uidRef",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class BaseRootObject(BaseObject):
    """Base type for root elements - objects that can be instantiated inside Container"""


@dataclass
class Header:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Element",
            "namespace": "",
        },
    )
    author: Optional[NameAndAddress] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "",
        },
    )
    organization: Optional[NameAndAddress] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "",
        },
    )
    preprocessor_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreprocessorVersion",
            "type": "Element",
            "namespace": "",
        },
    )
    originating_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginatingSystem",
            "type": "Element",
            "namespace": "",
        },
    )
    authorization: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authorization",
            "type": "Element",
            "namespace": "",
        },
    )
    documentation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Documentation",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Uos:
    """
    Unit of serialization.
    """

    class Meta:
        namespace = "http://standards.iso.org/iso/ts/10303/-3000/-ed-1/tech/xml-schema/common"

    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    data_container: List[DataContainer] = field(
        default_factory=list,
        metadata={
            "name": "DataContainer",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )

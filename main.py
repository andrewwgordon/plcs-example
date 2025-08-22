
"""
main.py

Example entry point for demonstrating the creation and serialization of PLCS (Product Life Cycle Support) data objects.
This script uses the PLCSFactory to build a simple product structure and serializes it to JSON.
"""

from typing import Dict, Tuple
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from org.oasis_open.plcs import *
from plcs_factory import PLCSFactory


def filter_nulls_empty_arrays(x: Tuple) -> Dict:
    """
    Filter function to remove null values and empty arrays from a dictionary.

    Args:
        x (Tuple): Tuple of (key, value) pairs from a dictionary.

    Returns:
        Dict: Dictionary with only non-null and non-empty values.
    """
    return {k: v for k, v in x if v}


# Configure the JSON serializer with pretty-print indentation and custom dict factory
config = SerializerConfig(indent="  ")
context = XmlContext()
serializer = JsonSerializer(dict_factory=filter_nulls_empty_arrays, context=context, config=config)

# Instantiate the PLCSFactory for creating PLCS objects
plcs_factory = PLCSFactory()


# Create a list of property assignments for the part (string and numeric)
property_assignments = [
    plcs_factory.create_string_property_value_assignment("Remark", "This is a remark"),
    plcs_factory.create_numeric_property_value_assignment("Mass", 10.5)
]


# Create a single PartViewDefinition called "As Operated" with the property assignments
part_view_definitions = [
    plcs_factory.create_part_view_definition("As Operated", property_assignments)
]


# Create a single PartVersion (version "1") with the PartViewDefinition
part_versions = [
    plcs_factory.create_part_version("1", part_view_definitions)
]


# Create the Part object with ID, description, versions, and manufacturer reference
part = plcs_factory.create_part(
    "ISO7380-M6x16-A2",  # Part ID
    "Screw, Hexagon Socket Button Head",  # Part description
    part_versions,  # List of part versions
    "Bolts Inc"  # Organisation reference (manufacturer)
)

# Create a PLCS Data Container and assign the part to it
data_container = PlcsDataContainer()
data_container.part = [part]

# Serialize the data container to JSON and print to STDOUT
output = serializer.render(data_container)
print(output)

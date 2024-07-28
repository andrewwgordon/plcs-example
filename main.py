from typing import Dict, Tuple
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from plcs import *
from plcs_factory import PLCSFactory

def filter_nulls_empty_arrays(x: Tuple) -> Dict:
    """
    Function to filter nulls and empty arrays from dictionary

    Parameters:
        x (Tuple): Current tuple of dictionary
    
    Returns:
        Dict: filtered dictionary
    """
    return {k: v for k, v in x if v}

config = SerializerConfig(indent="  ")
context = XmlContext()
serializer = JsonSerializer(dict_factory=filter_nulls_empty_arrays,context=context, config=config)
plcs_factory = PLCSFactory()

# Create a string and numeric PropertyAssignment for the PartDefinition
property_assignments = [
    plcs_factory.create_string_property_value_assignment("Remark","This is a remark"),
    plcs_factory.create_numeric_property_value_assignment("Mass",10.5)
]

# Create a single PartDefinition called "As Operated" with the two PropertyAssignments
part_view_definitions = [
    plcs_factory.create_part_view_definition("As Operated",property_assignments)
]

# Create a single PartVersion 1 with the PartDefinition
part_versions = [
    plcs_factory.create_part_version("1",part_view_definitions)
]

# Create the Part with the PartVersions
part = plcs_factory.create_part("ISO7380-M6x16-A2","Screw, Hexagon Socket Button Head",part_versions,"Bolts Inc")

# Create a PLCS Data Container
data_container = PlcsDataContainer()
# Set the list of Parts of the Data Container to the Part
data_container.part = [part]

# Render to JSON and display to STDOUT
output = serializer.render(data_container)
print(output)

from typing import List
from plcs import *

class PLCSFactory:
    """
    Factory helper to create PLCS objects
 
    Methods
        create_string_property_value_assignment (str, str): Creates a PropertyValueAssignment of a single string value
        create_numeric_property_value_assignment (str, float): Creates a PropertyValueAssignment of a single numeric value
        create_part_view_definition (str, List[PropertyValueAssignment]): Creates a PartViewDefinition with a Description and list of PropertyValueAssignments
        create_part_version (str, List[PartViewDefinition]): Creates a PartVersion with an Id and list of PartViewDefinitions
        create_part(str, str, List[PartVersion]): Creates a Part with an Id,Description and list of PartVersions
    """

    def __create_string_values(self,the_string: str) -> List[PropertyValue]:
        """
        Creates a list of PropertyValues containing a single string entry
 
        Parameters:
            the_string (str): The string value of the property
 
        Returns:
            List[PropertyValue]: A list of property values container a single entry of a string value
        """
        localized_string_value = LocalizedString()
        localized_string_value.value = the_string
        string_value = StringValue()
        string_value.value_component = localized_string_value
        property_values = [string_value]
        return property_values
    
    def __create_numeric_values(self,the_number: float) -> List[PropertyValue]:
        """
        Creates a list of PropertyValues containing a single numeric entry
 
        Parameters:
            the_number (str): The numeric value of the property
 
        Returns:
            List[PropertyValue]: A list of property values container a single entry of a numeric value
        """
        numeric_value = NumericalValue()
        numeric_value.value_component = the_number
        property_values = [numeric_value]
        return property_values
    
    def __create_descriptor(self,the_description: str) -> Descriptor:
        """
        Creates a Descriptor with a single string value entry
 
        Parameters:
            description (str): The single description
 
        Returns:
            Descriptor: A Descriptor containing a single description
        """
        localized_string_description = LocalizedString()
        localized_string_description.value = the_description
        localized_string_descriptions = [localized_string_description]
        descriptor = Descriptor()
        descriptor.localized_string = localized_string_descriptions
        return descriptor
    
    def __create_identifiers(self,id: str) -> List[Identifier]:
        """
        Creates a list of Identifiers with a single Id entry
 
        Parameters:
            id (str): The single id
 
        Returns:
            List[Identifier]: A list of Identifiers with a single id entry
        """
        identifier = Identifier()
        identifier.id = id
        identifiers = [identifier]
        return identifiers

    def create_string_property_value_assignment(self,description: str, value: str) -> PropertyValueAssignment:
        """
        Creates a PropertyValueAssignment with a single string entry
 
        Parameters:
            description (str): The description of the property
            value (str): The value of the property
 
        Returns:
            PropertyValueAssignment: A PropertyValueAssignment with a single string entry
        """
        property_value_assignment = PropertyValueAssignment()
        property_value_assignment.description = self.__create_descriptor(description)
        property_value_assignment.assigned_property_values = self.__create_string_values(value)
        return property_value_assignment

    def create_numeric_property_value_assignment(self,description: str, value: float) -> PropertyValueAssignment:
        """
        Creates a PropertyValueAssignment with a single numeric entry
 
        Parameters:
            description (str): The description of the property
            value (float): The value of the property
 
        Returns:
            PropertyValueAssignment: A PropertyValueAssignment with a single numeric entry
        """
        property_value_assignment = PropertyValueAssignment()
        property_value_assignment.description = self.__create_descriptor(description)
        property_value_assignment.assigned_property_values = self.__create_numeric_values(value)
        return property_value_assignment

    def create_part_view_definition(self,description: str, property_value_assignments: List[PropertyValueAssignment]) -> PartViewDefinition:
        """
        Creates a PartViewDefinition with a single description and list of PropertyValueAssignments
 
        Parameters:
            description (str): The description of the PartViewDefinition
            property_value_assignments (List[PropertyValueAssignment]): The list of PropertyValueAssignments
 
        Returns:
            PartViewDefinition: A PartViewDefinition containing a description and list of PropertyValueAssignments
        """
        part_view_definition = PartViewDefinition()
        part_view_definition.description = self.__create_descriptor(description)
        part_view_definition.property_value_assignment = property_value_assignments
        return part_view_definition
    
    def create_part_version(self,id: str, part_view_definitions: List[PartViewDefinition]) -> PartVersion:
        """
        Creates a Partversion with a single description and list of PartViewDefinitions
 
        Parameters:
            id (str): The id of the PartVersion            
            property_view_definitions (List[PartViewDefinition]): The list of PartViewDefinitions
 
        Returns:
            PartVersion: A PartVersion containing an id and list of PartViewDefinitions
        """
        part_version = PartVersion()
        part_version.id = self.__create_identifiers(id)
        part_version.view_definitions = part_view_definitions
        return part_version

    def create_part(self,id: str, description: str, part_versions: List[PartVersion]) -> Part:
        """
        Creates a Part with a single id, description and list of PartVersions
 
        Parameters:
            id (str): The id of the Part
            description (str): The description of the Part            
            part_versions (List[PartVersion]): The list of PartVersions
 
        Returns:
            Part: A Part containing an id, description and list of PartVersions
        """
        part = Part()
        part.id = self.__create_identifiers(id)
        part.description = self.__create_descriptor(description)
        part.versions = part_versions
        return part

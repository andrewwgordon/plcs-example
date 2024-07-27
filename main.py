from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.converter import Converter, converter,StringConverter

config = SerializerConfig(indent="  ")
context = XmlContext()
serializer = JsonSerializer()
serializer = JsonSerializer(context=context, config=config)

from plcs import *

remark_value = LocalizedString()
remark_value.uid = "1234"
remark_value.lang = "en"
remark_value.value = "This is a remark"
remark_property_value_assignment = PropertyValueAssignment()
remark_property_value_assignment.description = "Remark"
remark_assigned_property_values = []
remark_assigned_property_values.append(remark_value)
remark_property_value_assignment.assigned_property_values = remark_assigned_property_values

my_part_view_definition = PartViewDefinition()
my_part_view_definition.property_value_assignment.append(remark_property_value_assignment)


print(serializer.render(my_part_view_definition))



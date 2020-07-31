# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schemapages.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='schemapages.proto',
  package='SchemaPages',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11schemapages.proto\x12\x0bSchemaPages\"\xf4\x02\n\x07SDOTerm\x12\'\n\x08termType\x18\x01 \x02(\x0e\x32\x15.SchemaPages.TermType\x12\x0b\n\x03uri\x18\x02 \x02(\t\x12\r\n\x05label\x18\x04 \x02(\t\x12\x34\n\x0b\x62readcrumbs\x18\x06 \x03(\x0b\x32\x1f.SchemaPages.SDOTerm.BreadCrumb\x12\x18\n\x10\x61\x63knowledgements\x18\x05 \x03(\t\x12\x0f\n\x07\x63omment\x18\x07 \x02(\t\x12\x13\n\x0b\x65quivalents\x18\x08 \x03(\t\x12\x0f\n\x07pending\x18\t \x02(\x08\x12\x0f\n\x07retired\x18\n \x02(\x08\x12\x0f\n\x07sources\x18\x0b \x03(\t\x12\x0c\n\x04subs\x18\x0c \x03(\t\x12\x0e\n\x06supers\x18\r \x03(\t\x12\x14\n\x0csupersededBy\x18\x0e \x01(\t\x12\x12\n\nsupersedes\x18\x0f \x03(\t\x12\x11\n\ttermStack\x18\x10 \x03(\t\x1a \n\nBreadCrumb\x12\x12\n\nbreadcrumb\x18\x01 \x03(\t\"\x87\x01\n\x07SDOType\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm\x12\x12\n\nproperties\x18\x03 \x03(\t\x12\x15\n\rallProperties\x18\x04 \x03(\t\x12\x17\n\x0f\x65xpectedTypeFor\x18\x05 \x03(\t\"v\n\x0bSDOProperty\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm\x12\x16\n\x0e\x64omainIncludes\x18\x03 \x03(\t\x12\x15\n\rrangeIncludes\x18\x04 \x03(\t\"\x8b\x01\n\x0bSDODataType\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm\x12\x12\n\nproperties\x18\x03 \x03(\t\x12\x15\n\rallProperties\x18\x04 \x03(\t\x12\x17\n\x0f\x65xpectedTypeFor\x18\x05 \x03(\t\"\x8e\x01\n\x0eSDOEnumeration\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm\x12\x12\n\nproperties\x18\x03 \x03(\t\x12\x15\n\rallProperties\x18\x04 \x03(\t\x12\x17\n\x0f\x65xpectedTypeFor\x18\x05 \x03(\t\"j\n\x13SDOEnumerationValue\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm\x12\x19\n\x11\x65numerationParent\x18\x03 \x02(\t\"H\n\x0cSDOReference\x12\n\n\x02id\x18\x01 \x02(\t\x12,\n\x0etermdescriptor\x18\x02 \x03(\x0b\x32\x14.SchemaPages.SDOTerm*f\n\x08TermType\x12\x08\n\x04TYPE\x10\x00\x12\x0c\n\x08PROPERTY\x10\x01\x12\x0c\n\x08\x44\x41TATYPE\x10\x02\x12\x0f\n\x0b\x45NUMERATION\x10\x03\x12\x14\n\x10\x45NUMERATIONVALUE\x10\x04\x12\r\n\tREFERENCE\x10\x05'
)

_TERMTYPE = _descriptor.EnumDescriptor(
  name='TermType',
  full_name='SchemaPages.TermType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROPERTY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATATYPE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUMERATION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENUMERATIONVALUE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REFERENCE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1136,
  serialized_end=1238,
)
_sym_db.RegisterEnumDescriptor(_TERMTYPE)

TermType = enum_type_wrapper.EnumTypeWrapper(_TERMTYPE)
TYPE = 0
PROPERTY = 1
DATATYPE = 2
ENUMERATION = 3
ENUMERATIONVALUE = 4
REFERENCE = 5



_SDOTERM_BREADCRUMB = _descriptor.Descriptor(
  name='BreadCrumb',
  full_name='SchemaPages.SDOTerm.BreadCrumb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='breadcrumb', full_name='SchemaPages.SDOTerm.BreadCrumb.breadcrumb', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=407,
)

_SDOTERM = _descriptor.Descriptor(
  name='SDOTerm',
  full_name='SchemaPages.SDOTerm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='termType', full_name='SchemaPages.SDOTerm.termType', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='SchemaPages.SDOTerm.uri', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='SchemaPages.SDOTerm.label', index=2,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='breadcrumbs', full_name='SchemaPages.SDOTerm.breadcrumbs', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acknowledgements', full_name='SchemaPages.SDOTerm.acknowledgements', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='SchemaPages.SDOTerm.comment', index=5,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='equivalents', full_name='SchemaPages.SDOTerm.equivalents', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending', full_name='SchemaPages.SDOTerm.pending', index=7,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='retired', full_name='SchemaPages.SDOTerm.retired', index=8,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sources', full_name='SchemaPages.SDOTerm.sources', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subs', full_name='SchemaPages.SDOTerm.subs', index=10,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supers', full_name='SchemaPages.SDOTerm.supers', index=11,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supersededBy', full_name='SchemaPages.SDOTerm.supersededBy', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supersedes', full_name='SchemaPages.SDOTerm.supersedes', index=13,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termStack', full_name='SchemaPages.SDOTerm.termStack', index=14,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SDOTERM_BREADCRUMB, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=407,
)


_SDOTYPE = _descriptor.Descriptor(
  name='SDOType',
  full_name='SchemaPages.SDOType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDOType.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDOType.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='SchemaPages.SDOType.properties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allProperties', full_name='SchemaPages.SDOType.allProperties', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expectedTypeFor', full_name='SchemaPages.SDOType.expectedTypeFor', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=545,
)


_SDOPROPERTY = _descriptor.Descriptor(
  name='SDOProperty',
  full_name='SchemaPages.SDOProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDOProperty.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDOProperty.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domainIncludes', full_name='SchemaPages.SDOProperty.domainIncludes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rangeIncludes', full_name='SchemaPages.SDOProperty.rangeIncludes', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=665,
)


_SDODATATYPE = _descriptor.Descriptor(
  name='SDODataType',
  full_name='SchemaPages.SDODataType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDODataType.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDODataType.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='SchemaPages.SDODataType.properties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allProperties', full_name='SchemaPages.SDODataType.allProperties', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expectedTypeFor', full_name='SchemaPages.SDODataType.expectedTypeFor', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=807,
)


_SDOENUMERATION = _descriptor.Descriptor(
  name='SDOEnumeration',
  full_name='SchemaPages.SDOEnumeration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDOEnumeration.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDOEnumeration.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='SchemaPages.SDOEnumeration.properties', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allProperties', full_name='SchemaPages.SDOEnumeration.allProperties', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expectedTypeFor', full_name='SchemaPages.SDOEnumeration.expectedTypeFor', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=952,
)


_SDOENUMERATIONVALUE = _descriptor.Descriptor(
  name='SDOEnumerationValue',
  full_name='SchemaPages.SDOEnumerationValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDOEnumerationValue.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDOEnumerationValue.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enumerationParent', full_name='SchemaPages.SDOEnumerationValue.enumerationParent', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=1060,
)


_SDOREFERENCE = _descriptor.Descriptor(
  name='SDOReference',
  full_name='SchemaPages.SDOReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchemaPages.SDOReference.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='termdescriptor', full_name='SchemaPages.SDOReference.termdescriptor', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1062,
  serialized_end=1134,
)

_SDOTERM_BREADCRUMB.containing_type = _SDOTERM
_SDOTERM.fields_by_name['termType'].enum_type = _TERMTYPE
_SDOTERM.fields_by_name['breadcrumbs'].message_type = _SDOTERM_BREADCRUMB
_SDOTYPE.fields_by_name['termdescriptor'].message_type = _SDOTERM
_SDOPROPERTY.fields_by_name['termdescriptor'].message_type = _SDOTERM
_SDODATATYPE.fields_by_name['termdescriptor'].message_type = _SDOTERM
_SDOENUMERATION.fields_by_name['termdescriptor'].message_type = _SDOTERM
_SDOENUMERATIONVALUE.fields_by_name['termdescriptor'].message_type = _SDOTERM
_SDOREFERENCE.fields_by_name['termdescriptor'].message_type = _SDOTERM
DESCRIPTOR.message_types_by_name['SDOTerm'] = _SDOTERM
DESCRIPTOR.message_types_by_name['SDOType'] = _SDOTYPE
DESCRIPTOR.message_types_by_name['SDOProperty'] = _SDOPROPERTY
DESCRIPTOR.message_types_by_name['SDODataType'] = _SDODATATYPE
DESCRIPTOR.message_types_by_name['SDOEnumeration'] = _SDOENUMERATION
DESCRIPTOR.message_types_by_name['SDOEnumerationValue'] = _SDOENUMERATIONVALUE
DESCRIPTOR.message_types_by_name['SDOReference'] = _SDOREFERENCE
DESCRIPTOR.enum_types_by_name['TermType'] = _TERMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SDOTerm = _reflection.GeneratedProtocolMessageType('SDOTerm', (_message.Message,), {

  'BreadCrumb' : _reflection.GeneratedProtocolMessageType('BreadCrumb', (_message.Message,), {
    'DESCRIPTOR' : _SDOTERM_BREADCRUMB,
    '__module__' : 'schemapages_pb2'
    # @@protoc_insertion_point(class_scope:SchemaPages.SDOTerm.BreadCrumb)
    })
  ,
  'DESCRIPTOR' : _SDOTERM,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOTerm)
  })
_sym_db.RegisterMessage(SDOTerm)
_sym_db.RegisterMessage(SDOTerm.BreadCrumb)

SDOType = _reflection.GeneratedProtocolMessageType('SDOType', (_message.Message,), {
  'DESCRIPTOR' : _SDOTYPE,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOType)
  })
_sym_db.RegisterMessage(SDOType)

SDOProperty = _reflection.GeneratedProtocolMessageType('SDOProperty', (_message.Message,), {
  'DESCRIPTOR' : _SDOPROPERTY,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOProperty)
  })
_sym_db.RegisterMessage(SDOProperty)

SDODataType = _reflection.GeneratedProtocolMessageType('SDODataType', (_message.Message,), {
  'DESCRIPTOR' : _SDODATATYPE,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDODataType)
  })
_sym_db.RegisterMessage(SDODataType)

SDOEnumeration = _reflection.GeneratedProtocolMessageType('SDOEnumeration', (_message.Message,), {
  'DESCRIPTOR' : _SDOENUMERATION,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOEnumeration)
  })
_sym_db.RegisterMessage(SDOEnumeration)

SDOEnumerationValue = _reflection.GeneratedProtocolMessageType('SDOEnumerationValue', (_message.Message,), {
  'DESCRIPTOR' : _SDOENUMERATIONVALUE,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOEnumerationValue)
  })
_sym_db.RegisterMessage(SDOEnumerationValue)

SDOReference = _reflection.GeneratedProtocolMessageType('SDOReference', (_message.Message,), {
  'DESCRIPTOR' : _SDOREFERENCE,
  '__module__' : 'schemapages_pb2'
  # @@protoc_insertion_point(class_scope:SchemaPages.SDOReference)
  })
_sym_db.RegisterMessage(SDOReference)


# @@protoc_insertion_point(module_scope)

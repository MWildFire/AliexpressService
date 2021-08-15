# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"-\n\rSearchRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0f\n\x07proxies\x18\x02 \x03(\t\"f\n\x0cResponseItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\x12\x0e\n\x06rating\x18\x05 \x01(\t\x12\r\n\x05query\x18\x06 \x01(\t\"D\n\x14SearchResponseStream\x12\r\n\x05query\x18\x01 \x01(\t\x12\x1d\n\x06result\x18\x02 \x03(\x0b\x32\r.ResponseItem2D\n\rSearchService\x12\x33\n\x06Search\x12\x0e.SearchRequest\x1a\x15.SearchResponseStream(\x01\x30\x01\x62\x06proto3'
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='SearchRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxies', full_name='SearchRequest.proxies', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=62,
)


_RESPONSEITEM = _descriptor.Descriptor(
  name='ResponseItem',
  full_name='ResponseItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='ResponseItem.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='ResponseItem.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='ResponseItem.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='ResponseItem.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rating', full_name='ResponseItem.rating', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='ResponseItem.query', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=166,
)


_SEARCHRESPONSESTREAM = _descriptor.Descriptor(
  name='SearchResponseStream',
  full_name='SearchResponseStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='SearchResponseStream.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='SearchResponseStream.result', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=236,
)

_SEARCHRESPONSESTREAM.fields_by_name['result'].message_type = _RESPONSEITEM
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['ResponseItem'] = _RESPONSEITEM
DESCRIPTOR.message_types_by_name['SearchResponseStream'] = _SEARCHRESPONSESTREAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

ResponseItem = _reflection.GeneratedProtocolMessageType('ResponseItem', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEITEM,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ResponseItem)
  })
_sym_db.RegisterMessage(ResponseItem)

SearchResponseStream = _reflection.GeneratedProtocolMessageType('SearchResponseStream', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSESTREAM,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponseStream)
  })
_sym_db.RegisterMessage(SearchResponseStream)



_SEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='SearchService',
  full_name='SearchService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=238,
  serialized_end=306,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='SearchService.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESPONSESTREAM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHSERVICE)

DESCRIPTOR.services_by_name['SearchService'] = _SEARCHSERVICE

# @@protoc_insertion_point(module_scope)
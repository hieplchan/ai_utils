# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imageprocess.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='imageprocess.proto',
  package='imageprocess',
  syntax='proto3',
  serialized_options=b'\n\035io.grpc.examples.imageprocessB\021ImageProcessProtoP\001\242\002\003IMG',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12imageprocess.proto\x12\x0cimageprocess\"8\n\x14ImageProcessResquest\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"\'\n\x14ImageProcessResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2h\n\x0cImageProcess\x12X\n\x0cProcessImage\x12\".imageprocess.ImageProcessResquest\x1a\".imageprocess.ImageProcessResponse\"\x00\x42:\n\x1dio.grpc.examples.imageprocessB\x11ImageProcessProtoP\x01\xa2\x02\x03IMGb\x06proto3'
)




_IMAGEPROCESSRESQUEST = _descriptor.Descriptor(
  name='ImageProcessResquest',
  full_name='imageprocess.ImageProcessResquest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='imageprocess.ImageProcessResquest.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='imageprocess.ImageProcessResquest.image', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=36,
  serialized_end=92,
)


_IMAGEPROCESSRESPONSE = _descriptor.Descriptor(
  name='ImageProcessResponse',
  full_name='imageprocess.ImageProcessResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='imageprocess.ImageProcessResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=94,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['ImageProcessResquest'] = _IMAGEPROCESSRESQUEST
DESCRIPTOR.message_types_by_name['ImageProcessResponse'] = _IMAGEPROCESSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageProcessResquest = _reflection.GeneratedProtocolMessageType('ImageProcessResquest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPROCESSRESQUEST,
  '__module__' : 'imageprocess_pb2'
  # @@protoc_insertion_point(class_scope:imageprocess.ImageProcessResquest)
  })
_sym_db.RegisterMessage(ImageProcessResquest)

ImageProcessResponse = _reflection.GeneratedProtocolMessageType('ImageProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEPROCESSRESPONSE,
  '__module__' : 'imageprocess_pb2'
  # @@protoc_insertion_point(class_scope:imageprocess.ImageProcessResponse)
  })
_sym_db.RegisterMessage(ImageProcessResponse)


DESCRIPTOR._options = None

_IMAGEPROCESS = _descriptor.ServiceDescriptor(
  name='ImageProcess',
  full_name='imageprocess.ImageProcess',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=135,
  serialized_end=239,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessImage',
    full_name='imageprocess.ImageProcess.ProcessImage',
    index=0,
    containing_service=None,
    input_type=_IMAGEPROCESSRESQUEST,
    output_type=_IMAGEPROCESSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGEPROCESS)

DESCRIPTOR.services_by_name['ImageProcess'] = _IMAGEPROCESS

# @@protoc_insertion_point(module_scope)
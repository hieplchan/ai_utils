# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import imageprocess_pb2 as imageprocess__pb2


class ImageProcessStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessImage = channel.unary_unary(
                '/imageprocess.ImageProcess/ProcessImage',
                request_serializer=imageprocess__pb2.ImageProcessResquest.SerializeToString,
                response_deserializer=imageprocess__pb2.ImageProcessResponse.FromString,
                )


class ImageProcessServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageProcessServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessImage': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessImage,
                    request_deserializer=imageprocess__pb2.ImageProcessResquest.FromString,
                    response_serializer=imageprocess__pb2.ImageProcessResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'imageprocess.ImageProcess', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageProcess(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/imageprocess.ImageProcess/ProcessImage',
            imageprocess__pb2.ImageProcessResquest.SerializeToString,
            imageprocess__pb2.ImageProcessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
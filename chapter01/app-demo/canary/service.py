from canary.canary_pb2 import Request, Response
from canary.canary_pb2_grpc import CanaryServiceServicer


class NormalService(CanaryServiceServicer):

    def add(self, request: Request, context) -> Response:
        """
        context.set_code(500)
        context.set_details("ERROR SERVICE")
        return Response()
        """

        return Response(
            code=200,
            message='Normal Word'
        )


class GrayService(CanaryServiceServicer):
    def add(self, request: Request, context) -> Response:
        return Response(
            code=200,
            message='Gray Word'
        )

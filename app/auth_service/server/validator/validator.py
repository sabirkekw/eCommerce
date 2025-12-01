import grpc
from concurrent import futures
from app.protos.auth import auth_pb2, auth_pb2_grpc
from app.auth_service.service.validator import ValidatorService

class Validator(auth_pb2_grpc.ValidatorServicer):
    async def validate(self, request, context):
        is_valid = await ValidatorService.validate(request)
        return auth_pb2.ValidatorResponse(is_valid = is_valid)
import grpc
from concurrent import futures
from app.protos.auth import auth_pb2, auth_pb2_grpc
from app.auth_service.service.auth import AuthService

class Auth(auth_pb2_grpc.AuthServicer):
    async def register(self, request, context):
        id = await AuthService.register(request)
        return auth_pb2.RegisterReply(id = id)
    
    async def login(self, request, context):
        token = await AuthService.login(request)
        return auth_pb2.LoginReply(token = token)
    
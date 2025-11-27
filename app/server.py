import grpc
from concurrent import futures
from protos import pingpong_pb2_grpc
from protos import pingpong_pb2

class Ping(pingpong_pb2_grpc.PingPongerServicer):
    def Ping(self,request,context):
        return pingpong_pb2.PongReply(text = 'Pong')
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pingpong_pb2_grpc.add_PingPongerServicer_to_server(
        Ping(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
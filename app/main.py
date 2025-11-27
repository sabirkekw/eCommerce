import grpc
from protos import pingpong_pb2, pingpong_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pingpong_pb2_grpc.PingPongerStub(channel)
        response = stub.Ping(pingpong_pb2.PingRequest(text='Ping'))
        print(response.text)

if __name__ == "__main__":
    run()
import grpc
import streaming_sum_pb2 as streaming_pb2
import streaming_sum_pb2_grpc as streaming_pb2_grpc
from concurrent import futures

# Implement Calculator service with client streaming
class CalculatorServicer(streaming_pb2_grpc.CalculatorServicer):
    def SumStream(self, request_iterator, context):
        total = 0
        for request in request_iterator:  # Process incoming stream of numbers
            print(f"Received: {request.number}")
            total += request.number
        return streaming_pb2.SumResponse(result=total)  # Return the sum

# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


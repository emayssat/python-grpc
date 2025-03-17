import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures

# Implement Calculator service
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)

    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.MultiplyResponse(result=result)

# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


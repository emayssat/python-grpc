import grpc
import streaming_sum_pb2 as streaming_pb2
import streaming_sum_pb2_grpc as streaming_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = streaming_pb2_grpc.CalculatorStub(channel)

# Function to generate a stream of numbers
def generate_numbers():
    for num in [10, 20, 30, 40, 50]:  # Sending a stream of numbers
        print(f"Sending: {num}")
        yield streaming_pb2.SumRequest(number=num)

# Call the SumStream RPC with streaming input
response = stub.SumStream(generate_numbers())
print(f"Final Sum: {response.result}")


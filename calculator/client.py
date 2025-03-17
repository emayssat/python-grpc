import grpc
import calculator_pb2
import calculator_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Call the Add function
add_request = calculator_pb2.AddRequest(num1=5, num2=7)
add_response = stub.Add(add_request)
print(f"Addition Result: {add_response.result}")

# Call the Multiply function
multiply_request = calculator_pb2.MultiplyRequest(num1=5, num2=7)
multiply_response = stub.Multiply(multiply_request)
print(f"Multiplication Result: {multiply_response.result}")


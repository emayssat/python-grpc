import grpc
import stock_chat_pb2
import stock_chat_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = stock_chat_pb2_grpc.StockChatStub(channel)

# Generator function to send stock tickers to the server
def send_tickers():
    while True:
        ticker = input("Enter stock ticker (or type 'exit' to quit): ").upper()
        if ticker == "EXIT":
            break
        yield stock_chat_pb2.StockRequest(ticker=ticker)

# Receive real-time responses from the server
responses = stub.Chat(send_tickers())

# Process the server responses in real-time
for response in responses:
    print(f"{response.timestamp} - {response.message}")


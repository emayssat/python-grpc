import grpc
import stock_chat_pb2
import stock_chat_pb2_grpc
from concurrent import futures
import time
import random
from datetime import datetime

# Implement StockChat service with bidirectional streaming
class StockChatServicer(stock_chat_pb2_grpc.StockChatServicer):
    def Chat(self, request_iterator, context):
        for request in request_iterator:  # Receive client requests in a stream
            ticker = request.ticker.upper()
            price = round(random.uniform(100, 500), 2)  # Simulated stock price
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            response_message = f"Current price for {ticker} is ${price}"
            print(f"Received request: {ticker} | Responding: {response_message}")

            yield stock_chat_pb2.StockResponse(
                ticker=ticker, price=price, message=response_message, timestamp=timestamp
            )
            time.sleep(1)  # Simulate real-time updates

# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_chat_pb2_grpc.add_StockChatServicer_to_server(StockChatServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Stock Trading Chat Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


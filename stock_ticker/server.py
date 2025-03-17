import grpc
import stock_pb2
import stock_pb2_grpc
from concurrent import futures
import time
import random
from datetime import datetime

# Implement StockService with server streaming
class StockServiceServicer(stock_pb2_grpc.StockServiceServicer):
    def GetStockPrices(self, request, context):
        ticker = request.ticker.upper()
        print(f"Client subscribed to {ticker} stock updates")

        while True:  # Infinite loop to simulate real-time updates
            price = round(random.uniform(100, 500), 2)  # Simulate price change
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"Sending {ticker} price: ${price} at {timestamp}")
            yield stock_pb2.StockResponse(ticker=ticker, price=price, timestamp=timestamp)

            time.sleep(1)  # Simulate real-time stock updates

# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_pb2_grpc.add_StockServiceServicer_to_server(StockServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Stock Price Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


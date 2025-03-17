import grpc
import stock_pb2
import stock_pb2_grpc

# Connect to the gRPC server
channel = grpc.insecure_channel('localhost:50051')
stub = stock_pb2_grpc.StockServiceStub(channel)

# Ask user for stock ticker symbol
ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA, GOOGL): ").upper()

# Request stock price updates
request = stock_pb2.StockRequest(ticker=ticker)
responses = stub.GetStockPrices(request)

# Process the streamed stock prices
for response in responses:
    print(f"{response.timestamp} - {response.ticker}: ${response.price}")


# python-grpc

Simple
 * calculator

Client streaming
 * sum_streaming: 
    * client sends multiple requests and the server receives and sum the numbers
    * the server sends its reply when the client closes the stream

Streaming server
 * stock_tickers
    * start server and wait for a client to request a stream
    * the client receives the stream of stock updates for the selected company

Bidirectional:
 * stock chat
    * start server and wait for client to connect to stream
    * client connects and receive the requested stack price
    * connection stays open and the client can request for another company's stock price
    * once the new ticker is entered the value is send over the same channels/streams

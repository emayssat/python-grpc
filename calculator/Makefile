PROJECT_NAME?= calculator

SERVICE_PROTOBUF_FILENAME?= $(PROJECT_NAME).proto
PROTOBUF_SERIALIATION_FILENAME?= $(PROJECT_NAME)_pb2.py
SERVICE_DEFINITION_FILENAME?= $(PROJECT_NAME)_pb2_grpc.py

build_modules:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. $(SERVICE_PROTOBUF_FILENAME)

distclean:
	rm -rf __pycache__
	rm -rf $(PROTOBUF_SERIALIATION_FILENAME)
	rm -rf $(SERVICE_DEFINITION_FILENAME)

start_server: build_modules
	python server.py

run_client: build_modules
	python client.py




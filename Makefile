proto_auth: 
	python3 -m grpc_tools.protoc \
				--proto_path=. \
				--python_out=. \
				--grpc_python_out=. \
				app/protos/auth/auth.proto
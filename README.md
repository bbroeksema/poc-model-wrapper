# Challenge

Design a proto file and implement the python code to provide a gRPC interface
for the model.predict function.

Restrictions:
* The model.predict function is guiding, this interface cannot be changed
* The protobuf spec should support any dataframe. I.e. number of columns and types in column can vary for input and output.

Pointers:
* https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/schema.proto
* https://github.com/telamonian/numpy-protobuf/blob/master/protobuf/npbuf/type/ndarray.proto
* https://github.com/SeldonIO/seldon-core/blob/master/proto/prediction.proto

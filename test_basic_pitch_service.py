import sys
import grpc

# import the generated classes
import service.service_spec.basic_pitch_service_pb2_grpc as grpc_bp_grpc
import service.service_spec.basic_pitch_service_pb2 as grpc_bp_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Basic Pitch Service
        endpoint = input("Endpoint (localhost:{}): ".format(registry["basic_pitch_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["basic_pitch_service"]["grpc"])

        audio_file_path = input("Audio file path: ") if not test_flag else NEXT
        audio_file = NEXT

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))
        stub = grpc_bp_grpc.CalculatorStub(channel)
        audio_file = grpc_bp_pb2.Input(audio_file=audio_file)

        output = stub.audio2midi(audio_file)
        print(output.midi_file)

    except Exception as e:
        print(e)
        exit(1)

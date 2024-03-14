from ultralytics import YOLO

model = YOLO('best.pt')  # load a custom trained model

model.export(format='engine')

# import torch
# import onnx
# import tensorrt as trt

# onnx_model = 'artag.onnx'

# #output_names=['output'], opset_version=11)
# onnx_model = onnx.load(onnx_model)

# logger = trt.Logger(trt.Logger.ERROR)
# builder = trt.Builder(logger)

# EXPLICIT_BATCH = 1 << (int)(
#     trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
# network = builder.create_network(EXPLICIT_BATCH)

# parser = trt.OnnxParser(network, logger)

# if not parser.parse(onnx_model.SerializeToString()):
#     error_msgs = ''
#     for error in range(parser.num_errors):
#         error_msgs += f'{parser.get_error(error)}\n'
#     raise RuntimeError(f'Failed to parse onnx, {error_msgs}')

# config = builder.create_builder_config()
# config.max_workspace_size = 1<<20
# profile = builder.create_optimization_profile()

# profile.set_shape('input', [1, 1, 1440, 1440], [1, 1, 1440, 1440], [1, 1, 1440, 1440])
# config.add_optimization_profile(profile)

# engine = builder.build_engine(network, config)

# with open('artag.engine', mode='wb') as f:
#     f.write(bytearray(engine.serialize()))
#     print("generating file done!")
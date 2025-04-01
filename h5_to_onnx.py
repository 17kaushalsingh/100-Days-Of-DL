import tensorflow as tf
import tf2onnx

# Load the Keras model
model = tf.keras.models.load_model(r"CustomerChurnRatio/model.h5")

# Convert to ONNX
onnx_model, _ = tf2onnx.convert.from_keras(model)

# Save ONNX model
with open(r"CustomerChurnRatio/model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Conversion successful! Model saved as model.onnx")

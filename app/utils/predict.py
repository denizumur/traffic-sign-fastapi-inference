import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io

# Sınıf açıklamaları
class_labels = {
    0: 'Speed limit (20km/h)', 1: 'Speed limit (30km/h)', 2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)', 4: 'Speed limit (70km/h)', 5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)', 7: 'Speed limit (100km/h)', 8: 'Speed limit (120km/h)',
    9: 'No passing', 10: 'No passing veh over 3.5 tons', 11: 'Right-of-way at intersection',
    12: 'Priority road', 13: 'Yield', 14: 'Stop', 15: 'No vehicles', 16: 'Veh > 3.5 tons prohibited',
    17: 'No entry', 18: 'General caution', 19: 'Dangerous curve left', 20: 'Dangerous curve right',
    21: 'Double curve', 22: 'Bumpy road', 23: 'Slippery road', 24: 'Road narrows on the right',
    25: 'Road work', 26: 'Traffic signals', 27: 'Pedestrians', 28: 'Children crossing',
    29: 'Bicycles crossing', 30: 'Beware of ice/snow', 31: 'Wild animals crossing',
    32: 'End speed + passing limits', 33: 'Turn right ahead', 34: 'Turn left ahead',
    35: 'Ahead only', 36: 'Go straight or right', 37: 'Go straight or left', 38: 'Keep right',
    39: 'Keep left', 40: 'Roundabout mandatory', 41: 'End of no passing', 42: 'End no passing veh > 3.5 tons'
}

# Modeli belleğe yükle (sadece bir kez)
model = load_model("app/model/traffic_sign_model.keras")

def load_model_and_predict(image_bytes):
    try:
        # Görseli yükle ve boyutlandır
        image = Image.open(io.BytesIO(image_bytes)).resize((50, 50)).convert("RGB")
        img_array = np.expand_dims(np.array(image) / 255.0, axis=0)

        # Tahmin yap
        predictions = model.predict(img_array)
        class_id = int(np.argmax(predictions))
        probability = float(np.max(predictions))

        return {
            "class_id": class_id,
            "label": class_labels[class_id],
            "confidence": f"{probability*100:.2f}%"
        }
    except Exception as e:
        return {"error": str(e)}

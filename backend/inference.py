import json
import logging
from PIL import Image

try:
    import torch
    import torchvision.transforms as transforms
    TORCH_AVAILABLE = True
except Exception:
    torch = None
    transforms = None
    TORCH_AVAILABLE = False
    logging.warning("torch not available; inference will return placeholder")

if TORCH_AVAILABLE:
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

try:
    with open("class.json") as f:
        CLASS_MAP = json.load(f)
except Exception:
    CLASS_MAP = {}


def predict(model, image: Image.Image):
    if not TORCH_AVAILABLE or model is None:
        return {"error": "inference unavailable (torch or model missing)"}

    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)
        probs = torch.softmax(outputs, dim=1)[0]

    conf, idx = torch.max(probs, 0)

    return {
        "class_id": int(idx),
        "class_name": CLASS_MAP.get(str(int(idx)), "unknown"),
        "confidence": round(float(conf), 4)
    }

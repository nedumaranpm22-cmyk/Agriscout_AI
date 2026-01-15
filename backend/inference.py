import json
import torch
import torchvision.transforms as transforms
from PIL import Image
from model_loader import load_model

# Load model ONCE
MODEL = load_model("mobilenetv3_epoch1.pth")

with open("class.json") as f:
    CLASS_MAP = json.load(f)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image: Image.Image):
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = MODEL(image)
        probs = torch.softmax(outputs, dim=1)[0]

    conf, idx = torch.max(probs, 0)

    return {
        "class_name": CLASS_MAP.get(str(int(idx)), "unknown"),
        "confidence": round(float(conf), 4)
    }

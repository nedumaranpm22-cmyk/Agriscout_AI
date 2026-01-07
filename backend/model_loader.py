import os
import logging

try:
    import torch
    from torchvision import models
except Exception:
    torch = None
    models = None
    logging.warning("torch/torchvision not available in this environment")


def load_model(model_path, num_classes=18):
    """Loads MobileNetV3 model if torch is available; otherwise returns None."""

    if torch is None or models is None:
        logging.warning("load_model: torch or torchvision unavailable, returning None")
        return None

    # Get absolute path of the backend folder
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, model_path)

    # Create model
    model = models.mobilenet_v3_small(weights=None)

    # Replace classifier for 18 classes
    model.classifier[3] = torch.nn.Linear(
        model.classifier[3].in_features,
        num_classes
    )

    # Load trained weights
    state_dict = torch.load(full_path, map_location="cpu")
    model.load_state_dict(state_dict, strict=False)

    # Set evaluation mode
    model.eval()

    return model

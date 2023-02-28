from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image


model_id = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_id)
model = ViTForImageClassification.from_pretrained(model_id)


def predict(image: Image) -> str:
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]

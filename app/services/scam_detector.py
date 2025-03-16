from transformers import pipeline
import torch
from app.config import Config

class ScamDetector:
    """Uses Hugging Face model to classify scam messages."""
    def __init__(self):
        self.model_name = Config.HUGGINGFACE_MODEL
        self.classifier = pipeline("text-classification", 
                                 model=self.model_name,
                                 device=0 if torch.cuda.is_available() else -1)

    def classify(self, text):
        result = self.classifier(text)[0]
        return {
            "is_scam": result["label"] == "LABEL_1",
            "confidence": result["score"]
        }

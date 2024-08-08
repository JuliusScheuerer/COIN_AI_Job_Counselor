from fastapi import FastAPI, Request
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

app = FastAPI()

# Ensure the model is correctly loaded
model_path = "model/distilbert-finetuned-four-v4"
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

# Mapping from indices to job labels
label_mapping = {0: 'Athlete', 1: 'Teacher', 2: 'Construction Worker', 3: 'Lawyer'}

@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    inputs = tokenizer(data['text'], return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    predicted_label = label_mapping[int(predictions.item())]
    return {"prediction": predicted_label}

# Run the app using the following command in the terminal:
# uvicorn main:app --reload

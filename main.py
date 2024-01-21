from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from transformers import DistilBertModel, AutoTokenizer
from contextlib import asynccontextmanager, contextmanager

import __main__

class DistilBERTClass(torch.nn.Module):
    def __init__(self):
        super(DistilBERTClass, self).__init__()
        self.l1 = DistilBertModel.from_pretrained("distilbert-base-uncased")
        self.pre_classifier = torch.nn.Linear(768, 768)
        self.dropout = torch.nn.Dropout(0.1)
        self.classifier = torch.nn.Linear(768, 2)

    def forward(self, input_ids, attention_mask, token_type_ids):
        output_1 = self.l1(input_ids=input_ids, attention_mask=attention_mask)
        hidden_state = output_1[0]
        pooler = hidden_state[:, 0]
        pooler = self.pre_classifier(pooler)
        pooler = torch.nn.Tanh()(pooler)
        pooler = self.dropout(pooler)
        output = self.classifier(pooler)
        return output

setattr(__main__, "DistilBERTClass", DistilBERTClass)


# Load the tokenizer and model
# @contextmanager
# def load_model(app: FastAPI):
#     # Create an instance of the custom model
#     model = DistilBERTClass()
#     # # Load the model weights
#     state_dict = torch.load('./model/pytorch_model.bin', map_location=torch.device('cpu'))
#     state_dict = state_dict.state_dict()
#     model.load_state_dict(state_dict, strict=False)



def judge_text(model: any, text: str) -> bool:
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
    tokenized_text = tokenizer(text, return_tensors="pt")
    token_type_ids = torch.zeros_like(tokenized_text['input_ids'])
    with torch.no_grad():
        model_output = model(input_ids=tokenized_text['input_ids'], 
                             attention_mask=tokenized_text['attention_mask'], 
                             token_type_ids=token_type_ids)
    return (model_output[0][0] <= 1).item()

# app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class TextRequest(BaseModel):
    text: str

# Define the prediction endpoint
@app.post("/predict")
async def predict(req: TextRequest):
    model = DistilBERTClass()
    # # Load the model weights
    state_dict = torch.load('./model/pytorch_model.bin', map_location=torch.device('cpu'))
    state_dict = state_dict.state_dict()
    model.load_state_dict(state_dict, strict=False)
    probability = judge_text(model, req.text)
    return {"probability": probability}





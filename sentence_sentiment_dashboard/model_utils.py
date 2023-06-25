"""utils for rest dashboard"""

import numpy as np
from scipy.special import softmax

from transformers import AutoTokenizer, AutoConfig
from transformers import AutoModelForSequenceClassification

MODEL_PATH = "cardiffnlp/twitter-roberta-base-sentiment-latest"
MODEL = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)


def get_tokenizer():
    """tokenizer function"""

    tokenize = AutoTokenizer.from_pretrained(MODEL_PATH)
    return tokenize


def get_configuration():
    """configuration function"""

    config = AutoConfig.from_pretrained(MODEL_PATH)
    return config


def prediction_pipeline(text: str) -> dict:
    """return the predictions"""

    sentiment_scores = []
    labels = []

    tokenizer = get_tokenizer()
    config = get_configuration()

    encoded_input = tokenizer(text, return_tensors='pt')
    output = MODEL(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    for i in range(scores.shape[0]):
        labels.append(config.id2label[ranking[i]])
        sentiment_scores.append(scores[ranking[i]])

    return dict(zip(labels, sentiment_scores))

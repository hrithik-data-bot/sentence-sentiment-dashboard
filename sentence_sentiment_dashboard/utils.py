"""utils for rest dashboard"""

import numpy as np
from scipy.special import softmax

from transformers import AutoTokenizer, AutoConfig
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification

MODEL_PATH = "cardiffnlp/twitter-roberta-base-sentiment-latest"
MODEL = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)


def tokenizer():
    """tokenizer function"""

    tokenize = AutoTokenizer.from_pretrained(MODEL_PATH)
    return tokenize


def configuration():
    """configuration function"""

    config = AutoConfig.from_pretrained(MODEL_PATH)
    return config

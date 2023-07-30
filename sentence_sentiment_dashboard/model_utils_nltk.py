"""utils for rest dashboard"""

# pylint: disable=import-error
from nltk.sentiment.vader import SentimentIntensityAnalyzer

ANALYZER = SentimentIntensityAnalyzer()

def prediction_pipeline(text: str) -> dict:
    """return the predictions"""

    predictions = ANALYZER.polarity_scores(text)
    predictions.pop('compound')
    return predictions

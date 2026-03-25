from typing import Optional, List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

classifier = None
vectorizer = None


def train_from_labeled_reviews(reviews: List[dict]) -> bool:
    global classifier, vectorizer
    texts = []
    labels = []

    for item in reviews:
        text = item.get("text")
        label = item.get("label")
        if not text or label is None:
            continue
        texts.append(text)
        labels.append(1 if label in ["fake", "spam", "fraud"] else 0)

    if len(texts) < 10:
        return False

    vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2), stop_words="english")
    X = vectorizer.fit_transform(texts)

    classifier = LogisticRegression(max_iter=450)
    classifier.fit(X, labels)
    return True


def predict_fake_probability(text: str) -> Optional[float]:
    global classifier, vectorizer
    if classifier is None or vectorizer is None:
        return None

    if not text:
        return 0.5

    X = vectorizer.transform([text])
    prob = classifier.predict_proba(X)[0][1]
    return float(prob)

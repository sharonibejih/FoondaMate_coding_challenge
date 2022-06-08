import torch
from nltk.porter import PorterStemmer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pickle

# # load huggingface transformer question-vs-statement classification model
# tokenizer = AutoTokenizer.from_pretrained("shahrukhx01/question-vs-statement-classifier")
# model = AutoModelForSequenceClassification.from_pretrained("shahrukhx01/question-vs-statement-classifier")

# # write the tokenizer, model to file
# file = open("./models/model.shn", "wb")
# pickle.dump((tokenizer, model), file)
# file.close()


def load_pickle(filename: str):
    with open(filename, "rb") as f:
        return pickle.load(f)


def email_classifier(text):
    """
    Tokenizes a given sentence and returns the predicted class. 
    
    Returns:
    LABEL_0 --> sentence is predicted as a statement
    LABEL_1 --> sentence is predicted as a question
    """

    # load huggingface transformer question-vs-statement classification model
    try:
        tokenizer, model = load_pickle("./models/model.shn")

    except:
        print("Model path not found... Loading model directly from source")
        tokenizer = AutoTokenizer.from_pretrained(
            "shahrukhx01/question-vs-statement-classifier")
        model = AutoModelForSequenceClassification.from_pretrained(
            "shahrukhx01/question-vs-statement-classifier")

    inputs = tokenizer(f"{text}", return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    return model.config.id2label[predicted_class_id]


def filter(text):

    # initialize the PorterStemmer class
    ps = PorterStemmer()
    stems = []

    # preprocess sentence: split into words and get the stem of each word.
    for w in text.split():
        stems.append(ps.stem(w))

    # sentence is classified only if "share" and "email" are found in it.
    if "share" in stems and "email" in stems:
        output = email_classifier(text)
        if output == "LABEL_1":
            return "<tag> Student wants to know if can share"

        else:
            return "<tag> Student has shared"

    else:
        return f"'share' and 'email' not found in given sentence: {text}."


if __name__ == "__main__":
    text = str(input("Enter sentence: "))  # get sentence
    print(filter(text))

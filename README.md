# FoondaMate ML Engineer Coding Challenge-001

The goal of this challange is to develop a Python programme that filters emails having a stem “share” and the word “email” and labels them as either “Student wants to know if can share” or “Student has shared”.

Examples of such emails are unpunctuated one liners like: <br>
1. "Can I share your email" <br>
2. "I will share your email" <br>
3. "I shall share your email" <br>
4. "I've shared your email" <br>
5. "May I share your email" <br><br>

Emails containing:
- Questions are tagged as: “Student wants to know if can share”
- Statements are tagged as: “Student has shared”.


## Approach:
- Any given sentence is split into words.
- [PorterStemmer](https://github.com/sharonibejih/FoondaMate_coding_challenge/blob/master/src/nltk/porter.py) is used to get the stem of these words.
- The program checks if "share" and "email" exists in these stems.
- If it does, the [model](https://github.com/sharonibejih/FoondaMate_coding_challenge/blob/master/models/model.shn) is employed to classify the unpunctuated sentence to either a question (investigation) or statement (information). The predicted class determine the tag the sentence will be filtered with.
- If, however, the statement does not contain "share" or "email", there will be a return statement saying so.

### Setup:
- Clone this repo
- Create a virtual environment: `python3 -m venv .project-env`
- Activate virtual environment: `source .project-env/bin/activate`
- Ensure you are in the project folder (<FoondaMate_coding_challenge>) or `cd` to it and install dependencies: <br>
`pip install -r requirements.txt`

### Run Program
In your terminal, and still in <FoondaMate_coding_challenge>, run: `python src/main.py`
- You will be prompted to enter your text. _(Model make take a few seconds to load on the first run.)_
- Ensure the text has participle of 'share' and 'email' otherwise, it will print a different statement. 
<hr>

### Model Source:
[shahrukhx01/question-vs-statement-classifier](https://huggingface.co/shahrukhx01/question-vs-statement-classifier?text=what+did+you+eat+in+lunch%3F) on [Hugging Face](https://huggingface.co/).

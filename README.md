# FoondaMate ML Engineer Coding Challenge-001

Python programme that filters emails having a stem “share” and the word “email” and labels them as either “Student wants to know if can share” or “Student has shared”.

Emails containing:
- Questions are tagged as: “Student wants to know if can share”
- Statements are tagged as: “Student has shared”.

### Setup:
- Clone this repo
- Create a virtual environment: `python3 -m venv .project-env`
- Activate virtual environment: `source .project-env/bin/activate`
- Ensure you are in the project folder (<FoondaMate_coding_challenge>) or `cd` to it and install dependencies: <br>
`pip install -r requirements.txt`

### Run Program
In your terminal, and still in <FoondaMate_coding_challenge>, run: `python src/main.py`
- You will be prompted to enter your text.
- Ensure the text has participle of 'share' and 'email' otherwise, it will print a different statement. 

### Use the Program
To use this function in another python script outside the project (<FoondaMate_coding_challenge>), simply import it: <br>
`>>> from FoondaMate_coding_challenge.src.main import outcome` <br>
`>>> print(filter("Can I share your email"))`

### Model Source:
[shahrukhx01/question-vs-statement-classifier](https://huggingface.co/shahrukhx01/question-vs-statement-classifier?text=what+did+you+eat+in+lunch%3F) on [Hugging Face](https://huggingface.co/).

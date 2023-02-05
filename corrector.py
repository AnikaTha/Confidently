import os
import openai
import pymongo
from pymongo import MongoClient

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

email_unconf = "Dear Bob, I am really sorry to email you so last minute like this. I hope this email finds you well. I am writing to request a meeting to discuss quantum mechanics. I am very unsure about this project and believe that your expertise would be valuable to me and would help me better understand quantum mechanics. I feel that your time is valuable, and I am sorry to bring this up so last minute. I would appreciate any time you could spare for a meeting, either in-person or via video call. Thank you so much for considering my request. I look forward to discussing quantum mechanics with you. Best regards, Veda"
email_conf = "Dear Bob, I hope this email finds you well. I am writing to request a meeting to discuss quantum mechanics. I believe that your expertise would be valuable to me and would help me better understand quantum mechanics. I understand that your time is valuable, and I would appreciate any time you could spare for a meeting, either in-person or via video call. Please let me know your availability and I will arrange accordingly. Thank you for considering my request. I look forward to discussing quantum mechanics with you. Best regards, Veda"


def test_confidence(email):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Is this email confident? yes or no" + "\n" + email,
    temperature=0.21,
    max_tokens=150,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
    )

    return ("Yes") in (response["choices"][0]["text"])



def rewrite_email(email):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Rewrite this email more assertively and concisely" + "\n" + email,
    temperature=0.21,
    max_tokens=150,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
    )

    return response["choices"][0]["text"]


def findMatches(email): 
    #connect database
    CONNECTION_STRING = "mongodb+srv://confidently:hackviolet23@cluster1.vdxev7c.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['PhraseData']
    print(db)
    col = db.Phrases
    words = [elem["word"] for elem in list(col.find())]

    found_words = [word for word in words if word in email]
    return found_words    


#print(findMatches(email_unconf))
print(rewrite_email(email_unconf))
# Confidently

## What it does
Women tend to qualify their language and undermine themselves in their delivery, especially when communicating with colleagues and peers. They will frequently use qualifying words such as "just", "might", and "could" in emails which results in an apprehensive and diffident tone. We created "Confidently": a Google Chrome extension based website which helps women write more confident and assertive emails. Our extension will assess an email as it is being written by a user, and then provide the user with insight and suggestions on how to make the email more confident. These suggestions will appear to the user on a linked website.

The extension presents two buttons to the user:

`Check Email`

The Check Email button will parse the user's email for words and phrases that are taking away from the assertiveness of the email. This list of words will then be returned to the user (through the extension), giving the user an opportunity to change or remove these words from their email.

`Rewrite Email`

The Rewrite Email button will take the user's existing draft and rewrite it without any "unconfident" language. This email suggestion will be returned to the used through the extension.

Both of these options enable the user to make their emails sound more confident.

## How we built it
- Frontend developed utilizing `JavaScript` and `HTML` with `AJAX` to asynchronously send and receive data from server.
- Backend was built with `python`
- Web scraping Gmail drafts via the `Gmail API` and authentication verified through the `Google Cloud API`
- Text sentiment analysis and revision accomplished with the `OpenAI API`
- Keyword storage and retrieval in `MongoDB`

## Challenges we ran into and accomplishments that we're proud of
1. Integrating Flask to connect the front-end and back-end We were unfortunately unable to use Flask as originally intended, and as a result needed to pivot our project to be hosted as a separate website. This ultimately allowed us to connect our front end and back end, creating a fleshed out full stack application.

2. Implementing the Open-AI API In order to provide the user with a rewritten email, we decided to use the Open-AI API. In particular, we needed the API to assess whether or not an email is "confident" (yes or no) and then rewrite the email with a more assertive tone. Our team was new to this API and we had to experiment with it for a while to understand what kinds of prompts and parameters to pass to it. We messed around with parameters like "temperature" and " model" which change how creative the AI's response should be, and what model of the AI should be used respectively. Modifying these parameters resulted in a wide range of responses, and it took time to narrow these down to get exactly what we wanted.

3. Using MongoDB We needed a way to store the words and phrases that we want to flag in emails, so we turned to MongoDB. Our team members had not extensively used any database services before, so we had to figure out how populate a database and also connect it to the backend of our web application. First we created a file with "unconfident" words and phrases, and then imported this to a database. Then we needed to see matches between the database records and the email. It took us some time to understand the different MongoDB queries and how it can be integrated with Python. The MongoDB UI and shell were very user friendly and allowed us to easily query our database for matches given an email.

4. We are proud of creating a functioning full-stack web application. None of our team members had previously built a functioning website, so this was a huge learned experience for us all. We learned a lot about effective version control and integrating between various platforms that do not easily communicate with each other.

## What's next for Confidently
- Interface with the Gmail UI directly to get overlaid messages and alerts
- Host entire application as a chrome extension rather than a separate website
- Expand database of uncertain language, maybe even automate "uncertain language" recognition.


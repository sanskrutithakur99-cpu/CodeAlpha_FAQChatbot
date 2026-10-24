CodeAlpha FAQ Chatbot

Project Overview

The Student FAQ Chatbot is an NLP-based application developed as part of the CodeAlpha Artificial Intelligence Internship. It answers common student questions by matching user input with a predefined FAQ dataset.

Features

- Interactive chat interface built with Streamlit
- FAQ dataset stored in JSON format
- Text preprocessing and feature extraction using TF-IDF
- Question matching using cosine similarity
- Relevant responses for supported questions
- Fallback response for questions that do not match the dataset
- Clear conversation option

Technologies Used

- Python 3.13
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- JSON

Project Structure

CodeAlpha_FAQChatbot/
├── app.py
├── faqs.json
├── README.md
└── .venv/ 

Installation and Setup

1. Install Python 3.13 or a compatible Python version.
2. Open the project folder in VS Code.
3. Install the required libraries:

python -m pip install streamlit scikit-learn

4. Run the chatbot:

python -m streamlit run app.py

5. Open the local URL displayed in the terminal, usually "http://localhost:8501".

How It Works

1. The chatbot loads predefined questions and answers from "faqs.json".
2. TF-IDF converts FAQ questions into numerical feature vectors.
3. Cosine similarity compares the user's question with the stored questions.
4. The chatbot returns the answer associated with the best match when the similarity score meets the threshold.
5. If no suitable match is found, a fallback message is displayed.

Testing

Test the application using questions about admissions, fees, scholarships, exam timetables, admit cards and results. Also test an unrelated question to verify the fallback response.

Internship

Developed for the CodeAlpha Artificial Intelligence Internship.

Future Improvements

- Expand the FAQ dataset
- Support multilingual questions
- Add voice input and text-to-speech
- Integrate a database
- Deploy the chatbot online

Author

BCA Student | Artificial Intelligence Intern at CodeAlpha
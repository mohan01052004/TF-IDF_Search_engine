🔍 TF-IDF Based Search Engine
📌 Project Overview
This project implements a document search engine using TF-IDF (Term Frequency–Inverse Document Frequency) and an inverted index to retrieve and rank relevant documents.
The system is built on the 20 Newsgroups dataset and provides an interactive web interface using Streamlit.

The search engine preprocesses text using Natural Language Processing techniques and ranks documents based on cosine similarity between query and document vectors.

🎯 Objectives
Design a basic information retrieval system

Apply TF-IDF weighting for document representation

Implement an inverted index for efficient lookup

Rank documents using cosine similarity

Build an interactive Streamlit web application

Validate functionality using unit testing

🧠 Technologies Used
Python

NLTK – Text preprocessing

NumPy – Numerical computations

Scikit-learn – TF-IDF and dataset handling

Streamlit – Web application framework

Pytest – Unit testing

📊 Dataset
The project uses the 20 Newsgroups dataset, which consists of approximately 18,000 text documents categorized into 20 different topics including technology, sports, politics, religion, and science.

The dataset is automatically fetched using the scikit-learn library.

⚙️ Methodology
1. Text Preprocessing
Lowercasing text

Tokenization

Removal of stopwords

Removal of special characters and numbers

2. TF-IDF Representation
Documents are converted into TF-IDF vectors

Common terms are down-weighted

Important terms receive higher weights

3. Inverted Index
Terms are mapped to document IDs

Enables faster identification of candidate documents

4. Search and Ranking
User queries are preprocessed

Cosine similarity is computed between query and documents

Documents are ranked based on relevance score

🖥️ How to Run the Application
Step 1: Install Dependencies
pip install -r requirements.txt
Step 2: Run Unit Tests
pytest
Step 3: Launch the Application
streamlit run streamlit_app.py
Open your browser and navigate to:

http://localhost:8501
🧪 Testing
Unit tests are implemented using pytest to verify:

Correct preprocessing of text

Proper construction of the inverted index

Accurate document ranking

Correct calculation of evaluation metrics

All tests pass successfully before deployment.

📈 Evaluation Metrics
The system evaluates search performance using:

Precision

Recall

These metrics help measure the relevance of retrieved documents.

🌐 Deployment
The application can be deployed using Streamlit Community Cloud, allowing public access without the need for containerization.

🚀 Future Enhancements
Boolean and phrase-based search

Query expansion techniques

Advanced evaluation metrics (Precision@K, Recall@K)

Improved indexing for faster retrieval

👨‍💻 Author
Mohan C
B.Tech – Computer Science / Artificial Intelligence

📜 License
This project is intended for academic and educational purposes only.
# 💬 Sentiment Classifier for Comments (Portuguese)

This project uses **NLP with Hugging Face Transformers** (via `pysentimiento`) to analyze the sentiment of user-submitted comments in **Portuguese**. The input is a text string, and the output is classified as **Positive**, **Negative**, or **Neutral**.

## 🔧 Technologies Used
- Python
- [pysentimiento](https://github.com/josecannete/pysentimiento)
- Hugging Face Transformers
- Streamlit

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/youruser/sentiment-analyzer.git
cd sentiment-analyzer
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Note: The first run may take longer as the BERT model is downloaded.

✨ Example
Input:

"Eu odeio isso."

Output:

Negative

📁 Project Structure
bash
Copy
Edit
sentiment-analyzer/
├── app.py                  # Streamlit app
├── sentiment.py            # Sentiment analysis logic with Hugging Face
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

📄 License
MIT
# 🤖 AI Smart Answer Evaluator

An advanced NLP-based system that automatically evaluates subjective answers using multiple evaluation metrics. This project helps in reducing manual effort in grading and provides instant feedback.

---

## 🚀 Features

- ✅ Automatic answer evaluation
- 📊 Multi-metric scoring system
- 🧠 NLP-based similarity analysis
- 🔑 Keyword matching
- 📏 Length-based scoring
- ⚙️ Adjustable weight parameters
- 🎨 Interactive UI using Streamlit
- 📥 Download evaluation results

---

## 🧠 Methodology

The system evaluates answers using the following techniques:

### 1. Cosine Similarity (TF-IDF)
- Converts text into vectors
- Measures semantic similarity between answers

### 2. Keyword Matching
- Extracts important words from model answer
- Checks overlap with student answer

### 3. Length Analysis
- Ensures answers are not too short or incomplete

### 4. Weighted Final Score
- Combines all metrics using configurable weights

---

## 📊 Evaluation Formula
Final Score = (Similarity × W1) + (Keyword Match × W2) + (Length Score × W3)


Where:
- W1, W2, W3 are adjustable weights

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- NLP (TF-IDF, Cosine Similarity)

---

## 📂 Project Structure
AI_Smart_Answer_Evaluator/
│── app.py
│── requirements.txt
│── README.md


---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/your-username/AI_Smart_Answer_Evaluator.git

cd AI_Smart_Answer_Evaluator


### 2. Install Dependencies
pip install -r requirements.txt


### 3. Run Application

streamlit run app.py


---

## 🌐 Deployment

This project can be deployed easily using:
- Streamlit Cloud

Make sure `requirements.txt` includes:
streamlit
scikit-learn


---

## 🎯 Demo Examples

### ✅ Example 1 (Good Answer)
**Model:** Normalization reduces redundancy  
**Student:** Removes duplicate data  
➡️ Score: ~7–8

---

### 🌟 Example 2 (Excellent Answer)
**Student:** Reduces redundancy and improves integrity  
➡️ Score: ~9+

---

### ❌ Example 3 (Poor Answer)
**Student:** Database stores data  
➡️ Score: ~2–3

---

### ⚠️ Example 4 (Short Answer)
**Student:** Removes redundancy  
➡️ Score: ~4–5

---

## 📈 Future Improvements

- 🔍 Word highlighting
- 📊 Graph-based visualization
- 🤖 Deep learning models (BERT)
- 🗄️ Database integration
- 👤 User authentication system

---

## 🎓 Use Cases

- Automated answer grading
- Online education platforms
- Practice tools for students
- AI-based evaluation systems

---

## 👨‍💻 Author

**Krishna Rai**  
AI & Data Science Student  

---

## ❤️ Acknowledgment

This project was developed as part of an NLP/AI academic mini project.

---

## 📜 License

This project is open-source and free to use for educational purposes.

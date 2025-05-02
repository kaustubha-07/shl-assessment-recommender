# SHL Assessment Recommender

A smart SHL Assessment Recommender system that suggests the most relevant SHL assessments based on user inputs such as job roles, skillsets, and other relevant parameters. The system leverages machine learning and NLP techniques to process and recommend appropriate assessments.

## 🧠 Project Objective

The objective of this project is to help recruiters, HR professionals, and candidates identify the most relevant SHL assessments by analyzing input data such as job titles, skills, and domains.

## 🚀 Features

- Predicts suitable SHL assessments based on input job roles/skills
- Utilizes machine learning and NLP techniques
- Clean and simple user interface (if applicable)
- Recommender system architecture
- Data preprocessing and feature engineering

## 🛠️ Technologies Used

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- NLTK / SpaCy
- Streamlit / Flask (if UI is used)
- Matplotlib / Seaborn (for EDA)

## 📁 Project Structure

```
shl-assessment-recommender/
├── data/                 # Dataset and input files
├── notebooks/            # Jupyter Notebooks for EDA and experiments
├── recommender/          # Core recommendation engine scripts
│   ├── model.py
│   ├── utils.py
│   └── recommender.py
├── app.py                # Entry point for running the app (e.g., Streamlit)
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── LICENSE               # License information
```

## 📊 How It Works

1. **Input Collection**: User enters job title, skillset, or domain.
2. **Preprocessing**: Input is cleaned and vectorized using NLP.
3. **Model Prediction**: A ML model predicts the most relevant SHL assessment(s).
4. **Output**: Recommended assessment(s) are displayed.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kaustubha-07/shl-assessment-recommender.git
   cd shl-assessment-recommender
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📈 Model Training (if applicable)

To train or retrain the model:
```bash
python recommender/model.py
```

## 📄 Sample Input

```json
{
  "job_title": "Software Engineer",
  "skills": ["Python", "Machine Learning", "Data Structures"]
}
```

## ✅ Output Example

```
Recommended SHL Assessments:
- Cognitive Ability Test
- Problem Solving Assessment
- Coding Simulation (Python)
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- SHL for assessment formats and documentation
- Scikit-learn, NLTK, and other open-source libraries

---

**Made with ❤️ by [Kaustubha](https://github.com/kaustubha-07)**

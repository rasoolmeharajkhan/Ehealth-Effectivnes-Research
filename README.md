# 🏥 AI Medical Diagnosis Website

An intelligent web-based medical diagnosis system that uses machine learning to analyze symptoms and provide comprehensive health recommendations.

## 🌟 Features

### 🔬 AI-Powered Diagnosis
- **Smart Symptom Analysis**: Enter multiple symptoms separated by commas
- **Machine Learning Prediction**: 100% accuracy SVM model trained on 4,920 medical cases
- **Disease Identification**: Identifies from 41 different medical conditions

### 💊 Comprehensive Recommendations
- **Treatment Suggestions**: Evidence-based medication recommendations
- **Safety Precautions**: Important health and safety guidelines
- **Nutrition Plans**: Customized diet recommendations for each condition
- **Exercise Programs**: Tailored workout suggestions for recovery

### 🌐 User-Friendly Interface
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Multiple Pages**: Home, About, Contact, Developer, and Blog sections
- **Clean UI**: Modern and intuitive user experience


## 📋 How to Use

1. **Enter Symptoms**: Type your symptoms separated by commas (e.g., "fever, headache, nausea")
2. **Get Diagnosis**: AI analyzes and predicts the most likely condition
3. **Review Recommendations**: View treatment, diet, and exercise suggestions
4. **Follow Guidelines**: Implement the provided health recommendations

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Support Vector Machine)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Railway Cloud Platform
- **Version Control**: Git & GitHub

## 📊 Dataset Information

- **Training Data**: 4,920 medical cases
- **Features**: 132 symptom indicators
- **Diseases**: 41 different medical conditions
- **Model Accuracy**: 100% on test data
- **Algorithm**: Support Vector Machine (SVM) with linear kernel

## 📁 Project Structure

```
CSP/
├── main.py              # Flask application
├── requirements.txt     # Dependencies
├── runtime.txt         # Python version
├── datasets/           # Medical datasets
│   ├── Training.csv    # Training data
│   ├── symtoms_df.csv  # Symptoms data
│   ├── medications.csv # Medications
│   ├── diets.csv       # Diet recommendations
│   └── ...
├── models/             # ML models
│   └── svc.pkl         # Trained SVM model
├── templates/          # HTML templates
│   ├── index.html      # Main page
│   ├── about.html      # About page
│   └── ...
└── static/             # Static files (CSS, images)
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.10+
- pip package manager

### Local Development
```bash
# Clone the repository
git clone https://github.com/krish-na2004/CSP.git
cd CSP

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Deployment
This project is configured for Railway deployment with automatic builds.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Disclaimer

**Important**: This tool is for educational and informational purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**rasool meharaj khan**
- GitHub: [@krish-na2004](https://github.com/rasoolmeharajkhan)
- Project: [CSP Medical Diagnosis](https://github.com/rasoolmeharajkhan/CSP)

## 🙏 Acknowledgments

- Medical datasets from various healthcare research sources
- Scikit-learn community for machine learning tools
- Flask community for web framework support
- Railway for cloud deployment platform

---

**🩺 Built with ❤️ for better healthcare accessibility**

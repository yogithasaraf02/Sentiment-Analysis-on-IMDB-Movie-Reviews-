# 🎬 Sentiment Analysis on IMDB Movie Reviews 

This project performs **binary sentiment classification** (positive or negative) on IMDB movie reviews using **LSTM-based deep learning models**. It includes data preprocessing, tokenization, model building, evaluation, and hyperparameter tuning — all modularized into 13 cleanly organized Python scripts under the `code/` folder.

---

## 📌 Table of Contents

- [📖 Project Overview](#-project-overview)
- [📊 Dataset](#-dataset)
- [🧰 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [📈 Results](#-results)
- [🚀 Future Improvements](#-future-improvements)

---

## 📖 Project Overview

This sentiment analysis project uses an LSTM model to classify movie reviews from the IMDB dataset. The model is trained on cleaned and preprocessed text data, using techniques such as stopword removal, tokenization, padding, and dropout regularization. The project includes both a baseline LSTM model and a tuned version with a learning rate scheduler.

---

## 📊 Dataset

- **Name**: IMDB Movie Reviews Dataset
- **Size**: 50,000 reviews (25k positive, 25k negative)
- **Source**: [Kaggle - IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Format**: CSV with two columns: `review` and `sentiment`

⚠️ **Note**: The dataset is not uploaded due to redistribution restrictions. Please download it from the Kaggle link and place it in the root directory.

---

## 🧰 Tech Stack

### Languages & Libraries
- Python 3.x
- TensorFlow / Keras
- NumPy / Pandas
- Scikit-learn
- NLTK
- Matplotlib / Seaborn

### ML Techniques
- LSTM Neural Network
- Dropout Regularization
- Learning Rate Scheduler (`ReduceLROnPlateau`)

---

## 📂 Project Structure

```bash
.
├── code/
│   ├── 01_setup_and_imports.py
│   ├── 02_load_and_preview_data.py
│   ├── 03_data_exploration_and_summary.py
│   ├── 04_visualize_sentiment_distribution.py
│   ├── 05_text_cleaning_and_preprocessing.py
│   ├── 06_tokenization_and_encoding.py
│   ├── 07_train_test_split.py
│   ├── 08_model_definition_and_compilation.py
│   ├── 09_model_training.py
│   ├── 10_model_evaluation_and_metrics.py
│   ├── 11_plot_training_history.py
│   ├── 12_model_tuning_and_redefinition.py
│   └── 13_training_with_lr_scheduler.py
├── results/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── sentiment_distribution.png
├── models/
│   └── sentiment_model.h5
├── IMDB Dataset.csv     # Not uploaded — download manually
├── requirements.txt
├── .gitignore
└── README.md
```


##  📈 Results
| Metric    | Value |
| --------- | ----- |
| Accuracy  | \~85% |
| Precision | \~86% |
| Recall    | \~84% |
| F1 Score  | \~85% |


## 🚀 Future Improvements

✅ Add Attention Mechanism
✅ Integrate GloVe/Word2Vec embeddings
✅ Try transformer-based models (like BERT)
✅ Deploy model using Flask or FastAPI
✅ Add model explainability tools (LIME, SHAP)


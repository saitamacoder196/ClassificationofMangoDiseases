# Classification of Mango Diseases

## Overview
This project aims to develop an AI model using Convolutional Neural Networks (CNN) to classify defects on mango skin. The goal is to achieve an accuracy of over 90% in detecting various types of diseases that affect mangoes, such as anthracnose, black spots, and white spots.

## Motivation
Vietnam is a leading exporter of mangoes, and ensuring the quality of exported mangoes is crucial. Traditional manual sorting methods are prone to errors, especially for small or subtle defects. Automating this process using AI can significantly enhance accuracy and efficiency, reducing the risk of exporting defective mangoes.

## Project Structure
- **data/**: Contains raw and processed data
  - **raw/**: Raw images of mangoes
  - **processed/**: Preprocessed images ready for training
- **notebooks/**: Jupyter notebooks for data preprocessing, model training, and evaluation
  - **data_preprocessing.ipynb**
  - **model_training.ipynb**
  - **model_evaluation.ipynb**
- **src/**: Source code for data preprocessing, model training, and evaluation
  - **data_preprocessing.py**
  - **model_training.py**
  - **model_evaluation.py**
  - **utils.py**
- **models/**: Trained models
  - **cnn_model.h5**
- **results/**: Evaluation results and metrics
  - **evaluation_metrics.txt**
  - **classification_report.png**
- **environment.yml**: Conda environment file
- **README.md**: Project description and instructions
- **requirements.txt**: Python dependencies

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ClassificationofMangoDiseases.git
   cd ClassificationofMangoDiseases

# VSD-Net
VSD-Net: Underwater Image Enhancement Notebook

This repository contains the VSD-Net notebook for underwater image enhancement.

⚠️ Note: This project is in Jupyter Notebook format (.ipynb).
You need to download the files to run them, either on Google Colab or locally with VSCode/Python.

📂 Files in this repository

VSD-Net.ipynb — Main notebook for underwater image enhancement

README.md — This file

requirements.txt — Python dependencies

🚀 How to run
Option 1: Run on Google Colab

Download the repository as a ZIP or directly use the notebook file.

Open Google Colab
.

Upload VSD-Net.ipynb to Colab.

Make sure you have access to the dataset if needed (or download it from your local storage).

Run the notebook cells sequentially.

You can also use the direct link to download the notebook:
VSD-Net Notebook Link

Option 2: Run locally in VSCode / Jupyter Notebook

Clone this repository or download as ZIP and extract:

git clone <your-repo-url>


Create a Python virtual environment (optional but recommended):

python -m venv venv


Activate the virtual environment:

Windows CMD:

venv\Scripts\activate


Linux / MacOS:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Open VSD-Net.ipynb in VSCode (with Jupyter extension) or in Jupyter Notebook:

jupyter notebook


Run all cells sequentially.

⚠️ Notes

This notebook may include interactive widgets; some features might not fully work outside of Jupyter/Colab.

Ensure that all dataset files and dependencies are in the correct paths as expected by the notebook.

📌 Requirements

All required Python packages are listed in requirements.txt. Install with:

pip install -r requirements.txt


Typical packages may include: torch, torchvision, albumentations, numpy, matplotlib, etc.

💡 Recommendation

For easiest experience, use Google Colab. You won’t need to configure Python or CUDA locally.

If running locally, make sure you have Python >= 3.8 and GPU support if needed.

import tkinter as tk
from tkinter import scrolledtext  # Import scrolledtext for creating a scrollable text area
import subprocess
import pandas as pd
import pickle
import csv
import configparser

def execute_mail_extractor():
    try:
        # Execute the Python script to extract emails
        subprocess.run(["python", "mailextractor.py"])
        print("Email extraction process completed successfully.")
    except Exception as e:
        print(f"An error occurred while executing the mail extractor: {e}")

def preprocess_and_vectorize():
    try:
        subprocess.run(["python", "Datacleaner.py"])
        print("Email cleaning process completed successfully.")
    except Exception as e:
        print(f"An error occurred during cleaning process: {e}")

def predict():
    try:
        subprocess.run(["python", "phishindetector.py"])
        print("Email phishing scaning process completed successfully.")
    except Exception as e:
        print(f"An error occurred during prediction process: {e}")

def main():
    # Call the function to execute the mail extractor
    execute_mail_extractor()

    # Call the function to preprocess text, perform TF-IDF vectorization, and predict labels
    preprocess_and_vectorize()

    # Call the function to predict labels for the new data
    predict()

if __name__ == "__main__":
    main()

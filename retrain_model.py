#!/usr/bin/env python3
"""
Script to retrain and save the SVC model with current numpy version
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import os

def train_and_save_model():
    try:
        print("🔄 Training new SVC model...")
        
        # Load training data
        dataset = pd.read_csv('datasets/Training.csv')
        print(f"✅ Loaded dataset with shape: {dataset.shape}")
        
        # Prepare data
        X = dataset.drop('prognosis', axis=1)
        y = dataset['prognosis']
        
        # Encode target variable
        le = LabelEncoder()
        le.fit(y)
        Y = le.transform(y)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=20)
        
        # Train SVC model
        svc = SVC(kernel='linear')
        svc.fit(X_train, y_train)
        
        # Test accuracy
        accuracy = svc.score(X_test, y_test)
        print(f"✅ Model trained with accuracy: {accuracy:.4f}")
        
        # Save the model
        os.makedirs('models', exist_ok=True)
        with open('models/svc.pkl', 'wb') as f:
            pickle.dump(svc, f)
        
        print("✅ Model saved successfully to models/svc.pkl")
        return True
        
    except Exception as e:
        print(f"❌ Error training model: {e}")
        return False

if __name__ == "__main__":
    success = train_and_save_model()
    if success:
        print("🎉 Model retraining completed successfully!")
    else:
        print("💥 Model retraining failed!")

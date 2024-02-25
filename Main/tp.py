import numpy as np
import librosa
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('deepfake_audio_detection_model.h5')

def extract_audio_features(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)
    
    # Extract audio features
    chroma_stft = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))
    rms = np.mean(librosa.feature.rms(y=y))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20), axis=1)
    
    # Concatenate all features into a single vector
    features = np.concatenate([
        [chroma_stft],
        [rms],
        [spectral_centroid],
        [spectral_bandwidth],
        [rolloff],
        [zero_crossing_rate],
        mfccs
    ])
    
    # Check if the features have the desired shape
    if features.shape[0] != 26:
        raise ValueError("The number of features extracted is not 26")
    
    return features

def predict_audio(audio_file):
    # Extract features from the audio file
    audio_features = extract_audio_features(audio_file)
    
    # Scale the features
    scaler = StandardScaler()
    audio_features_scaled = scaler.fit_transform(audio_features.reshape(1, -1))
    
    # Predict using the model
    prediction = model.predict(audio_features_scaled)
    print(prediction)
    
    # Decode the prediction
    if prediction > 0.1:
        return "Fake"
    else:
        return "Real"

# Input audio file path from the user
# audio_file = input("Enter the path to your audio file: ")

# Predict the authenticity of the input audio file
prediction = predict_audio("C:\\Users\\princ\\Downloads\\fake1_1.wav")
print("Prediction:", prediction)







    



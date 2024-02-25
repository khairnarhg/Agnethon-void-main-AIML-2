from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import librosa
import logging

#loading models
model = load_model('deepfake_audio_detection_model.h5')


# Load the trained model
# model = load_model('deepfake_image_detection_model.h5')

def index(request):
    return render(request, 'Main/web.html')

def login(request):
    return render(request, 'Main/login.html')

def signup(request):
    return render(request, 'Main/signup.html')

def learn(request):
    return render(request, 'Main/learn.html')

def home(request):
    return render(request , 'Main/home.html')

def about(request):
    return render(request, 'Main/about.html')

def uploadvid(request):
    return render(request, 'Main/uploadvid.html')

def uploadaud(request):
    return render(request,'Main/uploadaud.html')

def uploadimg(request):
    return render(request,'Main/uploadimg.html')
@csrf_exempt
def predict_image(request):
    if request.method == 'POST':
        # Assuming the image file is sent in the request
        image_file = request.FILES['image']
        
        # Preprocess the image
        img = image.load_img(image_file, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.  # Normalize the image
        
        # Make prediction
        prediction = model.predict(img_array)
        
        # Convert prediction to readable format
        if prediction[0][0] >= 0.5:
            result = 'FAKE'
        else:
            result = 'REAL'
        
        return JsonResponse({'result': result})
    
from django.http import HttpResponse
from django.shortcuts import render
import librosa
import numpy as np

# Load your trained model here
# model = load_model('your_model_path')

@csrf_exempt
def predict_audio(request):
    if request.method == 'POST' and request.FILES['audio']:
        # Get the uploaded audio file
        audio_file = request.FILES['audio']
        
        # Extract audio features
        audio_features = extract_audio_features(audio_file)
        
        # Reshape features to match the model's input shape
        audio_features = audio_features.reshape(1, -1)
        
        # Make prediction using the trained model
        prediction = model.predict(audio_features)
        
        # Convert prediction to readable format
        if prediction[0][0] >= 0.5:
            result = 'FAKE'
        else:
            result = 'REAL'
        
        return render(request, 'audio_prediction_result.html', {'result': result})

    return HttpResponse("No audio file uploaded.")

def extract_audio_features(audio_file):
    # Load audio file
    y, sr = librosa.load(audio_file)
    
    # Extract audio features
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)[0]
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

    # Round each feature individually
    spectral_centroid_rounded = [round(x, 2) for x in spectral_centroid]
    spectral_bandwidth_rounded = [round(x, 2) for x in spectral_bandwidth]
    spectral_contrast_rounded = [round(x, 2) for x in spectral_contrast.mean(axis=1)]
    spectral_rolloff_rounded = [round(x, 2) for x in spectral_rolloff]
    zero_crossing_rate_rounded = [round(x, 2) for x in zero_crossing_rate]
    mfccs_rounded = [round(x, 2) for x in mfccs.mean(axis=1)]

    # Concatenate all rounded features into a single vector
    features = np.concatenate([
        spectral_centroid_rounded,
        spectral_bandwidth_rounded,
        spectral_contrast_rounded,
        spectral_rolloff_rounded,
        zero_crossing_rate_rounded,
        mfccs_rounded
    ])
    
    return features








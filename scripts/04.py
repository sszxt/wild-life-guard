import os, time, logging, tempfile
import cv2 as cv
from PIL import Image
import streamlit as st
from ultralytics import YOLO
import pygame  # For sound playback

MODEL_DIR = r'C:\Users\Rizwan\Downloads\Real-Time-Animal-Species-Detection-main\Real-Time-Animal-Species-Detection-main\runs\detect\train\weights\best.pt'
SOUND_DIR = r'C:\Users\Rizwan\Downloads\Real-Time-Animal-Species-Detection-main\Real-Time-Animal-Species-Detection-main\sound'  # Directory where sound files are stored

# Initialize pygame mixer for playing sound
pygame.mixer.init()

log_dir = "./logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, "log.log"), 
    filemode='a', 
    level=logging.INFO, 
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)

# Dictionary to map animal names to their corresponding sound files
animal_sounds = {
    "Buffalo": os.path.join(SOUND_DIR, "automobile-horn.mp3"),
    "Elephant": os.path.join(SOUND_DIR, "fireworks.mp3"),
    "Rhino": os.path.join(SOUND_DIR, "airhorn.mp3"),
    "Zebra": os.path.join(SOUND_DIR, "whistle-down.mp3"),
    "Cheetah": os.path.join(SOUND_DIR, "dog-barking.mp3"),
    "Fox": os.path.join(SOUND_DIR, "dog-barking.mp3"),
    "Jaguar": os.path.join(SOUND_DIR, "dog-barking.mp3"),
    "Tiger": os.path.join(SOUND_DIR, "fireworks.mp3"),
    "Lion": os.path.join(SOUND_DIR, "fireworks.mp3"),
    "Panda": os.path.join(SOUND_DIR, "police-siren.mp3")
}

def main():
    global model
    model = YOLO(MODEL_DIR)

    st.sidebar.header("**Animal Classes**")
    class_names = list(animal_sounds.keys())

    for animal in class_names:
        st.sidebar.markdown(f"- *{animal.capitalize()}*")

    st.title("Real-time Animal Species Detection")
    st.write("The aim of this project is to develop an efficient computer vision model capable of real-time wildlife detection.")

    # File upload for image or video
    uploaded_file = st.file_uploader("Upload an image or video", type=['jpg', 'jpeg', 'png', 'mp4'])

    # Option to select real-time detection
    detect_realtime = st.checkbox("Real-time Detection")

    if uploaded_file:
        if uploaded_file.type.startswith('image'):
            inference_images(uploaded_file)
        if uploaded_file.type.startswith('video'):
            inference_video(uploaded_file)

    if detect_realtime:
        inference_realtime()  # Start real-time detection


def inference_images(uploaded_file):
    image = Image.open(uploaded_file)
    predict = model.predict(image)

    boxes = predict[0].boxes
    plotted = predict[0].plot()[:, :, ::-1]

    if len(boxes) == 0:
        st.markdown("**No Detection**")
    
    st.image(plotted, caption="Detected Image", width=600)
    logging.info("Detected Image")


def inference_video(uploaded_file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    temp_file.close()

    cap = cv.VideoCapture(temp_file.name)
    frame_count = 0
    if not cap.isOpened():
        st.error("Error opening video file.")
 
    frame_placeholder = st.empty()
    stop_placeholder = st.button("Stop")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 2 == 0:
            predict = model.predict(frame, conf=0.75)
            plotted = predict[0].plot()
            frame_placeholder.image(plotted, channels="BGR", caption="Video Frame")
        
        if stop_placeholder:
            os.unlink(temp_file.name)
            break

    cap.release()


# Real-time detection using webcam
def inference_realtime():
    st.write("Starting Real-time Detection...")
    cap = cv.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        st.error("Could not open webcam.")
        return

    frame_placeholder = st.empty()  # Placeholder to show the video frames
    stop_button = st.button("Stop Real-time Detection")  # Button to stop real-time detection

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame from webcam.")
            break

        # Real-time prediction on the frame
        predict = model.predict(frame, conf=0.75)
        plotted = predict[0].plot()

        # Display the video stream
        frame_placeholder.image(plotted, channels="BGR", caption="Real-time Video Frame")

        # Play sound for detected animals
        play_sounds_for_animals(predict[0])

        # Stop the video stream when the stop button is clicked
        if stop_button:
            break

    cap.release()


# Function to play the sound for detected animals
def play_sounds_for_animals(predict_output):
    for result in predict_output:
        for cls in result.boxes.cls:
            animal_name = model.names[int(cls)]  # Get the detected animal name
            if animal_name in animal_sounds:
                sound_file = animal_sounds[animal_name]
                play_sound(sound_file)
                logging.info(f"Detected {animal_name} - Playing sound")

# Function to play sound using pygame
def play_sound(sound_file):
    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    else:
        logging.error(f"Sound file not found: {sound_file}")


if __name__ == '__main__':
    main()

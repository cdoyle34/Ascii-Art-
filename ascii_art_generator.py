#ascii_art
import cv2
from PIL import Image
import numpy as np

# ASCII characters used to build the output
ASCII_CHARS = "@%#*+=-:. "

def load_video(path):
    return cv2.VideoCapture(path)

def frame_to_ascii(frame, width=120):
    # Resize frame to desired width while maintaining aspect ratio
    height = int(frame.shape[0] * (width / frame.shape[1]))
    resized_frame = cv2.resize(frame, (width, height))
    
    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Normalize and map the grayscale values to ASCII characters
    ascii_art = ""
    for pixel_value in np.nditer(gray_frame):
        # Safe mapping of pixel values to the index in ASCII_CHARS
        index = int(pixel_value / 255 * (len(ASCII_CHARS) - 1))
        ascii_art += ASCII_CHARS[index]
    return '\n'.join([ascii_art[i:i+width] for i in range(0, len(ascii_art), width)])

import os  # Make sure to import os at the top of your script

def main(video_path, output_path):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    cap = load_video(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ascii_art = frame_to_ascii(frame)
        # Optionally display the ASCII art
        print(ascii_art)
        # Save the ASCII art to a file
        with open(f"{output_path}/frame_{frame_count}.txt", 'w') as file:
            file.write(ascii_art)
        frame_count += 1

    cap.release()

if __name__ == "__main__":
    video_path = "/Users/camdoyle/Desktop/vid2.mov"
    output_path = "/Users/camdoyle/Desktop/ascii_art_output"
    main(video_path, output_path)

import cv2
import os
import numpy as np

def text_frames_to_video(input_path, output_video_path, frame_rate):
    # List all files in the directory sorted by frame count in the filename
    frame_files = [os.path.join(input_path, f) for f in sorted(os.listdir(input_path), key=lambda x: int(x.split('_')[1].split('.')[0])) if f.endswith('.txt')]

    # Read the first frame to set video dimensions
    with open(frame_files[0], 'r') as file:
        frame_example = file.readlines()
    # Adjust scale to increase the resolution
    scale = 20  # Modify scale factor as needed for larger text and frame
    height, width = len(frame_example) * scale, len(frame_example[0].strip()) * scale
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height), False)

    for file_name in frame_files:
        with open(file_name, 'r') as file:
            frame = file.readlines()
        # Convert the frame to an image (create a blank image and put text on it)
        img = np.zeros((height, width), np.uint8)
        font = cv2.FONT_HERSHEY_PLAIN
        for i, line in enumerate(frame):
            cv2.putText(img, line.strip(), (0, (i + 1) * scale), font, 2, (255,), 2, cv2.LINE_AA)

        # Write the frame into the video
        out.write(img)

    # Release everything when job is finished
    out.release()

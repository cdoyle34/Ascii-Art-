# Ascii-Art-
Simple ascii art I made for fun after seeing someone else do it online, could have been created a little better.

Initial Setup and ASCII Art Generation
Script Development:

Extract Frames from Video: I started by developing a Python script to load a video file and extract its frames using OpenCV.
Convert Frames to ASCII Art: Each video frame was converted into ASCII art. This involved resizing each frame to a manageable dimension, converting it to grayscale, and then mapping the grayscale values to a predefined set of ASCII characters that represent different shades of gray.
Output ASCII Art to Text Files:
Saving Frames: I saved the ASCII art for each frame as individual text files, allowing for a frame-by-frame representation of the video in ASCII format.
Video Creation from ASCII Art
Script Modification for Video Creation:

Read ASCII Frames: I modified the script to read ASCII art from the text files.
Create Video from ASCII Art: Using OpenCV, I further adapted the script to convert these ASCII frames back into a video format. Each text file was read, and for each line in the file, the text was drawn onto a blank image frame using OpenCV's putText method.
Adjustments for Enhanced Clarity:

Resolution Adjustment: I increased the resolution of the output video by scaling up the dimensions of each frame. This was done to improve the clarity and readability of the ASCII art in the video.
Font Settings: I adjusted the font type and size used in cv2.putText to make the ASCII characters clearer and more visually appealing in the video.
Error Handling: I added checks to ensure the output directory exists before saving files and handled file reading errors gracefully.
Performance and Quality Enhancements:
Video Settings: I configured the frame rate and codec settings for the video creation to balance performance and quality.
Enhanced Contrast: I recommended using high contrast colors (e.g., white text on a black background) to improve the visibility and clarity of the ASCII art in the video.
Troubleshooting and Debugging
Error Resolution:

Index Error: I initially faced and resolved an indexing error in the ASCII mapping function which was causing crashes.
File Handling Errors: I addressed issues with file paths and directory existence to prevent FileNotFoundError.
Data Type Handling: I corrected issues related to how text data was handled, moving from using numpy's loadtxt (which was inappropriate for handling plain text files) to standard Python file reading methods.
By following these steps, I successfully created and refined the video from ASCII art frames.

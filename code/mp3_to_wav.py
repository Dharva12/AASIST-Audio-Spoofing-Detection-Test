import os
from pydub import AudioSegment

# Paths for input and output folders
input_folder = r"C:\Users\Legion 5I 72IN\Desktop\Reality Defender\Polly_final_mp3"
output_folder = r"C:\Users\Legion 5I 72IN\Desktop\Reality Defender\Sample_test"

#output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"): 
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".flac")
        
        # Load the MP3 file
        audio = AudioSegment.from_mp3(input_file)
        
        # Resample to 16 kHz (16000 samples/second)
        audio = audio.set_frame_rate(16000)
        
        # Export the file as FLAC with 16 kHz
        audio.export(output_file, format="flac")
        print(f"Converted {filename} to FLAC at 16 kHz")

print("All files have been converted to 16 kHz.")

import os
from pydub import AudioSegment

# Paths for input and output folders
input_folder = r"C:\Users\Legion 5I 72IN\Desktop\Reality Defender\Playht_Final_wav"  # Path where your WAV files are located
output_folder = r"C:\Users\Legion 5I 72IN\Desktop\Reality Defender\Sample_test"  # Path to save the converted FLAC files

# output folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):  
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".flac")
        
        # Load the WAV file
        audio = AudioSegment.from_wav(input_file)

        audio = audio.set_frame_rate(16000)
        
        # Export the file as FLAC
        audio.export(output_file, format="flac")
        print(f"Converted {filename} to FLAC")

print("All WAV files have been converted to FLAC.")

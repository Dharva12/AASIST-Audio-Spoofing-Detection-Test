# AASIST-Audio-Spoofing-Detection-Test
This repository contains the code and files for running audio spoofing detection using the AASIST model. The system detects synthetic (spoofed) audio using a pre-trained AASIST model and processes audio files generated from various Text-to-Speech (TTS) platforms like PlayHT, ElevenLabs, Amazon Polly, and samples from the ASVspoof19 dataset.

#Requirements
To ensure you have the correct dependencies, create a virtual environment using the included environment.yaml file. If you don’t have Conda installed, you can install it from here.

#Setup
1. Clone the repository:

git clone https://github.com/<your-repo-name>.git
cd AASIST-Audio-Spoofing-Detection

2. Install the environment: To set up the environment using Conda, run:

conda env create -f environment.yaml
conda activate aasist_audio_spoofing

3. Install dependencies with pip (if using requirements.txt instead of Conda):

pip install -r requirements.txt

4. Download the AASIST Pre-Trained Model: Place the pre-trained AASIST model checkpoint (AASIST.pth) in the models/weights/ directory:

C:\Users\<Your-Username>\Desktop\Reality Defender\aasist\models\weights\AASIST.pth
Running the Inference

To run inference on your custom dataset or provided test samples:

  1. Prepare the FLAC files: Convert your MP3 and WAV audio files to FLAC format using the provided conversion scripts (mp3_to_flac.py and wav_to_flac.py).

  2. Run the Inference Script: Use the following command to run inference on a directory of test samples:

python inference.py --config config/AASIST.conf --test_dir C:/path/to/test/samples --output_file inference_results.txt

--config: Path to the configuration file.
--test_dir: Directory containing test FLAC files.
--output_file: File to save the results.

  3. View Results: After running inference, the results will be saved in the specified output file (inference_results.txt). Each entry will contain the file name and the spoofing score, indicating whether the audio was classified as genuine or spoofed.

# Sample Data
The metadata of the test samples is provided in metadata.csv, containing details such as the source platform, prompts, settings used, and the model’s classification results.

# Key Files

inference.py: The script to run the audio spoof detection on custom test samples.
data_utils.py: Handles dataset loading and preprocessing.
mp3_to_flac.py: Converts MP3 files to FLAC.
wav_to_flac.py: Converts WAV files to FLAC.

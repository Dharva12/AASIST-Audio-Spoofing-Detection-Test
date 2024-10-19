import argparse
import json
import os
from pathlib import Path
import torch
import torch.nn as nn
from importlib import import_module
from data_utils import Dataset_Custom  # Importing the custom dataset loader

def run_inference(args: argparse.Namespace):
    # Load config
    with open(args.config, "r") as f_json:
        config = json.loads(f_json.read())
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")
    
    # Loading the pre-trained model
    model = get_model(config["model_config"], device)
    model.load_state_dict(torch.load(config["model_path"], map_location=device))
    model.eval()  # Setting the model to evaluation mode

    # Dataset Preparation
    audio_files = [f.stem for f in Path(args.test_dir).glob("*.flac")]  # Listing all FLAC files in the test directory
    test_dataset = Dataset_Custom(list_IDs=audio_files, base_dir=Path(args.test_dir))  # Using Dataset_Custom
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=config["batch_size"], shuffle=False)

    # Inference
    print("Running inference on test files...")
    results = []
    for batch_x, utt_id in test_loader:
        batch_x = batch_x.to(device)
        with torch.no_grad():
            _, batch_out = model(batch_x)
            batch_score = (batch_out[:, 1]).data.cpu().numpy().ravel()  # Spoofing score
        results.append((utt_id, batch_score))

    # Output
    save_results(results, args.output_file)
    print(f"Inference complete. Results saved to {args.output_file}")

def get_model(model_config, device):
    """Define the model architecture."""
    module = import_module(f"models.{model_config['architecture']}")
    _model = getattr(module, "Model")
    model = _model(model_config).to(device)
    print(f"Loaded model with {sum([p.numel() for p in model.parameters()])} parameters.")
    return model

def save_results(results, output_file):
    """Save the inference results to a file."""
    with open(output_file, "w") as f:
        for utt_id, score in results:
            f.write(f"{utt_id}: {score}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AASIST Inference")
    parser.add_argument("--config", type=str, required=True, help="Path to the configuration file")
    parser.add_argument("--test_dir", type=str, required=True, help="Directory with test audio files")
    parser.add_argument("--output_file", type=str, default="inference_results.txt", help="File to save results")
    args = parser.parse_args()

    run_inference(args)

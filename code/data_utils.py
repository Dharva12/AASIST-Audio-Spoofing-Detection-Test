import numpy as np
import soundfile as sf
import torch
from torch import Tensor
from torch.utils.data import Dataset

def pad(x, max_len=64600):
    x_len = x.shape[0]
    if x_len >= max_len:
        return x[:max_len]
    # need to pad
    num_repeats = int(max_len / x_len) + 1
    padded_x = np.tile(x, (1, num_repeats))[:, :max_len][0]
    return padded_x

class Dataset_Custom(Dataset):
    def __init__(self, list_IDs, base_dir):
        """list_IDs : list of strings (each string: filename of audio file without extension)"""
        self.list_IDs = list_IDs  # Audio File names
        self.base_dir = base_dir  # Directory containing audio files
        self.cut = 64600 

    def __len__(self):
        return len(self.list_IDs)

    def __getitem__(self, index):
        key = self.list_IDs[index]
        # Read .flac audio file
        X, _ = sf.read(str(self.base_dir / f"{key}.flac"))
        X_pad = pad(X, self.cut)
        x_inp = Tensor(X_pad)
        return x_inp, key

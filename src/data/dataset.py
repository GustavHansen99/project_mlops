import os
from os.path import join

from PIL import Image
from torch.utils.data import Dataset


class BTDataset(Dataset):
    def __init__(self, data_path, transform=None):
        super().__init__()

        self.images = [
            join(data_path, image_path)
            for image_path in os.listdir(data_path)
            if "jpg" in image_path
        ]

        self.labels = []
        for image in self.images:
            if "NotCancer" in image:
                self.labels.append(0)
            else:
                self.labels.append(1)

        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = Image.open(self.images[idx]).convert("RGB")
        if self.transform:
            return (self.transform(image), self.labels[idx])
        else:
            return (image, self.labels[idx])

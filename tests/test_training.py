import numpy as np
import torch
from torch.utils.data import DataLoader
from torchvision import transforms

from src.data.dataset import BTDataset


def test_training_and_validation_data():
    """
    Pytest to check our training and validation data:
    We check:
        - that both classes are represented in both sets
        - that the data is in the correct shape
    """
    train_path = "data/processed/train/"
    validation_path = "data/processed/validate/"

    shape = 128
    batch_size = 32
    workers = 8
    # Transforms
    transform = transforms.Compose(
        [
            transforms.Resize((shape, shape)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    train_set = DataLoader(
        BTDataset(data_path=train_path, transform=transform),
        shuffle=True,
        batch_size=batch_size,
        num_workers=workers,
    )

    validation_set = DataLoader(
        BTDataset(data_path=validation_path, transform=transform),
        shuffle=False,
        batch_size=batch_size,
        num_workers=workers,
    )

    train_ys = []
    train_shapes = []
    for step, (x, y) in enumerate(train_set):
        train_ys.append(np.unique(y))
        train_shapes.append(x.shape[1:] == torch.Size([3, shape, shape]))

    val_ys = []
    val_shapes = []
    for step, (x, y) in enumerate(validation_set):
        val_ys.append(np.unique(y))
        val_shapes.append(x.shape[1:] == torch.Size([3, shape, shape]))

    assert (
        len(np.unique(train_ys)) == 2
    ), "Both classes are not present in training"

    assert (
        len(np.unique(val_ys)) == 2
    ), "Both classes are not present in validation"

    assert all(train_shapes), "The shapes of training data is incorrect"

    assert all(val_shapes), "The shapes of validation data is incorrect"

import os
import sys

import pytorch_lightning as pl
from model import EfficientNet
from omegaconf import OmegaConf
from torch.utils.data import DataLoader
from torchvision import transforms

from src.data.dataset import BTDataset

sys.path.insert(0, os.path.join(os.getcwd()))


def evaluate(config):
    # Load model
    model = EfficientNet.load_from_checkpoint(
        config.hyperparameters.checkpoint_path
    )

    # Transforms
    transform = transforms.Compose(
        [
            transforms.Resize(
                (config.transforms.resize_x, config.transforms.resize_y)
            ),
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,)),
        ]
    )

    test_set = DataLoader(
        BTDataset(
            data_path=config.hyperparameters.test_path, transform=transform
        ),
        shuffle=False,
        batch_size=config.hyperparameters.batch_size,
        num_workers=config.hyperparameters.dl_workers,
    )

    # Initialize trainer
    if config.hyperparameters.gpu:
        trainer = pl.Trainer(accelerator="gpu", devices=1)
    else:
        trainer = pl.Trainer()

    # Evaluate model
    trainer.test(model, test_set)


if __name__ == "__main__":
    # loading
    config = OmegaConf.load(os.path.join("config", "evaluate_conf.yaml"))

    # Evaluate model
    evaluate(config)

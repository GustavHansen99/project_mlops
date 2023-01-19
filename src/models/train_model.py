import os
from typing import Optional

import pytorch_lightning as pl
from google.cloud import storage
from model import EfficientNet
from omegaconf import OmegaConf
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader
from torchvision import transforms

from src.data.dataset import BTDataset

_BUCKET_NAME = "artifacts_group_55"


def _create_bucket_folder(
    path: str, bucket: Optional[str] = _BUCKET_NAME
) -> None:
    """Creates a folder inside the bucket"""

    gcs_client = storage.Client()
    bucket = gcs_client.get_bucket(bucket)
    blob = bucket.blob(path)

    blob.upload_from_string(
        "", content_type="application/x-www-form-urlencoded;charset=UTF-8"
    )


def train(config):
    # Initialize model and dataloader
    model = EfficientNet(
        lr=config.hyperparameters.learning_rate,
        pretrained=config.hyperparameters.pretrained,
        num_classes=config.hyperparameters.num_classes,
        checkpoint_path=config.hyperparameters.checkpoint_path,
    )

    # Transforms
    transform = transforms.Compose(
        [
            transforms.Resize(
                (config.transforms.resize_x, config.transforms.resize_y)
            ),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    train_set = DataLoader(
        BTDataset(
            data_path=config.hyperparameters.train_path, transform=transform
        ),
        shuffle=True,
        batch_size=config.hyperparameters.batch_size,
        num_workers=config.hyperparameters.dl_workers,
    )

    validation_set = DataLoader(
        BTDataset(
            data_path=config.hyperparameters.validate_path, transform=transform
        ),
        shuffle=False,
        batch_size=config.hyperparameters.batch_size,
        num_workers=config.hyperparameters.dl_workers,
    )

    wandb_logger = WandbLogger(
        entity="g55_project_mlops", project="mlops_project"
    )
    wandb_logger.experiment.config.update(config)

    if config.hyperparameters.checkpoint_path:
        save_folder = config.data.bucket + "/" + str(config.experiment_id)
        _create_bucket_folder(path=save_folder)
        checkpoint_callback = ModelCheckpoint(
            dirpath=save_folder,
            monitor="validation_loss",
            mode="min",
        )
        early_stop = EarlyStopping(monitor="validation_loss", mode="min")
        # Initialize trainer
        if config.hyperparameters.gpu:
            trainer = pl.Trainer(
                callbacks=[checkpoint_callback, early_stop],
                max_epochs=config.hyperparameters.epochs,
                accelerator="gpu",
                devices=1,
                logger=wandb_logger,
            )
        else:
            trainer = pl.Trainer(
                callbacks=[checkpoint_callback, early_stop],
                max_epochs=config.hyperparameters.epochs,
                logger=wandb_logger,
            )
    else:
        # Initialize trainer
        if config.hyperparameters.gpu:
            trainer = pl.Trainer(
                max_epochs=config.hyperparameters.epochs,
                accelerator="gpu",
                devices=1,
                logger=wandb_logger,
            )
        else:
            trainer = pl.Trainer(
                max_epochs=config.hyperparameters.epochs, logger=wandb_logger
            )

    # Training
    trainer.fit(model, train_set, validation_set)


if __name__ == "__main__":
    # loading
    config = OmegaConf.load(os.path.join("config", "train_conf.yaml"))

    # Train model
    train(config)

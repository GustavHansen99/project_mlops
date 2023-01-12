import os
import sys
sys.path.insert(0, os.path.join(os.getcwd()))

from omegaconf import OmegaConf

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import transforms
import pytorch_lightning as pl

from model import EfficientNet
from src.data.dataset import BTDataset

def evaluate(config):
    # Load model 
    model = EfficientNet.load_from_checkpoint(config.hyperparameters.checkpoint_path)
    
    # Transforms
    transform = transforms.Compose([transforms.Resize((config.hyperparameters.resize_x, config.hyperparameters.resize_y)), 
                            transforms.ToTensor(),
                            transforms.Normalize((0.5,), (0.5,))
                            ])

    test_set = DataLoader(BTDataset(data_path=config.hyperparameters.test_path, transform=transform), 
                        shuffle=False, 
                        batch_size=config.hyperparameters.batch_size,
                        num_workers=config.hyperparameters.dl_workers)

    # Initialize trainer
    if config.hyperparameters.gpu:
        trainer = pl.Trainer(accelerator='gpu', devices=1)
    else: 
        trainer = pl.Trainer()

    # Evaluate model
    trainer.test(model, test_set)

if __name__ == "__main__":
    # loading
    config = OmegaConf.load(os.path.join('config', 'evaluate_conf.yaml'))
   
    # Evaluate model
    evaluate(config)

from typing import Optional

import timm
import torch
from pytorch_lightning import LightningModule
from torch import nn, optim


class EfficientNet(LightningModule):
    def __init__(
        self,
        lr: Optional[float] = 1e-3,
        pretrained: Optional[bool] = True,
        num_classes: Optional[int] = 2,
        checkpoint_path: Optional[bool] = False,
    ):
        super().__init__()

        self.efficientNet = timm.create_model(
            "efficientnet_b0", pretrained=pretrained, num_classes=num_classes
        )

        self.criterium = nn.CrossEntropyLoss()
        self.lr = lr

        self.save_hyperparameters()

    def forward(self, x):
        return self.efficientNet(x)

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=self.lr)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)

        # Log loss
        loss = self.criterium(y_hat, y)
        self.log(
            "train_loss",
            loss,
            on_step=False,
            on_epoch=True,
            prog_bar=True,
            logger=True,
        )

        # Log accuracy
        ps = torch.exp(y_hat)
        equality = y.data == ps.max(1)[1]
        accuracy = equality.type_as(torch.FloatTensor()).mean()
        self.log(
            "train_acc",
            accuracy,
            on_step=False,
            on_epoch=True,
            prog_bar=True,
            logger=True,
        ),

        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)

        # Log loss
        loss = self.criterium(y_hat, y)
        self.log("validation_loss", loss, prog_bar=True, logger=True)

        # Log accuracy
        ps = torch.exp(y_hat)
        equality = y.data == ps.max(1)[1]
        accuracy = equality.type_as(torch.FloatTensor()).mean()
        self.log("validation_acc", accuracy, prog_bar=True, logger=True),

    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)

        # Log loss
        loss = self.criterium(y_hat, y)
        self.log("test_loss", loss, prog_bar=True, logger=True)

        # Log accuracy
        ps = torch.exp(y_hat)
        equality = y.data == ps.max(1)[1]
        accuracy = equality.type_as(torch.FloatTensor()).mean()
        self.log("test_acc", accuracy, prog_bar=True, logger=True),

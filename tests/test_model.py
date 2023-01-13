import torch

from src.models.model import EfficientNet


def test_forward_pass():
    """
    Pytest to check the forward pass of our model:
    We check:
        - that given a input we get the correct output shape
    """
    model = EfficientNet(
        lr=0.0001, pretrained=True, num_classes=2, checkpoint_path=False
    )
    batch1 = 32
    batch2 = 64
    gen_data1 = torch.randn((batch1, 3, 128, 128))
    gen_data2 = torch.randn((batch2, 3, 150, 150))
    output1 = model.forward(gen_data1)
    output2 = model.forward(gen_data2)

    assert output1.shape == torch.Size(
        [batch1, 2]
    ), "The output shape of a forward pass is incorrect"

    assert output2.shape == torch.Size(
        [batch2, 2]
    ), "The output shape of a forward pass is incorrect"

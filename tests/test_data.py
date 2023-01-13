import torch
from torchvision import transforms

from src.data.dataset import BTDataset


def test_data():
    """
    Pytest to check that our data collection and transform work on our raw data
    """
    data_path_BT = "data/raw/BrainTumorDataSet/Brain_Tumor/"
    data_path_H = "data/raw/BrainTumorDataSet/Healthy/"

    shape = 128
    transform = transforms.Compose(
        [
            transforms.Resize((shape, shape)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
    BT_data = BTDataset(data_path_BT, transform=transform)
    healthy_data = BTDataset(data_path_H, transform=transform)
    assert (
        len(BT_data) == 2358 and len(healthy_data) == 2074
    ), "The data doesn't contain the correct number of samples"

    assert all([torch.is_tensor(BT_image) for BT_image, _ in BT_data]) and all(
        [torch.is_tensor(healthy_image) for healthy_image, _ in healthy_data]
    ), "The data has not been converted to tensors"

    assert all(
        [
            BT_image.shape == torch.Size([3, shape, shape])
            for BT_image, _ in BT_data
        ]
    ) and all(
        [
            healthy_image.shape == torch.Size([3, shape, shape])
            for healthy_image, _ in healthy_data
        ]
    ), "The shape of the data samples does not match the required"

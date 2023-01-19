#!/bin/bash

echo "Downloadind data..."
dvc pull

echo "Training model..."
python src/models/train_model.py

echo "Finished Training"

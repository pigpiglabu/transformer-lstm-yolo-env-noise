# transformer_lstm_yolo_env_noise

This repository contains a Transformer+LSTM YOLO-style architecture for env. noise SPL (Sound Pressure Level) time-series prediction and anomaly detection. The codebase follows a YOLO-inspired one-shot grid output processing in the temporal dimension.

## Project structure
- src/model/transformer_lstm_yolo.py
- src/utils/positional_encoding.py
- src/dataset/noise_spl_dataset.py
- train_transformer_lstm_yolo.py
- config/transformer_lstm_yolo.yaml
- README.md

## Getting started
- Install dependencies: PyTorch, NumPy, PyYAML
- Run training: python train_transformer_lstm_yolo.py --config config/transformer_lstm_yolo.yaml


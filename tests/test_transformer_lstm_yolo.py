import torch
from src.model.transformer_lstm_yolo import TransformerLSTYOLO

def main():
    model = TransformerLSTYOLO(input_dim=6, d_model=128, nhead=4, num_encoder_layers=2, horizon=12, lstm_hidden=128)
    model.eval()
    x = torch.randn(4, 32, 6)  # B, T, C
    with torch.no_grad():
        out = model(x)
    if isinstance(out, tuple):
        forecast, anom = out
        print("forecast shape:", forecast.shape)
        print("anom shape:", anom.shape)
        assert forecast.shape == (4, 12)
        assert anom.shape == (4, 1)
        print("forward pass OK")
    else:
        print("Output:", out)

if __name__ == "__main__":
    main()

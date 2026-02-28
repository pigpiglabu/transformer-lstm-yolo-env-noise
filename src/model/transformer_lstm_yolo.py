import torch
import torch.nn as nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))
    def forward(self, x):
        seq_len = x.size(1)
        return x + self.pe[:, :seq_len, :]

class TransformerLSTYOLO(nn.Module):
    def __init__(self, input_dim, d_model=256, nhead=8, num_encoder_layers=4, horizon=12, lstm_hidden=256, max_len=512, dropout=0.1):
        super().__init__()
        self.input_proj = nn.Linear(input_dim, d_model)
        self.pos = PositionalEncoding(d_model, max_len=max_len)
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward=d_model*4, dropout=dropout, activation="relu")
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_encoder_layers)
        self.lstm = nn.LSTM(d_model, lstm_hidden, batch_first=True)
        self.horizon = horizon
        self.fc_forecast = nn.Linear(lstm_hidden, horizon)
        self.fc_anom = nn.Linear(lstm_hidden, 1)
        self.grid_size = 8
    def forward(self, x):
        # x: [B, T, input_dim]
        B, T, _ = x.size()
        x = self.input_proj(x)
        x = self.pos(x)
        # Transformer expects [T, B, D] by default; adapt for batch_first
        x = x.permute(1, 0, 2)  # [T, B, D]
        x = self.transformer(x)  # [T, B, D]
        x = x.permute(1, 0, 2)  # [B, T, D]
        # Simple temporal collapse for forecasting horizon using last token
        x = self.lstm(x)[0][:, -1, :]  # [B, lstm_hidden]
        forecast = self.fc_forecast(x)  # [B, horizon]
        anom = self.fc_anom(x)  # [B, 1]
        return forecast, anom

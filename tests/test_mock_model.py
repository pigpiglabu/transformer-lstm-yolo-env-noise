import numpy as np

class MockTransformerLSTYOLO:
    def __init__(self, horizon=12):
        self.horizon = horizon
    def forward(self, x):
        B, T, C = x.shape
        forecast = np.zeros((B, self.horizon), dtype=float)
        anom = np.ones((B, 1), dtype=float)
        return forecast, anom

def main():
    model = MockTransformerLSTYOLO(12)
    x = np.random.randn(4, 32, 6)
    f, a = model.forward(x)
    print("forecast shape:", f.shape)
    print("anom shape:", a.shape)

if __name__ == "__main__":
    main()

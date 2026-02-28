import sys

def main():
    B = 4
    horizon = 12
    forecast = [[0.0 for _ in range(horizon)] for _ in range(B)]
    anomaly = [[0.0] for _ in range(B)]
    print("forecast shape:", (len(forecast), len(forecast[0])))
    print("anom shape:", (len(anomaly), len(anomaly[0])))
    assert len(forecast) == B and len(forecast[0]) == horizon
    assert len(anomaly) == B and len(anomaly[0]) == 1
    print("shape test passed")

if __name__ == "__main__":
    main()

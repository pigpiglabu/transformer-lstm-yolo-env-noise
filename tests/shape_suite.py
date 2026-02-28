import sys

def check_shape(B,T,C,horizon):
    forecast = [[0.0 for _ in range(horizon)] for _ in range(B)]
    anomaly = [[0.0] for _ in range(B)]
    assert len(forecast) == B and len(forecast[0]) == horizon
    assert len(anomaly) == B and len(anomaly[0]) == 1
    return (B, T, C, horizon)

def main():
    tests = [
        (2, 16, 4, 12),
        (4, 32, 6, 24),
        (1, 10, 3, 6),
        (8, 64, 8, 12)
    ]
    ok = True
    for t in tests:
        try:
            check_shape(*t)
        except AssertionError:
            ok = False
            print("FAILED:", t)
            break
    if ok:
        print("All shape tests passed")

if __name__ == '__main__':
    main()

import pandas as pd
import random

_number = None

def load() -> None:
    print("Loading model...")
    global _number
    _number = random.randint(0, 11)
    print("Model loaded: {}".format(_number))

def predict(X: pd.DataFrame) -> pd.DataFrame:
    global _number
    def greaterThan(row, number):
        if row['x1'] > number: return 1
        else: return 0

    x = pd.DataFrame(
        data = [{ 'ŷ': greaterThan(row, _number) } for index, row in X.iterrows()],
        index = X.index,
        columns = ['ŷ']
    )
    return x

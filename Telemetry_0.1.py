import pandas as pd
import matplotlib.pyplot as plt
import json

with open("Spa_F458_IT.json", "r") as f:
    lap = json.load(f)


for key in lap.keys():
    print(lap[key])

import pandas as pd
from pandas import DataFrame
import json

with open('appstore_books150.json') as f:
    appContent = json.load(f)

keys = appContent['results'][0].keys()

print(keys)

df = pd.DataFrame(columns=keys)

for i in range(len(appContent['results'])):

    for k in keys:
        if k in appContent['results'][i]:
            appContent['results'][i][k] = str(appContent['results'][i][k])

    df = df.append(appContent['results'][i], ignore_index=True)

df.to_csv('appstore_books150.csv', sep=',', encoding='utf-8')

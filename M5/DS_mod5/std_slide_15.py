import pandas as pd
import numpy as np

d = {'odd': np.arange(1, 100, 2), 'even': np.arange(0, 100, 2)}
print(d['odd'])
print(d['even'])
df = pd.DataFrame(d)
print(df.std())
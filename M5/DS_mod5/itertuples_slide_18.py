import pandas as pd
import numpy as np

df =pd.DataFrame(np.random.rand(5, 4), columns=['col1', 'col2', 'col3', 'col4'])
for row in df.itertuples():
    print(row)
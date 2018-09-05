import pandas as pd
import numpy as np

df =pd.DataFrame(np.random.rand(5, 4), columns=['col1', 'col2', 'col3', 'col4'])
for key, value in df.iteritems():
    print(key, value)
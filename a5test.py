
import pandas as pd
import numpy as np


df=pd.read_csv("F:\\joan\\joan_0121.csv")
ef=pd.pivot_table(df,index=["bd"],columns=["tt"],aggfunc=np.sum)
ef.to_csv('10.csv')







import numpy as np
import pandas as pd
import streamlit as st

scores_array = np.random.randint(50,high=101,size=(50,5))
student_dataFrame = pd.DataFrame(data=scores_array,
                                 columns=["國文","英文","數學","地理","社會"],
                                 index=range(1,51))
student_dataFrame
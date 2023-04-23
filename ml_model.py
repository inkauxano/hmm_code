import numpy as np

def transform_data(data):
  k=5
  data = data
  data['pass'] = data['pass']*np.log(k)
  return data
  

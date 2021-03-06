# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

# Enter Code Here
def get_total_extras():
    ipl_matches_array = read_ipl_data_csv(path, dtype='|S50')
    extras= ipl_matches_array[:,17]
    extras=extras.astype(int)
    return np.sum (extras)

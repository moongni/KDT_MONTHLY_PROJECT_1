from typing import Tuple, Dict
import os
import json

import numpy as np
import pandas as pd

from sklearn.preprocessing import OrdinalEncoder


DataFrame = pd.DataFrame
DROP_LIST = ["FP16 GFLOPS", "FP32 GFLOPS", "FP64 GFLOPS"]
path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path, 'data')

# 전처리함수
def preprocessing() -> Tuple[DataFrame, DataFrame, Dict]:
    ## data prepare
    data = pd.read_csv(os.path.join(path, 'chip_dataset.csv'), index_col=0)
    data['Release Date'] = pd.to_datetime(data['Release Date'])
    data = data.sort_values(by='Release Date', ascending=True).reset_index(drop=True)
    data.drop(columns=DROP_LIST, inplace=True)

    ## null value
    data['Process Size (nm)'].fillna(method="ffill", inplace=True)
    data['TDP (W)'].fillna(data['TDP (W)'].mean(), inplace=True)
    data['Die Size (mm^2)'].fillna(method='ffill', axis=0, inplace=True)
    data['Die Size (mm^2)'].fillna(data['Die Size (mm^2)'].mean(), inplace=True)
    data['Transistors (million)'].fillna(method='ffill', inplace=True)
    data['Transistors (million)'].fillna(data['Transistors (million)'].mean(), inplace=True)

    ## categorical -> numeric 
    info = {}
    numeric_data = data.copy()
    type_mapping = {'CPU':0, 'GPU':1}
    info['Type'] = type_mapping
    numeric_data['Type'] = numeric_data['Type'].map(type_mapping)

    encoder = OrdinalEncoder()
    numeric_data['Foundry'] = encoder.fit_transform(numeric_data['Foundry'].to_numpy().reshape(-1, 1)).reshape(-1)
    info['Foundry'] = {value: i for i, value in enumerate(encoder.categories_[0])}

    encoder = OrdinalEncoder()
    numeric_data['Vendor'] = encoder.fit_transform(numeric_data['Vendor'].to_numpy().reshape(-1, 1)).reshape(-1)
    info['Vendor'] = {value: i for i, value in enumerate(encoder.categories_[0])}

    return data, numeric_data, info


if __name__=="__main__":
    cat_data, num_data, num_info = preprocessing()

    ## save preprocessed data
    cat_data.to_csv(os.path.join(path, 'categorical_data.csv'))
    num_data.to_csv(os.path.join(path, 'numeric_data.csv'))

    with open(os.path.join(path, 'numberic_data_info.json'), 'w') as f:
        json.dump(num_info, f, indent='\t')
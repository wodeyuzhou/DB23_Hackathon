import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

train = pd.read_csv("../data/train.csv", index_col=0)
test = pd.read_csv("../data/test.csv", index_col=0)

data = pd.concat([train, test], axis=0)
data.index = pd.to_datetime(data.index)

data['year'] = data.index.year
data['month'] = data.index.month
data['day'] = data.index.day
data['weekday'] = data.index.weekday
data['dayofweek'] = data.index.dayofweek 
data['hour'] = data.index.hour
data['year_season'] = data['year'] + data['season'] / 10

test_start = '2012-12-01'
train_data = data[data.index < test_start].copy()
test_data = data[data.index >= test_start].copy()

train_data['cnt_log'] = np.log(train_data['cnt'] + 1)

by_season = train_data.groupby('year_season')['cnt'].median()
by_season = by_season.rename('count_season')

train_data = train_data.join(by_season, on='year_season')
test_data = test_data.join(by_season, on='year_season')

regs = {"gbdt": GradientBoostingRegressor(random_state=0),
        "rf": RandomForestRegressor(random_state=0, n_jobs=-1)}

features = ['season', 'holiday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'year', 'hour', 'dayofweek', 'count_season']

preds = {}
for name, reg in regs.items():
    if name == 'gbdt':
        reg.set_params(n_estimators=1000, min_samples_leaf=6)
    elif name == 'rf':
        reg.set_params(n_estimators=1000, min_samples_leaf=2)

    reg.fit(train_data[features], train_data['cnt_log'])
    
    preds[name] = reg.predict(test_data[features])
    preds[name] = np.exp(preds[name]) - 1 
test_pred = 0.5 * preds['gbdt'] + 0.5 * preds['rf']
test_pred[test_pred < 0] = 0 

submission_df = pd.read_csv('../data/sample_submission.csv')
submission_df['cnt'] = test_pred
submission_df.to_csv('../submission/final_submission.csv', index=False)
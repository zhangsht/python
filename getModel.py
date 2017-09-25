import xgboost as xgb
import numpy as np

dtrain = xgb.DMatrix('../get_train_data1.txt')
dtest = xgb.DMatrix('../get_train_data2.txt')
param = {'objective':'binary:logistic', 'eta': 0.08, 'max_depth':5}
watchlist = [(dtest,'eval'), (dtrain,'train')]
num_round = 1100
bst = xgb.train(param, dtrain, num_round, watchlist)
bst.save_model("bst.model")

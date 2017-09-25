import xgboost as xgb
import numpy as np
# read in data

#y = np.loadtxt('get_train_data1.txt')
train_data = xgb.DMatrix('../train_data.txt')
dtrain = train_data[0:180000, :]
dtest = train_data[180000:, :]
# specify parameters via map
param = {'objective':'binary:logistic' }
watchlist = [(dtest,'eval'), (dtrain,'train')]
num_round = 100
bst = xgb.train(param, dtrain, num_round, watchlist)
bst.save_model("bst.model")

# make prediction
# test_data = xgb.DMatrix('get_test_data.txt')
# preds = bst.predict(test_data)
# outing = open("predict_text_data", "w")
# outing.write(preds)
# outing.close()
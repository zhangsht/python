import xgboost as xgb
import numpy as np
# read in data

#y = np.loadtxt('get_train_data1.txt')
dtrain = xgb.DMatrix('train_data.txt')
# specify parameters via map
param = {'objective':'binary:logistic' }
num_round = 100
bst = xgb.train(param, dtrain, num_round)
bst.save_model("bst_model")
# make prediction

# dtest = xgb.DMatrix('get_test_data.txt')
# preds = bst.predict(dtest, ntree_limit=bst.best_ntree_limit)
# np.savetxt('predict_text_data', preds, delimiter='\n')
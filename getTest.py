import xgboost as xgb
import numpy as np

dtest = xgb.DMatrix('../get_test_data.txt')
bst = xgb.Booster()
bst.load_model("bst.model")
preds = bst.predict(dtest)
print(preds.shape)
np.savetxt("pridict_text_data.txt", preds, delimiter='\n')
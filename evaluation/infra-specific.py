from sklearn.metrics import accuracy_score, recall_score, precision_score
from xgboost import XGBRegressor
import pandas as pd


train_dataset_filename = "../dataset/infra-specific-medium/train.csv"
test_dataset_filename = "../dataset/infra-specific-medium/test.csv"

feature_list = ["GW_devCount_vs_appCount", "GW_devCount_vs_compCount", "GW_upwardBW_vs_appCount", "GW_resCap_vs_demand", "ES_devCount_vs_appCount", "ES_devCount_vs_compCount", "ES_upwardBW_vs_appCount", "ES_resCap_vs_demand"]
target_column_name = "is_fail"

train_dataset = pd.read_csv(train_dataset_filename)
x_train = train_dataset[feature_list].to_numpy()
y_train = train_dataset[target_column_name].to_numpy()


hyper_parameters = dict(
    n_estimators=40,
    max_depth=6,
    learning_rate=0.1,
    silent=False,
    tree_method="exact",
    objective="reg:logistic",
)

predictor = XGBRegressor(**hyper_parameters)
predictor.fit(
    x_train,
    y_train,
    verbose=True,
)

test_dataset = pd.read_csv(test_dataset_filename)
pred_values = predictor.predict(test_dataset[feature_list].to_numpy())

predictions_binary = [1 if p > 0.5 else 0 for p in pred_values]

accuracy = accuracy_score(test_dataset[target_column_name].to_numpy(), predictions_binary)
print(accuracy)

recall = recall_score(test_dataset[target_column_name].to_numpy(), predictions_binary)
print(recall)

precision = precision_score(test_dataset[target_column_name].to_numpy(), predictions_binary)
print(precision)

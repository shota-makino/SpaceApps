from sknn.mlp import Regressor, Layer
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import RandomizedSearchCV, GridSearchCV
import sklearn.cross_validation as skcv
import sklearn.metrics as skm
import scipy.stats as stats
import pickle

X, y = make_regression(n_samples = 100, n_features=100, n_informative=20, n_targets=1)

X_train, X_test, y_train, y_test = skcv.train_test_split(X, y, test_size=0.40, random_state=42)
scaler = StandardScaler()  
scaler.fit(X_train)  
X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test) 

nn = Regressor(
    layers=[
        Layer("Linear", units=50),
        Layer("Linear")],
    learning_rate=0.02,
    n_iter=10)

gs = GridSearchCV(nn, param_grid={
    'learning_rate': [0.05, 0.01, 0.005, 0.001],
    'hidden0__units': [4, 8, 12, 30, 50],
    'hidden0__type': ["Sigmoid", "Tanh"]})
gs.fit(X_train, y_train)

pickle.dump(nn, open('nn.pkl', 'wb'))

y_pred = gs.predict(X_test)

print("Neural network R^2:\n%s\n" % (skm.r2_score(y_test, y_pred)))

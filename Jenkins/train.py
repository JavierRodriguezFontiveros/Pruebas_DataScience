from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Cargar dataset de iris
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Guardar modelo entrenado
joblib.dump(model, 'model.pkl')
print("Modelo entrenado y guardado.")
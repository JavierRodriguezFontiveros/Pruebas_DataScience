import joblib
from sklearn.datasets import load_iris

def test_model():
    model = joblib.load('model.pkl')
    data = load_iris()
    
    # Verificar que el modelo pueda hacer predicciones
    pred = model.predict([data.data[0]])
    assert pred is not None, "El modelo no está generando predicciones"
    
    print("✅ Prueba exitosa: el modelo hace predicciones correctamente.")

if __name__ == "__main__":
    test_model()

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
<<<<<<< HEAD
X, y, test_size=0.2, random_state=42)
=======
  X, y, test_size=0.2, random_state=42)
>>>>>>> 01f790578fbbc45ce20f7a86fe45b88d8958ea7a

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
<<<<<<< HEAD
print(f"Model Accuracy: {accuracy:.2f}")
=======
print(f"Model Accuracy: {accuracy:.2f}")
>>>>>>> 01f790578fbbc45ce20f7a86fe45b88d8958ea7a

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Loadin the dataset from CSV file
dataset_path = "heart-disease.csv"
df = pd.read_csv(dataset_path)

#Printing the dataset structure
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Splitting dataset into features (X) and target variable (y)
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Splitting into training and testing sets
test_size = 49 % 40
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

# Identifying categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns

# Creating a ColumnTransformer to apply one-hot encoding to categorical columns
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_cols)
    ],
    remainder='passthrough'
)

# Creating a pipeline with the preprocessor and the decision tree classifier
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier())
])

# Training the model on the training set
pipeline.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = pipeline.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Printing evaluation metrics
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

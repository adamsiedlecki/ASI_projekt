import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Car_Prices_Poland_Kaggle.csv")

print("Brakujące wartości:\n", df.isnull().sum())

encoder = LabelEncoder()
df['mark'] = encoder.fit_transform(df['mark'])
df['model'] = encoder.fit_transform(df['model'])
df['generation_name'] = encoder.fit_transform(df['generation_name'])
df['fuel'] = encoder.fit_transform(df['fuel'])
df['city'] = encoder.fit_transform(df['city'])
df['province'] = encoder.fit_transform(df['province'])

# Obliczamy korelację
corr = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Macierz korelacji")
plt.subplots_adjust(left=0.2, right=0.95, top=0.9, bottom=0.3)
plt.show()


# Podział na cechy i zmienną docelową
X = df.drop('price', axis=1)
y = df['price']

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


model = RandomForestRegressor(n_jobs=-1,
                              random_state=42)

model.fit(X_train, y_train)

# Predykcje
y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

# Ewaluacja
print(f"\nMAE test: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MAE training: {mean_absolute_error(y_train, y_train_pred):.2f}")

# Zapis modelu
joblib.dump(model, 'car_prices_model.pkl')

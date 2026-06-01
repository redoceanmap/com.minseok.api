import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text


class RoseModel:

    def __init__(self, df: pd.DataFrame):
        self.model = DecisionTreeClassifier()
        self._X_train, self._X_test, self._y_train, self._y_test = self._prepare_data(df)
        self.model.fit(self._X_train, self._y_train)

    def _prepare_data(self, df: pd.DataFrame):
        df = df[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]].dropna().copy()
        df["Sex"] = LabelEncoder().fit_transform(df["Sex"])
        X = df.drop("Survived", axis=1)
        y = df["Survived"]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def get_model(self) -> str:
        return type(self.model).__name__

    def get_accuracy(self) -> float:
        y_pred = self.model.predict(self._X_test)
        return float(round(accuracy_score(self._y_test, y_pred), 4))

    def get_tree(self) -> str:
        return export_text(self.model, feature_names=self._X_train.columns.tolist())

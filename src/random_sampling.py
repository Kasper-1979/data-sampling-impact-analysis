import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from collections import Counter

columns_to_use = [
    'Flow Duration', 'Tot Fwd Pkts', 'TotLen Fwd Pkts',
    'Fwd Pkt Len Max', 'Fwd Pkt Len Min', 'Label'
]

print("[INFO] Wczytywanie danych...")
data = pd.read_csv('C:/Users/hp/Downloads/archive/02-21-2018.csv', usecols=columns_to_use)
data = data.dropna()

data['Flow Duration'] = data['Flow Duration'].astype('float32')
data['Tot Fwd Pkts'] = data['Tot Fwd Pkts'].astype('int32')
data['TotLen Fwd Pkts'] = data['TotLen Fwd Pkts'].astype('float32')
data['Fwd Pkt Len Max'] = data['Fwd Pkt Len Max'].astype('float32')
data['Fwd Pkt Len Min'] = data['Fwd Pkt Len Min'].astype('float32')

print("[INFO] Losowe próbkowanie całego zbioru...")
data = data.sample(n=10000, random_state=42)

X = data.drop('Label', axis=1).values
y = data['Label'].values

print(f"[INFO] Rozmiar danych przed podziałem: {X.shape}")
print(f"[INFO] Rozkład klas:\n{Counter(y)}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

indices = np.arange(X_scaled.shape[0])
np.random.seed(42)
np.random.shuffle(indices)

split_point = int(0.7 * len(indices))
train_idx = indices[:split_point]
test_idx = indices[split_point:]

X_train = X_scaled[train_idx]
y_train = y[train_idx]
X_test = X_scaled[test_idx]
y_test = y[test_idx]

def entropy(y):
    counter = Counter(y)
    total = len(y)
    return -sum((count / total) * np.log2(count / total) for count in counter.values() if count > 0)

def split(X_column, value):
    left = X_column <= value
    right = X_column > value
    return left, right

def best_split(X, y):
    best_gain = -1
    best_feat = None
    best_val = None
    base_entropy = entropy(y)

    n_features = X.shape[1]
    y = np.array(y)

    for feature_index in range(n_features):
        sorted_idx = np.argsort(X[:, feature_index])
        X_sorted = X[sorted_idx, feature_index]
        y_sorted = y[sorted_idx]

        left_counts = Counter()
        right_counts = Counter(y_sorted)
        total = len(y_sorted)

        for i in range(1, total):
            c = y_sorted[i - 1]
            left_counts[c] += 1
            right_counts[c] -= 1

            if X_sorted[i] == X_sorted[i - 1]:
                continue

            left_size = i
            right_size = total - i

            p_left = left_size / total
            p_right = 1 - p_left

            ent_left = -sum(
                (count / left_size) * np.log2(count / left_size)
                for count in left_counts.values() if count > 0
            )
            ent_right = -sum(
                (count / right_size) * np.log2(count / right_size)
                for count in right_counts.values() if count > 0
            )

            gain = base_entropy - (p_left * ent_left + p_right * ent_right)

            if gain > best_gain:
                best_gain = gain
                best_feat = feature_index
                best_val = (X_sorted[i] + X_sorted[i - 1]) / 2

    return best_feat, best_val

class TreeNode:
    def __init__(self, feature=None, value=None, left=None, right=None, *, label=None):
        self.feature = feature
        self.value = value
        self.left = left
        self.right = right
        self.label = label

class MyDecisionTree:
    def __init__(self, max_depth=7, min_samples_split=10):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        print("[INFO] Rozpoczynam budowę drzewa...")
        self.tree = self._build_tree(X, np.array(y), 0)
        print("[INFO] Budowa drzewa zakończona.")

    def _build_tree(self, X, y, depth):
        num_samples_per_class = Counter(y)
        most_common = num_samples_per_class.most_common(1)[0][0]

        if (depth >= self.max_depth or len(set(y)) == 1 or len(y) < self.min_samples_split):
            return TreeNode(label=most_common)

        feat, val = best_split(X, y)
        if feat is None:
            return TreeNode(label=most_common)

        left_idx, right_idx = split(X[:, feat], val)
        left = self._build_tree(X[left_idx], y[left_idx], depth + 1)
        right = self._build_tree(X[right_idx], y[right_idx], depth + 1)

        return TreeNode(feature=feat, value=val, left=left, right=right)

    def predict_one(self, x, node):
        while node.label is None:
            if x[node.feature] <= node.value:
                node = node.left
            else:
                node = node.right
        return node.label

    def predict(self, X):
        return np.array([self.predict_one(x, self.tree) for x in X])

tree = MyDecisionTree(max_depth=7, min_samples_split=10)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

print("\n=== WYNIKI DRZEWA DECYZYJNEGO ===")
print(classification_report(y_test, y_pred))
accuracy = accuracy_score(y_test, y_pred)
print(f"[INFO] Accuracy: {accuracy:.4f}\n")

print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

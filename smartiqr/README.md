# SmartIQR 📊

SmartIQR is a simple Machine Learning utility library to automatically calculate IQR (Interquartile Range) and detect outliers from data.

It works with Python lists and Pandas Series.

---

## 🚀 Installation (Local)

Clone the repository:

git clone https://github.com/vishakha-python772200/smartiqr.git

Then go inside folder and install:

pip install .

---

## 📦 Usage

from smartiqr import analyze_iqr

data = [10, 12, 14, 15, 18, 100]

result = analyze_iqr(data)

print(result)

---

## ✅ Output Includes

- Q1 (First Quartile)
- Q3 (Third Quartile)
- IQR Value
- Lower Bound
- Upper Bound
- Outliers List

---

## 👩‍💻 Author

Vishakha Badgujar

---

## 📄 License

MIT License

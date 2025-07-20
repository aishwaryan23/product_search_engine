# 🛍️ Product Search Engine

A Streamlit-powered **Product Recommendation System** that helps users discover similar electronics based on the selected product. Using machine learning similarity metrics, the app recommends top alternatives and displays their images and prices in a modern web interface.

----
## Preview
 
<img width="1915" height="933" alt="image" src="https://github.com/user-attachments/assets/23e8717b-7a86-4225-bb89-16d39527dd3c" />

---

## 🔍 Features

- 📦 **Product-Based Recommendations**: Select a product and get the top 10 most similar items.
- 🖼️ **Image & Price Display**: See each product's image and actual price for easy comparison.
- ⚡ **Fast & Lightweight**: Uses pre-computed similarity scores from a machine learning model.
- 💡 **Clean UI**: Built using Streamlit with sidebar controls and a responsive layout.
- 🧠 **Model & Data**: Includes pickled similarity matrix and electronics dataset.

---

## 🧑‍💻 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Data Processing**: `pandas`, `numpy`
- **Model Persistence**: `pickle`

---

## 📁 Folder Structure

```bash
📦 ProductSearchEngine/
├── test.py # Main Streamlit app
├── similarity.pkl # Precomputed similarity matrix
├── data.pkl # Product data (names, images, prices)
└── README.md # Project documentation
```
## ▶️ Getting Started

### 1. **Clone the repository**

```bash
git clone https://github.com/your-username/ProductSearchEngine.git
cd ProductSearchEngine
```

### 2. Install Dependencies
``` bash
pip install streamlit pandas numpy requests 
```

### 3. Run App
```bash
streamlit run test.py
```
### 🧠 How it Works
The app loads the electronics dataset and a cosine similarity matrix.

When a product is selected, it:

Finds its index in the dataset.

Retrieves top 10 most similar products based on the similarity matrix.

Filters out results with broken image links.

Displays each result with product name, image, and price.




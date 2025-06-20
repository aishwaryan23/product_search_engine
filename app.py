import streamlit as st
import pandas as pd
import numpy as np
import pickle

electronics = pickle.load(open('data.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))

def recommender(product):
    electronics_index = electronics[electronics['name']==product].index[0]
    similarity_list = list(enumerate(similarity[electronics_index]))
    top_10_similar_product = sorted(similarity_list,key= lambda x:x[1],reverse=True)[1:5]

    similar_product = []
    for idx,similarly in top_10_similar_product:
        product_info={
            'name':electronics.loc[idx]['name'],
            'image':electronics.loc[idx]['image'],
            'actual_price':electronics.loc[idx]['actual_price']
        }

        similar_product.append(product_info)
    return similar_product

st.title("Product Search Engine")

product_name = st.sidebar.selectbox('Select a product: ',electronics['name'])

if st.sidebar.button('Search'):
    search_product = recommender(product_name)
    st.write(f"Top 10 recommended for -> {product_name}")

    for rec in search_product:
        st.image(rec['image'], width=150)
        st.write(f"**{rec['name']}**")
        st.write(f"**{rec['actual_price']}**")
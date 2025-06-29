# app.py

import streamlit as st
import pandas as pd
import re
from rapidfuzz import fuzz

# -------------------------------
# Cleaning function
# -------------------------------
def clean_company_name(name):
    name = str(name).lower()
    name = re.sub(r'[^\w\s]', '', name)
    remove_words = ['inc', 'llc', 'ltd', 'corporation', 'corp', 'limited', 'pvt', 'pvt ltd', 'plc']
    for word in remove_words:
        name = re.sub(r'\b' + word + r'\b', '', name)
    name = name.replace('technologies', 'tech')
    name = name.replace('technology', 'tech')
    name = re.sub(r'\sai$', '', name)
    name = re.sub(' +', ' ', name)
    name = name.strip()
    return name

# -------------------------------
# Streamlit App
# -------------------------------
st.title("🔎 Company Deduplication Tool")
st.write("""
Upload a CSV file with **any columns**.  
Select the column containing company names, and this app will clean and deduplicate them using fuzzy matching.
""")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("✅ **Uploaded Data Sample:**")
    st.write(df.head())
    
    # Let user select the company name column
    company_column = st.selectbox("Select the company name column:", df.columns)
    
    if company_column:
        # Cleaning
        df['clean_company_name'] = df[company_column].apply(clean_company_name)
        
        # Fuzzy Matching with original names retained for output
        duplicates = []
        for i in range(len(df)):
            name1_clean = df.loc[i, 'clean_company_name']
            name1_orig = df.loc[i, company_column]
            
            for j in range(i+1, len(df)):
                name2_clean = df.loc[j, 'clean_company_name']
                name2_orig = df.loc[j, company_column]
                
                similarity = fuzz.ratio(name1_clean, name2_clean)
                if similarity >= 85:
                    # Append original names in Title Case + similarity
                    duplicates.append((str(name1_orig).title(), str(name2_orig).title(), similarity))
        
        # Convert duplicates list to dataframe for viewing
        dup_df = pd.DataFrame(duplicates, columns=['Company 1', 'Company 2', 'Similarity'])
        
        st.write("🔁 **Potential Duplicates:**")
        st.write(dup_df)
        
        # Download option
        csv = dup_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Duplicates CSV",
            data=csv,
            file_name='duplicate_companies.csv',
            mime='text/csv',
        )

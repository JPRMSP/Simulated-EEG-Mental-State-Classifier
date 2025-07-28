import streamlit as st
import numpy as np
import pandas as pd

# Page settings
st.set_page_config(page_title="Simulated EEG Classifier", page_icon="🧠")

# Title and Description
st.title("🧠 Simulated EEG Mental State Classifier")
st.markdown("""
This app simulates EEG signals and classifies the mental state as either **Relaxed** 🧘 or **Concentrated** ⚡  
based on simple signal analysis.  
Click the button below to begin!
""")

# Simulate EEG on button click
if st.button("🔁 Start EEG Simulation"):
    # Simulate EEG: 4 channels × 100 time samples
    eeg_data = np.random.randint(400, 700, (100, 4))
    df = pd.DataFrame(eeg_data, columns=["Channel 1", "Channel 2", "Channel 3", "Channel 4"])

    # Display the first few rows
    st.subheader("📊 Simulated EEG Data (First 5 Rows)")
    st.dataframe(df.head())

    # Display line chart of signals
    st.subheader("📈 EEG Signal Plot")
    st.line_chart(df)

    # Simple classification logic
    avg_value = df.values.mean()
    st.subheader("🧮 Analysis Result")
    st.write(f"**Average Signal Value:** {avg_value:.2f}")

    if avg_value < 550:
        st.success("🧘 Predicted Mental State: Relaxed")
    else:
        st.success("⚡ Predicted Mental State: Concentrated")

# Footer
st.markdown("---")
st.caption("Project by: Your Name | Subject: FI1912 – Human-Computer Interaction and Usability Engineering")

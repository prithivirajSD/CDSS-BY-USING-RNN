import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def about_page():
    st.markdown(
        """
        <h2 style="text-align: center;">About Clinical Decision Support System (CDSS)</h2>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    Predictive analytics is revolutionizing healthcare, enabling faster and more accurate disease diagnosis. 
    This project leverages advanced deep learning models like Bidirectional LSTM to analyze patient symptoms and medical history, providing reliable predictions for clinical decision-making.
    """)

    # Benefits Section
    st.markdown("### Benefits of CDSS")
    st.markdown("""
    - **Improved Diagnostic Precision**: Enhances the accuracy of disease diagnosis.
    - **Clinician Support**: Assists in treatment planning with data-driven predictions.
    - **Time Efficiency**: Processes extensive medical data swiftly.
    - **Better Patient Outcomes**: Reduces diagnostic errors, improving overall care.
    """)

    st.markdown("### How It Works")
    st.markdown("""
    - **Data Preprocessing**: Handles 132 attributes representing patient symptoms and medical indicators.
    - **Deep Learning Models**: Utilizes Bidirectional LSTM for sequential data analysis.
    - **Evaluation**: Ensures performance through metrics like accuracy, precision, recall, and F1-score.
    """)

    st.markdown(" ### Data Visualizations")

    count_plot_path = "images/count_plot.png"
    pair_plot_path = "images/pair_plot.png"

    col1, col2 = st.columns(2)

    with col1:
        st.image(count_plot_path, caption="Count Plot", use_column_width=True)

    with col2:
        st.image(pair_plot_path, caption="Pair Plot", use_column_width=True)

    st.markdown("### Learn More")
    st.markdown("""
    - **Model Architecture**:
        - Input Layer: Processes 132 features representing symptoms.
        - Bidirectional LSTM Layers: Captures forward and backward dependencies.
        - Dense Layer: Extracts meaningful features for predictions.
        - Output Layer: Uses softmax activation to classify diseases.
    - **Training & Evaluation**:
        - Loss Function: Categorical Cross-Entropy.
        - Metrics: Accuracy, precision, recall, F1-score.
        - Testing: Cross-validation ensures generalizability.
    """)
    
    if st.button("View Model Workflow"):
        st.image("images/workflow.png", caption="CDSS Workflow", use_column_width=True)


    st.markdown("### Share Your Feedback")
    col1, col2, col3 = st.columns([1, 2, 1]) 

    with col2:
        name = st.text_input("Your Name:")
        email = st.text_input("Your Email:")
        message = st.text_area("Your Feedback:")

        if st.button("Submit"):
            if name and email and message:
                feedback_data = {"Name": name, "Email": email, "Message": message}
                feedback_df = pd.DataFrame([feedback_data])
                feedback_df.to_csv("data/feedback.csv", mode="a", index=False, header=False)
                st.success("Thank you for your feedback!")
            else:
                st.warning("Please fill in all fields.")



    st.markdown("---")
    st.markdown("""
    <hr style='border:1px solid gray'>
    <p style='text-align: center;'>© 2025 CDSS | Contact: <a href="mailto:arrchith26@gmail.com" style="text-decoration: none; color: gray;">arrchith26@gmail.com</a></p>
    """, unsafe_allow_html=True)
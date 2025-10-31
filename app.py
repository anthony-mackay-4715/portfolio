import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Capstone Portfolio",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 2.5 rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 2rem;
    }
    .project-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    /* Center only the profile section's middle column and its image */
    #profile-section div[data-testid="column"]:nth-child(2) {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #profile-section div[data-testid="stImage"] { text-align: center; }
    #profile-section div[data-testid="stImage"] img { display: block; margin: 0 auto; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Anthony Mackay</div>', unsafe_allow_html=True)

# Profile section with image and bio
st.markdown('<div id="profile-section">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    try:
        image = Image.open('Profile.jpg')
        st.image(image, width=450)
    except:
        st.info("📷 Add your profile image as 'profile.jpg' in the same directory")

    st.markdown("""
    ### About Me
    
    I'm a passionate student with a strong interest in solving complex data problems. 
    Through my coursework and personal projects, I've developed skills in data acquisition, 
    data cleaning, data analysis, and statistical modeling. I love building solutions that help businesses 
    and organizations make data-driven decisions.
    
    **Skills:** Python, SQL, Machine Learning, Web Development, Big Data Analysis
    
    **Contact:** anthonymackay2022@outlook.com | [GitHub](https://github.com/anthony-mackay-4715)
    """)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Projects Section
st.markdown("## 🚀 Featured Projects")

# Project 1
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Luxury Watch Pricing Analysis Dashboard")
        st.markdown("""
        A comprehensive data visualization dashboard built with Python and Streamlit. 
        This project analyzes luxury watch prices from a popular reselling site and provides interactive visualizations 
        to help users understand trends and patterns in the watch market.
        
        **Technologies:** Python, Pandas, Plotly, Streamlit
        
        **Key Features:**
        - Interactive data filtering
        - Real-time visualizations
        - Export functionality
        """)
    
    with col2:
        st.markdown("#### Link to project repository")
        st.link_button("📁 GitHub Repository", "https://github.com/anthony-mackay-4715/data-360-final-proj")

    st.markdown('</div>', unsafe_allow_html=True)

# Project 2
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🤖 Bitcoin Price Prediction Machine Learning Model")
        st.markdown("""
        A machine learning model that predicts Bitcoin prices using historical data.
        The model achieves a daily mean absolute error of < $100 on the test set.
        
        **Technologies:** Python, Scikit-learn, Pandas
        
        **Key Features:**
        - Model training pipeline
        - Hyperparameter optimization
        """)
    
    with col2:
        st.markdown("#### Link to project repository")
        st.link_button("📁 GitHub Repository", "https://github.com/anthony-mackay-4715/BTC-Machine-Learning-Model")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with Streamlit | © 2024 Your Name</p>
    </div>
""", unsafe_allow_html=True)
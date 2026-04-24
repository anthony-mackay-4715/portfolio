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
        font-size: 2.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 2rem;
        color: #1a1a2e;
    }
    .project-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .reflection-box {
        background-color: #dce6f5;
        border-left: 4px solid #2c5fa8;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin-top: 1rem;
        color: #1a1a2e;
    }
    .reflection-box strong {
        color: #1a1a2e;
    }
    /* Center profile image */
    #profile-section div[data-testid="stImage"] { text-align: center; }
    #profile-section div[data-testid="stImage"] img { display: block; margin: 0 auto; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Anthony Mackay</div>', unsafe_allow_html=True)

# Profile section — image left, about me right (wider)
st.markdown('<div id="profile-section">', unsafe_allow_html=True)
col_img, col_bio = st.columns([1, 2.5])

with col_img:
    try:
        image = Image.open('Profile.jpg')
        st.image(image, width=300)
    except:
        st.info("📷 Add your profile image as 'Profile.jpg' in the same directory")

with col_bio:
    st.markdown("""
    ### About Me

    Hi, I'm Anthony Mackay. I'm a business operations analyst at Lendio, a fintech company where I turn complex data into clear, actionable insights for leadership.

    My work spans dashboarding, data visualization, and customer analytics — whatever helps the business make smarter, data-driven decisions. Recently, I played a key role on a team that resegmented our entire customer base. That work was implemented company-wide and drove a **10% increase in customer conversion**.

    I'm wrapping up my Computer Science degree with a Data Science minor at Westminster University, and I'm eager to bring that same analytical approach to new challenges upon graduation this spring!

    **Skills:** Python, SQL, Machine Learning, Web Development, Big Data Analysis, Algorithmic Trading

    **Contact:** anthonymackay2022@outlook.com | [GitHub](https://github.com/anthony-mackay-4715)
    """)

    try:
        with open("resume.pdf", "rb") as f:
            st.download_button(
                label="Download Resume",
                data=f,
                file_name="Anthony_Mackay_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.info("Add your resume as 'resume.pdf' in the project directory to enable the download button.")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Projects Section
st.markdown("## Featured Projects")

# Project 1 — Luxury Watch Pricing
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Luxury Watch Pricing Analysis Dashboard")
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
        st.markdown("""
        <div class="reflection-box">
        <strong>Reflections & Lessons Learned</strong><br><br>
        This project was my first serious dive into building a full end-to-end data product, from raw web-scraped data all the way to a polished, interactive dashboard.
        The biggest challenge was learning Plotly and Streamlit from scratch simultaneously while managing a messy, inconsistent dataset.
        I quickly discovered that real-world data is rarely clean, and that the visualization layer is only as good as the data pipeline behind it.
        Pushing through that friction taught me how to debug data transformation issues methodically and deliver something that genuinely looked and felt professional.
        By the end, I was proud to have a deployable app that a non-technical user could pick up and use without any guidance. That was the bar I set for myself, and hitting it felt like a real milestone.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Project Repository")
        st.link_button("📁 GitHub Repository", "https://github.com/anthony-mackay-4715/data-360-final-proj")

    st.markdown('</div>', unsafe_allow_html=True)

# Project 2 — Bitcoin ML Model
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Bitcoin Price Prediction Machine Learning Model")
        st.markdown("""
        A machine learning model that predicts Bitcoin prices using historical data.
        The model achieves a daily mean absolute error of < $100 on the test set.

        **Technologies:** Python, Scikit-learn, Pandas

        **Key Features:**
        - Model training pipeline
        - Hyperparameter optimization
        """)
        st.markdown("""
        <div class="reflection-box">
        <strong>Reflections & Lessons Learned</strong><br><br>
        Predicting cryptocurrency prices is a humbling problem; the market does not reward overconfidence.
        My early models looked great on training data and fell apart on anything unseen, which forced me to truly internalize the concept of overfitting and why rigorous validation matters.
        Learning to implement a proper time-series train/test split (rather than a random one) was a turning point that made my results honest.
        I also had to become comfortable with the uncomfortable truth that a MAE under $100 on Bitcoin is still just a starting point, not a finished product.
        That honesty shaped how I communicate model results today, always pairing a metric with its limitations rather than leading with the headline number.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### Project Repository")
        st.link_button("📁 GitHub Repository", "https://github.com/anthony-mackay-4715/BTC-Machine-Learning-Model")

    st.markdown('</div>', unsafe_allow_html=True)

# Project 3 — Senior Capstone: Algo Trading Platform
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Algorithmic Trading Platform — Senior Capstone Project")
        st.markdown("""
        A full-stack algorithmic trading platform built as my senior capstone, featuring a profitable automated trading strategy
        composed of multiple coordinated sub-strategies. The system executes live and paper trades through the Alpaca API,
        with a React frontend for monitoring positions and performance, and a Python backend for strategy logic and execution.

        **Technologies:** Python, React, Alpaca API, REST APIs

        **Key Features:**
        - Multiple composable sub-strategies with independent signal logic
        - Live and paper trading via Alpaca brokerage API
        - React dashboard for real-time position and P&L monitoring
        - Backtesting pipeline to validate strategy profitability before deployment
        """)
        st.markdown("""
        <div class="reflection-box">
        <strong>Reflections & Lessons Learned</strong><br><br>
        This was the most technically ambitious project I've undertaken, and it required me to grow in multiple directions at once.
        I came in comfortable with Python but had to learn React from the ground up to build a frontend worthy of a real trading dashboard.
        Bridging a Python backend to a React UI taught me how to think about systems holistically, not just in isolated scripts.
        Integrating the Alpaca API introduced me to the realities of working with live financial data: rate limits, websocket streams,
        and the unforgiving precision required when placing real orders. The hardest problem was designing sub-strategies that work
        independently but don't conflict with each other when running simultaneously, which required careful thought around
        position sizing, signal priority, and risk management.
        Delivering a system that is genuinely profitable in paper trading, not just functional in theory, was the standard I held myself to,
        and meeting it gave me a deep appreciation for what it takes to bridge academic concepts and real-world execution.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Project 4 — Jungle Jump
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Jungle Jump — Educational Math Game")
        st.markdown("""
        A full-stack educational math game built collaboratively in Software Engineering class.
        Designed for elementary school teachers and students, the app reinforces math concepts taught in class
        through an engaging, interactive game format.

        **Technologies:** TypeScript, Deno Fresh Framework

        **Key Features:**
        - Interactive math challenges targeting elementary curriculum concepts
        - Teacher and student-facing views
        - Built and delivered as a functioning full-stack web application by a collaborative team
        """)
        st.markdown("""
        <div class="reflection-box">
        <strong>Reflections & Lessons Learned</strong><br><br>
        Jungle Jump was my first real exposure to full-stack development, and it came with a steep but rewarding learning curve.
        Learning the Deno Fresh framework and TypeScript simultaneously while also navigating team collaboration meant I had to move fast and lean on my teammates when I hit walls.
        The experience taught me how to contribute meaningfully to a shared codebase without breaking others' work, and how important clear communication is when multiple people are building the same product.
        Shipping something polished enough for actual use in a classroom set a high bar for the team. Knowing that real teachers and students might interact with what we built pushed me to care about the quality of the final product in a way that a purely academic exercise never quite does.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Project 5 — Borrower/Lender Recommendation (SVD)
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Borrower-Lender Recommendation System — Numerical Linear Algebra")
        st.markdown("""
        A solo project completed for Numerical Analysis (Math 362) applying SVD matrix factorization
        to a 2.2 million row Lending Club dataset from Kaggle. The system decomposes a borrower-lender
        interaction matrix into latent factors and uses the reconstruction to recommend the best-fit lender
        for each borrower based on predicted loan amounts.

        **Technologies:** Python, NumPy, SciPy, Pandas, Scikit-learn, Seaborn

        **Key Features:**
        - SVD-based matrix factorization on a 2.2M row real-world dataset
        - Borrower-lender matching via latent factor similarity
        - RMSE of $245.65 and MAE of $4.73 on loan amount predictions
        - Heatmap visualizations comparing original vs. predicted borrower-purpose matrices
        """)
        st.markdown("""
        <div class="reflection-box">
        <strong>Reflections & Lessons Learned</strong><br><br>
        This project challenged me to take a concept from a linear algebra classroom and apply it to a problem with real financial stakes.
        SVD had always felt abstract until I used it to make actual predictions on a dataset with over two million rows, at which point the power of matrix decomposition became concrete and intuitive.
        Working solo on a dataset this large also forced me to think carefully about computational efficiency: naive approaches that worked on small samples would grind to a halt at scale.
        The most satisfying moment was seeing the reconstructed matrix converge on the original values with a MAE under $5, which validated that the mathematical theory translated cleanly into a working system.
        More broadly, this project deepened my appreciation for numerical methods as a practical engineering tool, not just an academic exercise.
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with Streamlit | © 2025 Anthony Mackay</p>
    </div>
""", unsafe_allow_html=True)

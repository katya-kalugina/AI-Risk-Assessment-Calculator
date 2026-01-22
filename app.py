import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- CONFIG ---
st.set_page_config(page_title="AI Risk Calculator", layout="wide")

st.title("AI Risk Assessment Calculator (EDPB/FRASP)")
st.markdown("""
This tool operationalizes the **EDPB SPE 2025** methodology for assessing the probability and severity of AI risks.
It features a deterministic scoring engine with integrated **'Stopper Rules'** for absolute rights protection.
""")

# --- TABS FOR INPUT ---
tab1, tab2, tab3 = st.tabs(["1. Probability Factors", "2. Severity Factors", "3. Risk Report"])

# --- TAB 1: PROBABILITY ---
with tab1:
    st.header("Assess Probability (Likelihood)")
    st.info("Score each factor from 1 (Unlikely) to 4 (Very High).")
    
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.slider("1. Frequency of Use (Daily vs Annual)", 1, 4, 2)
        p2 = st.slider("2. Exposure to High-Risk Scenarios", 1, 4, 2)
        p3 = st.slider("3. Historical Precedents / Failures", 1, 4, 1)
        p4 = st.slider("4. Environmental & Regulatory Factors", 1, 4, 2)
    with col2:
        p5 = st.slider("5. System Robustness (Redundancy)", 1, 4, 2)
        p6 = st.slider("6. Data Quality & Integrity", 1, 4, 2)
        p7 = st.slider("7. Human Oversight Effectiveness", 1, 4, 2)

    prob_score = (p1 + p2 + p3 + p4 + p5 + p6 + p7) / 7
    st.metric("Aggregate Probability Score", f"{prob_score:.2f}")

# --- TAB 2: SEVERITY ---
with tab2:
    st.header("Assess Severity (Impact)")
    st.warning("Stopper Rule: If any critical factor is Level 4, the total Severity becomes 4.")
    
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        st.markdown("**Critical Factors (Stopper Rules)**")
        s1 = st.selectbox("1. Nature of the Right (Life/Dignity)", [1, 2, 3, 4])
        s2 = st.selectbox("2. Nature of Data (Special Categories)", [1, 2, 3, 4])
        s3 = st.selectbox("3. Category of Data Subject (Minors/Vulnerable)", [1, 2, 3, 4])
        s4 = st.selectbox("4. Purpose of Processing (Legitimacy)", [1, 2, 3, 4])
        s5 = st.selectbox("5. Scale of Impact (>100k people)", [1, 2, 3, 4])
        s7 = st.selectbox("7. Reversibility of Harm", [1, 2, 3, 4])
        s8 = st.selectbox("8. Duration of Harm (Permanent?)", [1, 2, 3, 4])

    with s_col2:
        st.markdown("**Contextual Factors**")
        s6 = st.selectbox("6. Contextual Sensitivity", [1, 2, 3, 4])
        s9 = st.selectbox("9. Velocity to Materialize", [1, 2, 3, 4])
        s10 = st.selectbox("10. Accountability Mechanisms", [1, 2, 3, 4])
        s11 = st.selectbox("11. Ripple & Cascading Effects", [1, 2, 3, 4])

    # Applying the Stopper Rule logic
    stoppers = [s1, s2, s3, s4, s5, s7, s8]
    if any(s == 4 for s in stoppers):
        final_severity = 4
        st.error("STOPPER RULE TRIGGERED: Final Severity set to 4 (Very Significant)")
    else:
        final_severity = max([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11])

# --- TAB 3: FINAL REPORT ---
with tab3:
    st.header("Final Risk Determination")
    
    # Mapping logic for the Matrix
    prob_level = 1
    if prob_score > 3.5: prob_level = 4
    elif prob_score > 2.5: prob_level = 3
    elif prob_score > 1.5: prob_level = 2
    
    # Risk Matrix Result
    # Matrix: Prob rows, Sev cols
    matrix = [
        ["Low", "Low", "Medium", "Very High"],      # Prob 1
        ["Low", "Medium", "High", "Very High"],     # Prob 2
        ["Low", "High", "Very High", "Very High"],  # Prob 3
        ["Medium", "High", "Very High", "Very High"] # Prob 4
    ]
    
    result = matrix[prob_level-1][final_severity-1]
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.subheader("Risk Scorecard")
        st.write(f"**Final Probability Level:** {prob_level}")
        st.write(f"**Final Severity Level:** {final_severity}")
        
        if result == "Very High":
            st.error(f"FINAL RISK: {result}")
        elif result == "High":
            st.warning(f"FINAL RISK: {result}")
        else:
            st.success(f"FINAL RISK: {result}")
            
    with res_col2:
        # Mini Heatmap logic
        df_hm = pd.DataFrame([
            {"P": p, "S": s, "Risk": matrix[p-1][s-1]} 
            for p in range(1, 5) for s in range(1, 5)
        ])
        fig = px.scatter(df_hm, x="S", y="P", color="Risk", 
                         color_discrete_map={"Low": "green", "Medium": "yellow", "High": "orange", "Very High": "red"},
                         size_max=30, title="Your Risk Position on the Matrix")
        # Add current point
        fig.add_scatter(x=[final_severity], y=[prob_level], marker=dict(size=25, color='black', symbol='x'), name="Current")
        st.plotly_chart(fig, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Ekaterina Kalugina. Based on EDPB 2025 Guidelines.")

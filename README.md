# AI Risk Assessment Calculator

A deterministic risk-scoring engine designed to operationalize the **EDPB SPE Programme** guidelines (2025) and the **FRASP** (Functional Rights AI Assessment & Scoring Protocol).

[**📊 Launch Risk Calculator**](ВСТАВЬТЕ_ССЫЛКУ_ОТ_STREAMLIT_ЗДЕСЬ)

## Project Overview
This tool provides a structured interface for evaluating the probability and severity of privacy and fundamental rights risks in AI systems. It transitions from qualitative descriptions to a quantitative scoring model while maintaining legal rigor.

### Key Functional Features:
- **Probability Assessment:** Multi-factor scoring based on usage frequency, historical precedents, and system robustness.
- **Severity Modeling:** Granular evaluation of impact on natural persons across 11 dimensions.
- **Automated 'Stopper' Logic:** Integrated override that sets overall severity to Level 4 (Very Significant) if critical factors—such as human dignity or physical safety—are severely impacted.
- **Risk Matrix Visualization:** Real-time mapping of current system status onto the probability/severity heatmap.

## Research & Compliance Context
Developed to support DPOs and AI researchers in conducting robust impact assessments (DPIA/FRIA). The methodology strictly follows the March 2025 recommendations of the European Data Protection Board (EDPB) Pool of Experts.

## Technical Implementation
- **Logic:** Rule-based scoring engine.
- **Stack:** Python, Streamlit, Plotly (Data Visualization).

---
*Developed by Ekaterina Kalugina. Part of the AI Governance Toolkit project.*

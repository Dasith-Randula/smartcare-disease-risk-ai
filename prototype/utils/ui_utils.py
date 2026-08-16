import streamlit as st

def apply_custom_css():
    """Injects custom CSS for glassmorphism and 3D effects based on active theme."""
    is_dark = st.session_state.get('theme', 'Light') == 'Dark'

    if is_dark:
        bg_color = "#000000"
        card_bg = "rgba(17,30,48,0.82)"
        text_primary = "#FFFFFF"
        border_color = "rgba(139,114,248,0.2)"
    else:
        bg_color = "#FFFFFF"
        card_bg = "rgba(255,255,255,0.78)"
        text_primary = "#000000"
        border_color = "rgba(108,92,231,0.12)"

    css = f"""
    <style>
    .stApp {{
        background: {bg_color};
        background-image: radial-gradient(at 0% 0%, rgba(108,92,231,0.1) 0px, transparent 50%),
                          radial-gradient(at 100% 0%, rgba(34,184,207,0.1) 0px, transparent 50%);
        color: {text_primary};
    }}
    .glass-card {{
        background: {card_bg};
        backdrop-filter: blur(12px);
        border: 1px solid {border_color};
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }}
    .glass-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
    }}
    .orb-container {{
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
    }}
    .orb {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #7e948a, #7e948a);
        box-shadow: 0 20px 40px rgba(126, 148, 138, 1), inset -20px -20px 40px rgba(0,0,0,0.2);
        animation: float 4s ease-in-out infinite;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 22px;
        font-weight: 600;
        letter-spacing: 0.08em;
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-20px) rotate(5deg); }}
        100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 20px; color: #9399a3; font-size: 14px;'>
        SmartCare AI | Disease Risk Prediction System<br>
        AI Powered. Data Driven. Better Decisions.
    </div>
    """, unsafe_allow_html=True)
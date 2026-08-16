import streamlit as st

def apply_custom_css():
    """Injects custom CSS for themed glassmorphism and consistent contrast."""
    is_dark = st.session_state.get('theme', 'Light') == 'Dark'
    
    if is_dark:
        bg_color = "#060a12"
        card_bg = "rgba(16,24,38,0.86)"
        text_primary = "#edf4ff"
        text_muted = "#b8c5dc"
        border_color = "rgba(116,204,176,0.26)"
        accent = "#74ccb0"
        accent_soft = "rgba(116,204,176,0.22)"
        button_bg = "#74ccb0"
        button_text = "#081115"
        line_color = "rgba(184,197,220,0.28)"
        sidebar_bg = "linear-gradient(180deg, #0d1727 0%, #0a1220 100%)"
        sidebar_border = "rgba(116,204,176,0.24)"
        nav_text = "#e7f1ff"
        nav_hover = "rgba(116,204,176,0.18)"
        nav_active = "rgba(116,204,176,0.28)"
    else:
        bg_color = "#f4f8fb"
        card_bg = "rgba(255,255,255,0.88)"
        text_primary = "#1d2a39"
        text_muted = "#4c6075"
        border_color = "rgba(86,177,148,0.24)"
        accent = "#3f8e75"
        accent_soft = "rgba(63,142,117,0.16)"
        button_bg = "#3f8e75"
        button_text = "#ffffff"
        line_color = "rgba(29,42,57,0.18)"
        sidebar_bg = "linear-gradient(180deg, #eef3fb 0%, #e7eef9 100%)"
        sidebar_border = "rgba(29,42,57,0.14)"
        nav_text = "#1d2a39"
        nav_hover = "rgba(63,142,117,0.14)"
        nav_active = "rgba(63,142,117,0.24)"

    css = f"""
    <style>
    :root {{
        --sc-bg: {bg_color};
        --sc-card-bg: {card_bg};
        --sc-text: {text_primary};
        --sc-text-muted: {text_muted};
        --sc-border: {border_color};
        --sc-accent: {accent};
        --sc-accent-soft: {accent_soft};
        --sc-button-bg: {button_bg};
        --sc-button-text: {button_text};
        --sc-line: {line_color};
        --sc-sidebar-bg: {sidebar_bg};
        --sc-sidebar-border: {sidebar_border};
        --sc-nav-text: {nav_text};
        --sc-nav-hover: {nav_hover};
        --sc-nav-active: {nav_active};
    }}
    .stApp {{
        background: var(--sc-bg);
        background-image: radial-gradient(at 0% 0%, rgba(108,92,231,0.1) 0px, transparent 50%),
                          radial-gradient(at 100% 0%, rgba(34,184,207,0.1) 0px, transparent 50%);
        color: var(--sc-text);
    }}
    .stApp p,
    .stApp li,
    .stApp span,
    .stApp label,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6,
    .stApp div {{
        color: var(--sc-text);
    }}
    .glass-card {{
        background: var(--sc-card-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--sc-border);
        border-radius: 14px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }}
    .glass-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
    }}

    .section-eyebrow {{
        color: var(--sc-accent) !important;
        letter-spacing: 0.08em;
        font-weight: 700;
        text-transform: uppercase;
    }}
    .muted-text {{
        color: var(--sc-text-muted) !important;
    }}
    .insight-title {{
        color: var(--sc-accent) !important;
    }}
    .flow-text {{
        color: var(--sc-text-muted) !important;
    }}
    .metric-title {{
        color: var(--sc-accent) !important;
        margin: 0;
    }}
    .danger-title {{
        color: #e85d68 !important;
    }}
    .prediction-card {{
        text-align: center;
        border-top: 5px solid var(--sc-accent);
    }}

    [data-testid="stMarkdownContainer"] hr {{
        border: none;
        border-top: 1px solid var(--sc-line);
    }}

    .stButton > button,
    .stFormSubmitButton > button,
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondary"] {{
        color: var(--sc-button-text) !important;
        background: var(--sc-button-bg) !important;
        border: 1px solid color-mix(in srgb, var(--sc-button-bg), #000 18%) !important;
        font-weight: 700 !important;
    }}
    .stButton > button:hover,
    .stFormSubmitButton > button:hover,
    [data-testid="stBaseButton-primary"]:hover,
    [data-testid="stBaseButton-secondary"]:hover {{
        filter: brightness(1.05);
        transform: translateY(-1px);
    }}

    [data-testid="stSidebar"] {{
        background: var(--sc-sidebar-bg);
        border-right: 1px solid var(--sc-sidebar-border);
    }}
    [data-testid="stSidebar"] * {{
        color: var(--sc-nav-text) !important;
    }}
    [data-testid="stSidebar"] hr {{
        border: none;
        border-top: 1px solid var(--sc-sidebar-border);
    }}

    [data-testid="stSidebarNav"] {{
        padding-top: 0.2rem;
    }}
    [data-testid="stSidebarNav"] ul {{
        gap: 0.36rem;
    }}
    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] button {{
        border-radius: 12px !important;
        padding: 0.46rem 0.68rem !important;
        border: 1px solid transparent !important;
        color: var(--sc-nav-text) !important;
        transition: all 0.2s ease !important;
    }}
    [data-testid="stSidebarNav"] a:hover,
    [data-testid="stSidebarNav"] button:hover {{
        background: var(--sc-nav-hover) !important;
        border-color: var(--sc-sidebar-border) !important;
        transform: translateX(2px);
    }}
    [data-testid="stSidebarNav"] a[aria-current="page"],
    [data-testid="stSidebarNav"] button[aria-current="page"] {{
        background: var(--sc-nav-active) !important;
        border-color: var(--sc-sidebar-border) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        font-weight: 700 !important;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
        color: var(--sc-nav-text) !important;
    }}

    /* Decorated medical mark */
    .med-mark-wrap {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        position: relative;
    }}
    .med-mark-core {{
        width: 138px;
        height: 138px;
        border-radius: 50%;
        background: radial-gradient(circle at 28% 25%, #9be3cb, #3f8e75 72%);
        box-shadow: 0 26px 46px rgba(63, 142, 117, 0.33), inset -12px -12px 24px rgba(6, 10, 18, 0.28);
        display: flex;
        justify-content: center;
        align-items: center;
        color: #f7fffc;
        font-size: 52px;
        font-weight: 800;
        z-index: 2;
        animation: medFloat 5s ease-in-out infinite;
    }}
    .med-mark-core::before,
    .med-mark-core::after {{
        content: "";
        position: absolute;
        border-radius: 50%;
        border: 1px solid var(--sc-accent-soft);
        inset: -14px;
        animation: pulseRing 2.8s ease-out infinite;
        z-index: 1;
    }}
    .med-mark-core::after {{
        inset: -28px;
        animation-delay: 1.4s;
    }}
    .med-mark-dot {{
        position: absolute;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #8be6c8;
        box-shadow: 0 0 18px rgba(139, 230, 200, 0.8);
    }}
    .dot-a {{ top: 78px; left: 20%; animation: orbitA 7s linear infinite; }}
    .dot-b {{ top: 52px; right: 19%; animation: orbitB 6s linear infinite; }}
    .dot-c {{ bottom: 64px; left: 62%; animation: orbitC 8s linear infinite; }}

    @keyframes medFloat {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-14px); }}
        100% {{ transform: translateY(0px); }}
    }}
    @keyframes pulseRing {{
        0% {{ transform: scale(0.92); opacity: 0.8; }}
        100% {{ transform: scale(1.16); opacity: 0; }}
    }}
    @keyframes orbitA {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(18px, -12px); }}
        100% {{ transform: translate(0, 0); }}
    }}
    @keyframes orbitB {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(-16px, 14px); }}
        100% {{ transform: translate(0, 0); }}
    }}
    @keyframes orbitC {{
        0% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(10px, -16px); }}
        100% {{ transform: translate(0, 0); }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class='muted-text' style='text-align: center; margin-top: 50px; padding: 20px; font-size: 14px;'>
        SmartCare AI | Disease Risk Prediction System<br>
        AI Powered. Data Driven. Better Decisions.
    </div>
    """, unsafe_allow_html=True)
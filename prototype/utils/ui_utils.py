import streamlit as st

def apply_custom_css():
    """Injects modern dashboard CSS with light/dark parity."""
    is_dark = st.session_state.get('theme', 'Light') == 'Dark'
    
    if is_dark:
        bg_color = "#0f1827"
        bg_accent = "radial-gradient(920px 540px at 92% -5%, rgba(53,210,167,0.16), transparent 62%), radial-gradient(860px 560px at -8% 112%, rgba(88,133,229,0.16), transparent 62%)"
        card_bg = "#152235"
        card_shadow = "0 16px 38px rgba(0, 0, 0, 0.34)"
        text_primary = "#e9eff8"
        text_muted = "#a7b8cf"
        border_color = "#2a3a50"
        accent = "#39c39a"
        accent_soft = "rgba(57,195,154,0.16)"
        button_bg = "#33b78f"
        button_text = "#07110d"
        line_color = "rgba(180,197,224,0.24)"
        sidebar_bg = "linear-gradient(180deg, #0f1f2f 0%, #0d1928 55%, #0a1623 100%)"
        sidebar_border = "#233347"
        nav_text = "#dce8f8"
        nav_hover = "rgba(57,195,154,0.14)"
        nav_active = "#1f6f5e"
        nav_active_text = "#f5fffb"
        panel_subtle = "#111d2e"
        input_bg = "#101c2d"
    else:
        bg_color = "#f6f8fb"
        bg_accent = "radial-gradient(900px 520px at 100% -8%, rgba(183,233,214,0.35), transparent 62%), radial-gradient(880px 560px at -10% 108%, rgba(203,220,247,0.35), transparent 62%)"
        card_bg = "#ffffff"
        card_shadow = "0 12px 28px rgba(16, 35, 57, 0.08)"
        text_primary = "#1f2a37"
        text_muted = "#6a7587"
        border_color = "#e6ebf2"
        accent = "#0f6b5a"
        accent_soft = "rgba(15,107,90,0.11)"
        button_bg = "#0f6b5a"
        button_text = "#ffffff"
        line_color = "rgba(31,42,55,0.12)"
        sidebar_bg = "#ffffff"
        sidebar_border = "#e7edf3"
        nav_text = "#354458"
        nav_hover = "#f3f7f6"
        nav_active = "#0f6b5a"
        nav_active_text = "#ffffff"
        panel_subtle = "#f3f7fa"
        input_bg = "#fbfdff"

    css = f"""
    <style>
    [data-testid="stAppViewContainer"],
    .stApp,
    .stApp * {{
        font-family: "Manrope", "Avenir Next", "Segoe UI", sans-serif;
    }}

    :root {{
        --sc-bg: {bg_color};
        --sc-bg-accent: {bg_accent};
        --sc-card-bg: {card_bg};
        --sc-card-shadow: {card_shadow};
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
        --sc-nav-active-text: {nav_active_text};
        --sc-panel-subtle: {panel_subtle};
        --sc-input-bg: {input_bg};
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    .stApp {{
        background: var(--sc-bg);
        background-image: var(--sc-bg-accent);
        color: var(--sc-text);
    }}

    .main .block-container {{
        max-width: 1200px;
        padding-top: 1.1rem;
        padding-bottom: 2.4rem;
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

    h1 {{
        font-size: clamp(2rem, 3.4vw, 3rem) !important;
        letter-spacing: -0.02em;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }}
    h2 {{
        letter-spacing: -0.015em;
    }}
    h3 {{
        letter-spacing: -0.01em;
    }}

    .glass-card {{
        background: var(--sc-card-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--sc-border);
        border-radius: 18px;
        padding: 24px;
        box-shadow: var(--sc-card-shadow);
        transition: all 0.3s ease;
        margin-bottom: 18px;
    }}
    .glass-card:hover {{
        transform: translateY(-4px);
    }}

    .surface-card {{
        background: var(--sc-panel-subtle);
        border: 1px solid var(--sc-border);
        border-radius: 18px;
        box-shadow: var(--sc-card-shadow);
        padding: 18px 20px;
        margin-bottom: 16px;
        margin-top: 2rem;
    }}
    .kpi-card {{
        border-radius: 16px;
        border: 1px solid var(--sc-border);
        box-shadow: var(--sc-card-shadow);
        padding: 18px;
        min-height: 118px;
        margin-top: 1rem;
    }}
    .kpi-blue {{ background: linear-gradient(135deg, rgba(157,210,245,0.32), rgba(157,210,245,0.14)); }}
    .kpi-pink {{ background: linear-gradient(135deg, rgba(236,184,232,0.32), rgba(236,184,232,0.12)); }}
    .kpi-green {{ background: linear-gradient(135deg, rgba(173,234,196,0.34), rgba(173,234,196,0.12)); }}
    .kpi-amber {{ background: linear-gradient(135deg, rgba(246,219,168,0.35), rgba(246,219,168,0.12)); }}
    .kpi-label {{
        font-size: 0.86rem;
        font-weight: 600;
        color: var(--sc-text-muted) !important;
    }}
    .kpi-value {{
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.1;
        margin-top: 0.35rem;
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

    .stTabs [data-baseweb="tab-list"] {{
        gap: 0.45rem;
        background: var(--sc-card-bg);
        border: 1px solid var(--sc-border);
        border-radius: 14px;
        padding: 0.35rem;
        width: fit-content;
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        font-weight: 600;
        color: var(--sc-text-muted);
        height: 2.3rem;
        padding: 0 0.95rem;
    }}
    .stTabs [aria-selected="true"] {{
        background: var(--sc-accent-soft) !important;
        color: var(--sc-text) !important;
    }}

    [data-testid="stForm"] {{
        background: var(--sc-card-bg);
        border: 1px solid var(--sc-border);
        border-radius: 18px;
        padding: 1rem 1rem 0.6rem 1rem;
        box-shadow: var(--sc-card-shadow);
    }}

    .stSelectbox > div > div,
    .stDateInput > div > div,
    .stNumberInput > div > div,
    .stTextInput > div > div,
    [data-baseweb="select"] > div {{
        background: var(--sc-input-bg) !important;
        border: 1px solid var(--sc-border) !important;
        border-radius: 12px !important;
    }}
    .stTextInput input,
    .stNumberInput input,
    .stDateInput input,
    [data-baseweb="select"] span {{
        color: var(--sc-text) !important;
    }}

    .stButton > button,
    .stFormSubmitButton > button,
    [data-testid="stBaseButton-primary"],
    [data-testid="stBaseButton-secondary"] {{
        color: var(--sc-button-text) !important;
        background: var(--sc-button-bg) !important;
        border: 1px solid color-mix(in srgb, var(--sc-button-bg), #000 18%) !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        min-height: 2.7rem;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
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
        padding-top: 0.25rem;
    }}
    [data-testid="stSidebarNav"] ul {{
        gap: 0.34rem;
    }}
    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] button {{
        border-radius: 12px !important;
        padding: 0.46rem 0.68rem !important;
        border: 1px solid var(--sc-sidebar-border) !important;
        color: var(--sc-nav-text) !important;
        transition: all 0.2s ease !important;
        font-weight: 600;
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
        border-color: var(--sc-nav-active) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
        font-weight: 700 !important;
    }}
    [data-testid="stSidebarNav"] a[aria-current="page"] *,
    [data-testid="stSidebarNav"] button[aria-current="page"] * {{
        color: var(--sc-nav-active-text) !important;
    }}

    [data-testid="stSidebar"] [role="radiogroup"] label {{
        color: var(--sc-nav-text) !important;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] > label {{
        background: color-mix(in srgb, var(--sc-nav-hover), #ffffff 45%);
        border: 1px solid var(--sc-sidebar-border);
        border-radius: 10px;
        padding: 0.35rem 0.55rem;
        margin-bottom: 0.3rem;
    }}

    .sidebar-brand {{
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.2rem;
    }}
    .brand-logo {{
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: var(--sc-accent-soft);
        border: 1px solid var(--sc-sidebar-border);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        color: var(--sc-accent) !important;
    }}
    .brand-title {{
        font-size: 1.12rem;
        font-weight: 800;
        color: var(--sc-nav-text) !important;
    }}
    .brand-subtitle {{
        margin-top: -0.15rem;
        margin-left: 2.65rem;
        color: color-mix(in srgb, var(--sc-nav-text), #ffffff 20%) !important;
        font-size: 0.84rem;
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
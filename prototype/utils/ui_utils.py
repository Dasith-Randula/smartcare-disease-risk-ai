import streamlit as st


def get_icon_svg(name, size=18, color="currentColor"):
    """Return a small inline SVG for common dashboard icons."""
    safe_name = (name or "info").lower().replace(" ", "_")

    svg_map = {
        "home": "<path d='M3 10.5 12 3l9 7.5M5.5 9.5V20h13V9.5' />",
        "info": "<circle cx='12' cy='12' r='9' /><path d='M12 10.5v5' /><circle cx='12' cy='7.5' r='1' />",
        "analytics": "<path d='M4 18V7m6 11V4m6 14v-8m4 8H4' />",
        "psychology": "<path d='M9 5.5A3.5 3.5 0 0 1 12.5 9v1.4a3.5 3.5 0 1 1-4 0V9A3.5 3.5 0 0 1 9 5.5Z' /><path d='M14.5 6.5c1.7 0 3 1.3 3 3v3.5c0 1.7-1.3 3-3 3h-1.2c-1.1 0-2.8-1.7-2.8-3.5V9.5c0-1.7 1.3-3 3-3h1Z' /><path d='M9 15.5v3M12 15.5v3M15 15.5v3' />",
        "query_stats": "<path d='M6 18V8m6 10V4m6 14v-7' /><path d='M3 18h18' />",
        "health_and_safety": "<path d='M12 21s-7.5-4.35-9.5-8.5C1.2 10.2 2.8 6 7.1 6c2.1 0 3.1 1.1 4.9 2.8C13.8 7.1 14.8 6 16.9 6c4.3 0 5.9 4.2 4.6 6.5C19.5 16.65 12 21 12 21Z' />",
        "stethoscope": "<path d='M7 4v5a5 5 0 0 0 10 0V4M7 8h10M9 18h6m-3 0v-3' /><path d='M5 8h2m10 0h2' />",
        "clinical_notes": "<path d='M7 4.5h8a3 3 0 0 1 3 3v11l-4-2.5-4 2.5-4-2.5-4 2.5v-11a3 3 0 0 1 3-3Z' /><path d='M9 9h6M9 12h6' />",
        "shield": "<path d='M12 3.5 18.5 6v6.2c0 4.5-2.8 7.4-6.5 9.3-3.7-1.9-6.5-4.8-6.5-9.3V6L12 3.5Z' /><path d='m9.5 12 1.7 1.7 3.3-4.2' />",
        "neurology": "<path d='M7 7.5A4.5 4.5 0 1 1 7 16.5a4.5 4.5 0 0 1 0-9Zm10 0A4.5 4.5 0 1 1 17 16.5a4.5 4.5 0 0 1 0-9Z' /><path d='M10 12h4' />",
        "hospital": "<path d='M4 20V6.5L12 3l8 3.5V20M8 20v-6h8v6M10 9h.01M14 9h.01M10 12h.01M14 12h.01' />",
        "monitor_heart": "<path d='M4 6.5A2.5 2.5 0 0 1 6.5 4h11A2.5 2.5 0 0 1 20 6.5v8A2.5 2.5 0 0 1 17.5 17H14l-1.5 3h-3L9 17H6.5A2.5 2.5 0 0 1 4 14.5v-8Z' /><path d='M8.5 12.5 10.5 10l2.2 2.2 2.8-4.2' />",
        "medical_services": "<path d='M8 10h8M10 8v4M14 8v4M6 16h12a2 2 0 0 0 2-2V7.5A1.5 1.5 0 0 0 18.5 6H5.5A1.5 1.5 0 0 0 4 7.5V14a2 2 0 0 0 2 2Z' /><path d='M12 18v3' />",
        "bar_chart": "<path d='M5 18V9m7 9V5m7 13v-7' /><path d='M3 18h18' />",
        "users": "<path d='M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm-5 9v-1.2A3.8 3.8 0 0 1 7.8 15h2.4A3.8 3.8 0 0 1 14 18.8V20M15 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm4 11v-1.2a3.8 3.8 0 0 0-3.2-3.7' />",
        "target": "<circle cx='12' cy='12' r='7' /><circle cx='12' cy='12' r='3.2' /><path d='M12 2v3M12 19v3M2 12h3M19 12h3' />",
        "default": "<circle cx='12' cy='12' r='8' /><path d='M12 7.5v5l3 2' />"
    }

    icon = svg_map.get(safe_name, svg_map["default"])
    return (
        f"<svg viewBox='0 0 24 24' width='{size}' height='{size}' fill='none' "
        f"stroke='{color}' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'>"
        f"{icon}</svg>"
    )


def apply_custom_css():
    """Centralized design system for the SmartCare dashboard."""
    is_dark = st.session_state.get("theme", "Light") == "Dark"

    if is_dark:
        bg = "#08111F"
        card = "rgba(17, 29, 48, 0.88)"
        text = "#F5F7FF"
        text_soft = "#A8B3C8"
        primary = "#34D399"
        lavender = "#059669"
        cyan = "#38CED0"
        border = "rgba(155, 171, 210, 0.16)"
        border_hover = "rgba(52, 211, 153, 0.38)"
        shadow = "0 18px 42px rgba(3, 7, 18, 0.26)"
        sidebar = "rgba(11, 18, 31, 0.82)"
        nav_inactive = "rgba(255,255,255,0.03)"
        nav_active = "linear-gradient(135deg, #34D399, #059669)"
        nav_hover = "linear-gradient(135deg, #059669, #34D399)"
        glow_primary = "rgba(52, 211, 153, 0.08)"
        glow_secondary = "rgba(5, 150, 105, 0.06)"
    else:
        bg = "#F6F8FD"
        card = "rgba(255,255,255,0.88)"
        text = "#16234A"
        text_soft = "#66738D"
        primary = "#10B981"
        lavender = "#059669"
        cyan = "#21C1C3"
        border = "rgba(72, 96, 165, 0.12)"
        border_hover = "rgba(16, 185, 129, 0.24)"
        shadow = "0 20px 55px rgba(61, 76, 130, 0.10)"
        sidebar = "rgba(255,255,255,0.78)"
        nav_inactive = "rgba(16,185,129,0.03)"
        nav_active = "linear-gradient(135deg, #10B981, #059669)"
        nav_hover = "linear-gradient(135deg, #059669, #10B981)"
        glow_primary = "rgba(16, 185, 129, 0.08)"
        glow_secondary = "rgba(5, 150, 105, 0.06)"

    css = f"""
    <style>
    :root {{
        --primary: {primary};
        --lavender: {lavender};
        --text: {text};
        --text-soft: {text_soft};
    }}

    [data-testid="stAppViewContainer"], .stApp {{
        font-family: "Inter", "Segoe UI", sans-serif;
        background: radial-gradient(circle at 18% 12%, {glow_primary}, transparent 26%), radial-gradient(circle at 82% 10%, {glow_secondary}, transparent 30%), radial-gradient(circle at 76% 78%, rgba(16,185,129,0.05), transparent 28%), {bg};
        color: {text};
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-image: radial-gradient(rgba(16,185,129,0.035) 1.1px, transparent 1.1px);
        background-size: 24px 24px;
        pointer-events: none;
        opacity: 1;
    }}

    .main .block-container {{ max-width: 1500px; padding-top: 1.15rem; padding-bottom: 2.2rem; }}
    .stHeader {{ background: transparent; }}
    h1, h2, h3, h4, h5, h6, p, li, span, div, label {{ color: {text}; }}
    h1 {{ font-size: clamp(3rem, 4vw, 4rem) !important; line-height: 1.05 !important; letter-spacing: -0.06em !important; font-weight: 800 !important; margin: 0 !important; }}
    h2 {{ font-size: clamp(2rem, 2.6vw, 2.8rem) !important; letter-spacing: -0.04em !important; font-weight: 700 !important; }}
    h3 {{ font-size: clamp(1.5rem, 2vw, 2.3rem) !important; font-weight: 600 !important; }}
    .glass-card, [data-testid="stForm"] {{ background: {card}; border: 1px solid {border}; border-radius: 22px; box-shadow: {shadow}; backdrop-filter: blur(14px); margin-bottom: 1.6rem; }}
    .chart-card {{ background: {card}; border: 1px solid {border}; border-radius: 22px; box-shadow: {shadow}; backdrop-filter: blur(14px); margin-bottom: 1.6rem; }}
    .glass-card {{ padding: 1.5rem 1.4rem; }}
    .section-eyebrow {{ display: block; font-size: 0.76rem; font-weight: 700; letter-spacing: 0.19em; text-transform: uppercase; color: {primary} !important; margin: 0 0 0.7rem 0; }}
    .hero-subtitle {{ margin-top: 0.5rem; margin-bottom: 1.4rem; font-size: clamp(1.5rem, 2vw, 2rem); font-weight: 600; color: #34415F; }}
    .hero-description {{ display: flex; align-items: center; gap: 0.9rem; background: rgba(255,255,255,.78); border: 1px solid rgba(85,105,165,.10); border-radius: 18px; padding: 1.1rem 1.2rem; box-shadow: 0 12px 30px rgba(56,72,120,.08); max-width: 540px; margin: 0 0 1.4rem 0; }}
    .hero-description .hero-icon {{ display: inline-flex; align-items: center; justify-content: center; width: 2.6rem; height: 2.6rem; border-radius: 12px; background: rgba(16,185,129,0.08); color: {primary}; }}
    .hero-description p {{ margin: 0; font-size: 1rem; color: {text_soft}; line-height: 1.5; }}
    .primary-cta, .stButton > button, .stFormSubmitButton > button {{ background: linear-gradient(135deg, {primary}, {lavender}) !important; color: white !important; border: none !important; border-radius: 14px !important; min-height: 3rem !important; padding: 0.75rem 1.7rem !important; font-weight: 700 !important; box-shadow: 0 12px 26px rgba(16,185,129,.22) !important; transition: transform .22s ease, box-shadow .22s ease, filter .22s ease !important; }}
    .primary-cta:hover, .stButton > button:hover, .stFormSubmitButton > button:hover {{ background: linear-gradient(135deg, {lavender}, {primary}) !important; color: white !important; transform: translateY(-3px) !important; box-shadow: 0 17px 35px rgba(16,185,129,.30) !important; filter: brightness(1.04) !important; }}
    .hero-scene {{ position: relative; display: flex; align-items: center; justify-content: center; height: 100%; min-height: 300px; perspective: 1200px; filter: drop-shadow(0 22px 28px rgba(74,100,190,0.14)); animation: heroFloat 6s ease-in-out infinite; }}
    .hero-platforms {{ position: relative; width: 310px; height: 220px; display: flex; align-items: center; justify-content: center; }}
    .hero-platform {{ position: absolute; bottom: 18px; width: 230px; height: 74px; border-radius: 28px; background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(198,217,255,0.18)); border: 1px solid rgba(117,142,220,0.16); box-shadow: inset 0 10px 18px rgba(255,255,255,0.8), 0 18px 46px rgba(84,112,200,0.12); transform: perspective(1000px) rotateX(72deg); }}
    .hero-platform.platform-back {{ width: 200px; bottom: 38px; background: linear-gradient(135deg, rgba(254,255,255,0.82), rgba(195,210,255,0.22)); }}
    .hero-cube-wrap {{ position: absolute; bottom: 52px; width: 170px; height: 170px; display: flex; align-items: center; justify-content: center; transform: rotateX(18deg) rotateY(-18deg); }}
    .hero-cube {{ width: 150px; height: 150px; border-radius: 26px; background: rgba(255,255,255,0.28); border: 1px solid rgba(102,148,255,0.30); box-shadow: inset 0 0 26px rgba(255,255,255,0.72), 0 16px 32px rgba(16,185,129,0.12); display: flex; align-items: center; justify-content: center; text-align: center; backdrop-filter: blur(10px); }}
    .hero-cube span {{ font-size: 3.1rem; font-weight: 800; letter-spacing: -0.05em; background: linear-gradient(135deg, {primary}, {lavender}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; color: transparent; }}
    .hero-object {{ position: absolute; width: 20px; height: 20px; border-radius: 14px; display: flex; align-items: center; justify-content: center; color: {primary}; background: rgba(255,255,255,0.82); border: 1px solid rgba(104,122,204,0.18); box-shadow: 0 12px 24px rgba(66,100,170,0.10); }}
    .hero-object.heart {{ left: 12%; top: 18%; width: 54px; height: 54px; border-radius: 18px; }}
    .hero-object.cross {{ right: 16%; top: 14%; width: 56px; height: 56px; border-radius: 18px; }}
    .hero-object.chart {{ right: 10%; bottom: 16%; width: 58px; height: 58px; border-radius: 18px; }}
    .hero-sphere {{ position: absolute; border-radius: 50%; background: rgba(255,255,255,0.7); box-shadow: 0 0 0 8px rgba(16,185,129,0.06); }}
    .hero-sphere.one {{ width: 16px; height: 16px; left: 14%; top: 22%; }}
    .hero-sphere.two {{ width: 18px; height: 18px; right: 12%; top: 28%; background: rgba(206,226,255,0.9); }}
    .hero-sphere.three {{ width: 14px; height: 14px; right: 24%; bottom: 18%; background: rgba(235,227,255,0.8); }}
    .hero-sphere.four {{ width: 20px; height: 20px; left: 20%; bottom: 16%; background: rgba(202,240,241,0.8); }}
    .page-header {{ display: flex; align-items: center; gap: 0.9rem; margin: 0.2rem 0 2rem; }}
    .page-header-icon {{ display: inline-flex; align-items: center; justify-content: center; width: 52px; height: 52px; border-radius: 16px; background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(5,150,105,0.06)); color: {primary}; border: 1px solid rgba(16,185,129,0.12); }}
    .page-header-copy {{ display: flex; flex-direction: column; gap: 0.2rem; }}
    .page-header-copy .page-eyebrow {{ font-size: 0.74rem; font-weight: 800; letter-spacing: 0.16em; text-transform: uppercase; color: {primary}; margin: 0; }}
    .page-header-copy h2 {{ margin: 0; font-size: clamp(1.8rem, 2.4vw, 2.5rem); letter-spacing: -0.05em; }}
    .page-header-copy p {{ margin: 0; color: {text_soft}; font-size: 1rem; }}
    .metric-section-title {{ margin: 2.2rem 0 1.1rem 0; font-size: clamp(1.8rem, 2.2vw, 2.5rem); font-weight: 700; letter-spacing: -0.04em; display: inline-block; position: relative; }}
    .metric-section-title::after {{ content: ""; position: absolute; left: 0; bottom: -9px; width: 132px; height: 4px; border-radius: 999px; background: linear-gradient(90deg, {primary}, {lavender}); }}
    .metric-card {{ position: relative; overflow: hidden; padding: 1.5rem 1.3rem; min-height: 160px; transition: all 0.25s ease; background: {card}; border: 1px solid {border}; border-radius: 22px; box-shadow: {shadow}; margin-bottom: 1.6rem; }}
    .metric-card:hover {{ transform: translateY(-6px); border-color: {border_hover}; box-shadow: 0 20px 42px rgba(16,185,129,.12); }}
    .metric-card::after {{ content: ""; position: absolute; right: -14px; bottom: -24px; width: 110px; height: 70px; border: 1px solid rgba(16,185,129,0.18); border-top-left-radius: 80px; border-top-right-radius: 80px; border-bottom: none; transform: rotate(-18deg); opacity: 0.45; }}
    .metric-icon {{ width: 58px; height: 58px; border-radius: 18px; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1rem; }}
    .metric-icon.blue {{ background: rgba(16,185,129,0.1); color: {primary}; }}
    .metric-icon.cyan {{ background: rgba(33,193,195,0.1); color: {cyan}; }}
    .metric-icon.purple {{ background: rgba(5,150,105,0.1); color: {lavender}; }}
    .metric-value {{ font-size: clamp(2rem, 2.5vw, 3rem); font-weight: 800; letter-spacing: -0.06em; margin: 0; line-height: 1; }}
    .metric-label {{ margin-top: 0.5rem; color: {text_soft} !important; font-size: 1rem; font-weight: 600; }}
    [data-testid="stSidebar"] {{ background: {sidebar}; border-right: 1px solid {border}; backdrop-filter: blur(18px); }}
    [data-testid="stSidebar"] * {{ color: {text} !important; }}
    [data-testid="stSidebarNav"] {{ padding-top: 0.4rem; }}
    [data-testid="stSidebarNav"] ul {{ gap: 0.54rem; }}
    [data-testid="stSidebarNav"] a, [data-testid="stSidebarNav"] button {{ border-radius: 14px !important; border: 1px solid {border} !important; padding: 0.7rem 0.8rem !important; background: transparent !important; transition: all 0.22s ease !important; font-weight: 600 !important; color: {text} !important; }}
    [data-testid="stSidebarNav"] a:hover, [data-testid="stSidebarNav"] button:hover {{ background: {nav_hover} !important; color: white !important; transform: translateX(4px); border-color: transparent !important; }}
    [data-testid="stSidebarNav"] a:hover *, [data-testid="stSidebarNav"] button:hover * {{ color: white !important; }}
    [data-testid="stSidebarNav"] a[aria-current="page"], [data-testid="stSidebarNav"] button[aria-current="page"] {{ background: {nav_active} !important; border: none !important; box-shadow: 0 12px 26px rgba(16,185,129,.18); color: white !important; }}
    [data-testid="stSidebarNav"] a[aria-current="page"] *, [data-testid="stSidebarNav"] button[aria-current="page"] * {{ color: white !important; }}
    .sidebar-brand {{ display: flex; align-items: center; gap: 0.75rem; padding: 0.1rem 0.2rem 0.5rem 0.2rem; }}
    .brand-logo {{ width: 40px; height: 40px; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, {primary}, {lavender}); color: white; box-shadow: 0 12px 24px rgba(16,185,129,.18); }}
    .brand-title {{ font-size: 1.15rem; font-weight: 800; }}
    .brand-subtitle {{ margin-left: 3.15rem; font-size: 0.8rem; color: {text_soft} !important; font-weight: 500; }}
    .sidebar-card {{ background: rgba(255,255,255,0.58); border: 1px solid {border}; border-radius: 18px; padding: 0.9rem 0.8rem; margin-top: 1rem; color: {text_soft}; font-size: 0.84rem; line-height: 1.5; }}
    [data-testid="stSidebar"] [role="radiogroup"] label {{ color: {text_soft}; }}
    [data-testid="stSidebar"] [role="radiogroup"] > label {{ background: rgba(255,255,255,0.5); border: 1px solid {border}; border-radius: 10px; padding: 0.38rem 0.55rem; }}
    [data-testid="stSidebar"] [role="radiogroup"] [aria-checked="true"] {{ background: linear-gradient(135deg, {primary}, {lavender}) !important; color: white !important; border-color: transparent !important; }}
    [data-testid="stForm"] {{ background: rgba(255,255,255,0.88); border-radius: 24px; border: 1px solid {border}; box-shadow: 0 14px 38px rgba(16,185,129,.08); padding: 1.2rem 1rem 0.8rem; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 0.5rem; padding: 0.35rem; border-radius: 16px; border: 1px solid {border}; background: rgba(255,255,255,0.54); }}
    .stTabs [data-baseweb="tab"] {{ border-radius: 12px !important; background: transparent; color: {text_soft}; font-weight: 600; padding: 0.5rem 1rem; }}
    .stTabs [aria-selected="true"] {{ background: linear-gradient(135deg, rgba(16,185,129,0.10), rgba(5,150,105,0.08)) !important; color: {text} !important; border: 1px solid rgba(16,185,129,0.18); }}
    .stTextInput > div > div, .stNumberInput > div > div, .stSelectbox > div > div, .stDateInput > div > div {{ background: #F4F7FC !important; border: 1px solid #E5EAF5 !important; border-radius: 12px !important; }}
    .stTextInput input, .stNumberInput input, .stSelectbox div[role="combobox"], .stDateInput input {{ color: {text} !important; background: transparent !important; }}
    .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox div[role="combobox"]:focus-within {{ border-color: #5984FF !important; box-shadow: 0 0 0 3px rgba(89,132,255,.11) !important; }}
    @keyframes heroFloat {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-10px); }} }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def render_page_header(title, subtitle, eyebrow=None, icon="info"):
    """Display a standard page heading inside the SmartCare design system."""
    eyebrow_html = f"<span class='page-eyebrow'>{eyebrow}</span>" if eyebrow else ""
    header_html = (
        f"<div class='page-header'>"
        f"<div class='page-header-icon'>{get_icon_svg(icon, 24, 'var(--primary)')}</div>"
        f"<div class='page-header-copy'>"
        f"{eyebrow_html}"
        f"<h2>{title}</h2>"
        f"<p>{subtitle}</p>"
        f"</div>"
        f"</div>"
    )
    st.markdown(header_html, unsafe_allow_html=True)


def render_footer():
    st.markdown(
        """
        <div style='text-align: center; margin-top: 42px; padding: 18px 12px 8px; color: var(--text-muted); font-size: 14px; border-top: 1px solid rgba(79,111,247,0.10);'>
            SmartCare AI | Disease Risk Prediction System<br>
            AI Powered. Data Driven. Better Decisions.
        </div>
        """,
        unsafe_allow_html=True,
    )

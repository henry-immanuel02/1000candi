import streamlit as st

st.set_page_config(page_title="1000 Candi untuk Jimmie", page_icon="🛕", layout="wide")

APP_PASSWORD = "jimmieandhenry"


def init_state():
    defaults = {
        "authenticated_candi": False,
        "candi_password_error": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_html_block(body: str, *, height: int | None = None):
    """Render pure HTML/CSS reliably across newer Streamlit versions."""
    if hasattr(st, "html"):
        try:
            st.html(body, width="stretch")
            return
        except TypeError:
            st.html(body)
            return

    # Fallback for older Streamlit.
    try:
        from streamlit.components.v1 import html as components_html
        components_html(body, height=height or 800, scrolling=True)
    except Exception:
        st.markdown(body, unsafe_allow_html=True)


STYLE_BLOCK = """
<style>
:root {
    --bg1: #0f0f10;
    --bg2: #171718;
    --card: rgba(255,255,255,0.055);
    --border: rgba(255,255,255,0.10);
    --text-soft: rgba(255,255,255,0.76);
    --text-faint: rgba(255,255,255,0.48);
}

.block-wrap {
    width: 100%;
}

.login-wrap {
    min-height: 72vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.login-card {
    width: min(480px, 92vw);
    background: linear-gradient(180deg, var(--bg2), var(--bg1));
    border: 1px solid var(--border);
    border-radius: 28px;
    padding: 34px 28px;
    text-align: center;
    box-shadow: 0 28px 80px rgba(0,0,0,0.34);
}

.login-icon {
    font-size: 3rem;
    margin-bottom: 8px;
}

.login-title {
    font-size: 2rem;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
    letter-spacing: 0.3px;
}

.login-subtitle {
    color: var(--text-soft);
    font-size: 1rem;
}

.hero {
    text-align: center;
    margin: 0 0 20px 0;
}

.hero h1 {
    margin: 0;
    font-size: 2.6rem;
    letter-spacing: 0.4px;
}

.hero p {
    margin: 8px 0 0 0;
    color: var(--text-soft);
    font-size: 1rem;
}

.grid-wrap {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(108px, 1fr));
    gap: 14px;
    align-items: stretch;
}

.candi-card {
    position: relative;
    min-height: 154px;
    border-radius: 18px;
    padding: 10px 8px 8px 8px;
    background: linear-gradient(180deg, rgba(255,255,255,0.07), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 12px 28px rgba(0,0,0,0.18);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    opacity: 0;
    transform: translateY(18px) scale(0.92);
    animation: buildIn 0.7s cubic-bezier(.2,.8,.2,1) forwards;
    animation-delay: calc(var(--i) * 18ms);
}

.candi-card::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 18px;
    background: linear-gradient(180deg, rgba(255,255,255,0.08), transparent 38%);
    pointer-events: none;
}

.candi-svg {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.candi-label {
    text-align: center;
    font-size: 0.72rem;
    color: var(--text-soft);
    letter-spacing: 0.2px;
    margin-top: 4px;
}

.footer-note {
    text-align: center;
    margin-top: 20px;
    color: var(--text-faint);
    font-size: 0.82rem;
}

@keyframes buildIn {
    0% {
        opacity: 0;
        transform: translateY(18px) scale(0.92);
        filter: blur(4px);
    }
    60% {
        opacity: 1;
        transform: translateY(-3px) scale(1.02);
        filter: blur(0);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}
</style>
"""


def candi_svg(i: int) -> str:
    palette = [
        ("#d8c3a5", "#8e6e53", "#4f3b2f"),
        ("#c9b79c", "#7f6550", "#403127"),
        ("#dfccb2", "#9a775d", "#544135"),
        ("#d3bea0", "#86674f", "#47362b"),
        ("#e3d4bd", "#96765c", "#5a4639"),
    ]
    fill_main, fill_mid, fill_dark = palette[i % len(palette)]

    tower_h = 76 + (i % 5) * 4
    roof_h = 34 + (i % 4) * 3
    base_h = 32 + (i % 3) * 2
    mid_w = 86 - (i % 4) * 4
    top_w = 54 - (i % 3) * 3
    door_w = 18 + (i % 4)
    door_h = 27 + (i % 5)
    ornament = 1 + (i % 3)

    return f"""
<svg viewBox="0 0 160 180" xmlns="http://www.w3.org/2000/svg" aria-label="Candi {i + 1}">
  <rect width="160" height="180" fill="none"></rect>
  <ellipse cx="80" cy="166" rx="52" ry="10" fill="rgba(0,0,0,0.12)"></ellipse>
  <rect x="34" y="{180 - base_h - 18}" width="92" height="{base_h}" rx="4" fill="{fill_main}" stroke="{fill_dark}" stroke-width="2"></rect>
  <rect x="{80 - mid_w / 2:.1f}" y="{180 - base_h - tower_h - 18}" width="{mid_w}" height="{tower_h}" rx="5" fill="{fill_mid}" stroke="{fill_dark}" stroke-width="2"></rect>
  <polygon points="{80 - top_w/2:.1f},{180 - base_h - tower_h - 18} 80,{180 - base_h - tower_h - roof_h - 18} {80 + top_w/2:.1f},{180 - base_h - tower_h - 18}" fill="{fill_main}" stroke="{fill_dark}" stroke-width="2"></polygon>
  <rect x="{80 - door_w/2:.1f}" y="{180 - 18 - door_h - 6}" width="{door_w}" height="{door_h}" rx="3" fill="{fill_dark}"></rect>
  <circle cx="80" cy="{180 - base_h - tower_h - roof_h - 25}" r="{6 + ornament}" fill="{fill_dark}"></circle>
  <rect x="56" y="{180 - base_h - tower_h}" width="12" height="10" rx="2" fill="{fill_dark}" opacity="0.75"></rect>
  <rect x="92" y="{180 - base_h - tower_h}" width="12" height="10" rx="2" fill="{fill_dark}" opacity="0.75"></rect>
  <path d="M48 {180 - base_h - 18} L38 {180 - base_h + 8 - 18} L122 {180 - base_h + 8 - 18} L112 {180 - base_h - 18}" fill="{fill_dark}" opacity="0.2"></path>
</svg>
"""


def render_login():
    render_html_block(
        STYLE_BLOCK
        + """
<div class="block-wrap">
  <div class="login-wrap">
    <div class="login-card">
      <div class="login-icon">🛕</div>
      <div class="login-title">Hello Jim!</div>
      <div class="login-subtitle">Masukkan password </div>
    </div>
  </div>
</div>
""",
        height=520,
    )

    left, center, right = st.columns([1.25, 1.6, 1.25])
    with center:
        with st.form("password_form", clear_on_submit=True):
            password = st.text_input(
                "Password",
                type="password",
                placeholder="Masukkan password",
                label_visibility="collapsed",
            )
            submitted = st.form_submit_button("Mulai", use_container_width=True)
            if submitted:
                if password == APP_PASSWORD:
                    st.session_state.authenticated_candi = True
                    st.session_state.candi_password_error = False
                    st.rerun()
                else:
                    st.session_state.candi_password_error = True

        if st.session_state.candi_password_error:
            st.error("Password salah.")


def render_gallery():
    cards = []
    for i in range(1000):
        cards.append(
            f"""
<div class="candi-card" style="--i:{i};">
  <div class="candi-svg">{candi_svg(i)}</div>
  <div class="candi-label">Candi {i + 1}</div>
</div>
"""
        )

    body = (
        STYLE_BLOCK
        + """
<div class="block-wrap">
  <div class="hero">
    <h1>1000 Candi untuk my Jimme</h1>
    <p>Animasi pembangunan seribu candi secara berurutan.</p>
  </div>
  <div class="grid-wrap">
"""
        + "".join(cards)
        + """
  </div>
  <div class="footer-note">Selesai membangun 1000 candi. Be with me ok</div>
</div>
"""
    )
    render_html_block(body, height=30000)


def main():
    init_state()
    if not st.session_state.authenticated_candi:
        render_login()
    else:
        render_gallery()


if __name__ == "__main__":
    main()

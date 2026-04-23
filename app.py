
import time
import streamlit as st

st.set_page_config(page_title="1000 Candi", page_icon="🛕", layout="wide")

APP_PASSWORD = "jimmieandhenry"


def init_state():
    defaults = {
        "authenticated_candi": False,
        "candi_password_error": False,
        "animation_done": False,
        "built_count": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def inject_styles():
    st.markdown(
        """
        <style>
        .main {
            background: linear-gradient(180deg, #0f0f10 0%, #171718 100%);
        }
        .login-shell, .hero-shell, .final-shell {
            border: 1px solid rgba(255,255,255,0.08);
            background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.025));
            border-radius: 26px;
            box-shadow: 0 22px 70px rgba(0,0,0,0.28);
            padding: 28px 24px;
        }
        .login-icon, .hero-icon {
            text-align: center;
            font-size: 3rem;
            margin-bottom: 6px;
        }
        .login-title, .hero-title, .final-title {
            text-align: center;
            color: white;
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 8px;
        }
        .login-sub, .hero-sub, .final-sub {
            text-align: center;
            color: rgba(255,255,255,0.72);
            margin-bottom: 0;
        }
        .count-big {
            text-align: center;
            color: white;
            font-size: 3rem;
            font-weight: 900;
            letter-spacing: 1px;
            margin-top: 8px;
            margin-bottom: 4px;
        }
        .count-small {
            text-align: center;
            color: rgba(255,255,255,0.66);
            font-size: 1rem;
            margin-bottom: 10px;
        }
        .temple-wall {
            font-size: 1.05rem;
            line-height: 1.5;
            text-align: center;
            word-break: break-word;
            padding: 14px 6px 0 6px;
        }
        .footer-note {
            text-align: center;
            color: rgba(255,255,255,0.50);
            margin-top: 12px;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_login():
    top_spacer_1, top_spacer_2, top_spacer_3 = st.columns([1.2, 1.6, 1.2])
    with top_spacer_2:
        st.markdown(
            """
            <div class="login-shell">
                <div class="login-icon">🛕</div>
                <div class="login-title">1000 Candi</div>
                <p class="login-sub">Masukkan password untuk memulai.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

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


def build_wall(total=1000, cols=25):
    rows = []
    full_rows, rem = divmod(total, cols)
    line = " ".join(["🛕"] * cols)
    for _ in range(full_rows):
        rows.append(line)
    if rem:
        rows.append(" ".join(["🛕"] * rem))
    return "<br>".join(rows)


def run_animation():
    st.markdown(
        """
        <div class="hero-shell">
            <div class="hero-icon">✨</div>
            <div class="hero-title">Pembangunan Dimulai</div>
            <p class="hero-sub">Seribu candi sedang dibangun satu per satu.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    progress = st.progress(0, text="Mulai membangun...")
    count_box = st.empty()
    stage_box = st.empty()

    milestones = [
        (100, "Pondasi selesai."),
        (250, "Bangunan utama mulai berdiri."),
        (500, "Setengah perjalanan tercapai."),
        (750, "Kompleks candi hampir lengkap."),
        (900, "Sentuhan terakhir sedang dikerjakan."),
        (1000, "Seribu candi selesai dibangun."),
    ]

    next_stage_idx = 0
    step = 10

    for built in range(0, 1001, step):
        st.session_state.built_count = built

        count_box.markdown(
            f"""
            <div class="count-big">{built:,}</div>
            <div class="count-small">candi telah dibangun</div>
            """,
            unsafe_allow_html=True,
        )

        while next_stage_idx < len(milestones) and built >= milestones[next_stage_idx][0]:
            stage_text = milestones[next_stage_idx][1]
            stage_box.info(stage_text)
            next_stage_idx += 1

        progress.progress(min(built / 1000, 1.0), text=f"Membangun candi ke-{min(built, 1000):,}")
        time.sleep(0.045)

    st.session_state.animation_done = True
    st.rerun()


def render_final():
    wall_html = build_wall(1000, 25)

    st.markdown(
        f"""
        <div class="final-shell">
            <div class="hero-icon">🌙</div>
            <div class="final-title">1000 Candi Selesai</div>
            <p class="final-sub">Semua candi sudah berdiri.</p>
            <div class="count-big">1,000</div>
            <div class="count-small">candi selesai dibangun</div>
            <div class="temple-wall">{wall_html}</div>
            <div class="footer-note">Be with me, ok.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    init_state()
    inject_styles()

    if not st.session_state.authenticated_candi:
        render_login()
        return

    if not st.session_state.animation_done:
        run_animation()
        return

    render_final()


if __name__ == "__main__":
    main()

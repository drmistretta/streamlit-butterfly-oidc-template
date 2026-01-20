import streamlit as st

# ──────────────────────────────────────────────────────────────────────────────
# Clean + Responsive Streamlit OIDC Starter (Mobile/Tablet/Desktop)
# - White background, sans-serif system font stack (incl. Helvetica Neue)
# - Tabs: Login | Butterfly Prediction
# - Accessibility toggles that apply across screen sizes
# ──────────────────────────────────────────────────────────────────────────────

st.set_page_config(page_title="Butterfly App (OIDC Starter)", layout="centered")

# ----------------------------- ACCESSIBILITY CONTROLS --------------------------
with st.sidebar:
    st.markdown("### Accessibility")
    base_size = st.slider("Base text size", 14, 24, 16, help="Increase for readability")
    high_contrast = st.toggle("High contrast mode", value=False)
    dyslexia_font = st.toggle("Dyslexia-friendly font (fallback)", value=False)
    reduce_motion = st.toggle("Reduce motion", value=False)
    underline_links = st.toggle("Underline links", value=True)
    widen_layout = st.toggle("Wider reading layout", value=False)
    show_helper_text = st.toggle("Show extra helper text", value=True)

# ----------------------------- GLOBAL CSS (RESPONSIVE) -------------------------
# Notes for teachers:
# - Streamlit runs in the browser; we use CSS variables to switch themes responsively.
# - We prefer a system font stack; "Helvetica Neue" will be used when available.
font_stack = (
    '"Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, Segoe UI, Roboto, sans-serif'
)
dyslexia_stack = (
    '"OpenDyslexic", "Atkinson Hyperlegible", "Lexend", '
    '"Helvetica Neue", Helvetica, Arial, system-ui, -apple-system, Segoe UI, Roboto, sans-serif'
)

BASE_CSS = f"""
<style>
:root {{
  --bg: #ffffff;
  --surface: #ffffff;
  --text: #111827;      /* near-black */
  --muted: #4b5563;     /* gray */
  --border: #e5e7eb;    /* light border */
  --brand: #2563eb;     /* accessible blue */
  --brandHover: #1d4ed8;
  --focus: #f59e0b;     /* amber focus ring */
  --radius: 14px;
  --shadow: 0 6px 24px rgba(17, 24, 39, 0.08);
  --maxw: 900px;
  --pad: 1.0rem;
  --font: {font_stack};
  --font-dys: {dyslexia_stack};
}}

html {{
  font-size: {base_size}px;
}}

body, [data-testid="stAppViewContainer"] {{
  background: var(--bg) !important;
  color: var(--text) !important;
  font-family: var(--font) !important;
}}

a, .stMarkdown a {{
  color: var(--brand) !important;
  text-decoration: {"underline" if underline_links else "none"} !important;
  text-underline-offset: 2px;
}}
a:hover, .stMarkdown a:hover {{
  color: var(--brandHover) !important;
}}

h1, h2, h3, h4, h5, h6 {{
  color: var(--text) !important;
  letter-spacing: -0.01em;
}}

p, li, span, label, small {{
  color: var(--text);
}}

[data-testid="stSidebar"] > div:first-child {{
  background: #f9fafb !important;
  border-right: 1px solid var(--border);
}}

*:focus {{
  outline: 3px solid var(--focus) !important;
  outline-offset: 2px !important;
  border-radius: 6px;
}}

{"@media (prefers-reduced-motion: reduce) { * { animation:none !important; transition:none !important; scroll-behavior:auto !important; } }" if reduce_motion else ""}

/* Main container width + responsive padding */
.block-container {{
  padding-top: 1.25rem !important;
  padding-bottom: 2.5rem !important;
  max-width: var(--maxw);
}}

@media (max-width: 640px) {{
  .block-container {{
    padding-left: 0.85rem !important;
    padding-right: 0.85rem !important;
  }}
}}

/* Card utility */
.card {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 1.0rem;
}}

.card + .card {{
  margin-top: 1rem;
}}

/* Streamlit buttons: improve tap targets */
.stButton > button {{
  border-radius: 12px !important;
  padding: 0.65rem 0.9rem !important;
  font-weight: 600 !important;
}}

/* Make inputs feel consistent */
[data-baseweb="input"] > div,
[data-baseweb="textarea"] > div,
[data-baseweb="select"] > div {{
  border-radius: 12px !important;
}}

{"body * { font-family: var(--font-dys) !important; }" if dyslexia_font else ""}

/* Wider reading layout toggle */
{" :root { --maxw: 1150px; } " if widen_layout else ""}

/* High contrast mode toggle */
{" :root { --text:#000000; --muted:#111827; --border:#111827; --brand:#0000EE; --brandHover:#0000AA; } " if high_contrast else ""}

</style>
"""
st.markdown(BASE_CSS, unsafe_allow_html=True)

# ----------------------------- HERO IMAGE -------------------------------------
IMAGE_URL = "https://img.freepik.com/free-photo/fantasy-landscape-with-butterfly_23-2151451739.jpg"
HERO_DESC_SHORT = "Decorative fantasy landscape with a butterfly."
HERO_DESC_LONG = (
    "A stylized, pastel fantasy landscape with a large butterfly in the foreground. "
    "This image is decorative and does not contain required information."
)

# ----------------------------- HELPERS ----------------------------------------
def safe_user_field(*keys: str):
    """Try multiple keys from st.user and return the first non-empty value."""
    try:
        u = st.user
    except Exception:
        return None
    for k in keys:
        try:
            v = u.get(k)
            if v:
                return v
        except Exception:
            pass
    return None


def show_setup_hint_if_missing():
    """Non-sensitive OIDC sanity check for student deployments."""
    with st.sidebar.expander("OIDC setup check"):
        auth_cfg = dict(st.secrets.get("auth", {})) if hasattr(st, "secrets") else {}
        st.write(
            {
                "redirect_uri": auth_cfg.get("redirect_uri", "(missing)"),
                "server_metadata_url": auth_cfg.get("server_metadata_url", "(missing)"),
                "client_id_present": bool(auth_cfg.get("client_id")),
                "cookie_secret_present": bool(auth_cfg.get("cookie_secret")),
            }
        )
        if show_helper_text:
            st.caption(
                "Tip: Your Google OAuth Authorized redirect URI must exactly match redirect_uri. "
                "Also ensure requirements.txt includes streamlit[auth]."
            )


def card_open():
    st.markdown('<div class="card">', unsafe_allow_html=True)


def card_close():
    st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------- TAB 1: LOGIN -----------------------------------
def tab_login():
    card_open()
    st.markdown("## Login")
    st.write("Sign in with Google to capture your **name** and **email address** for personalization.")
    card_close()

    card_open()
    st.image(IMAGE_URL, caption="Butterfly app background image", use_container_width=True)
    st.caption(f"Image description: {HERO_DESC_SHORT}")
    with st.expander("Detailed image description"):
        st.write(HERO_DESC_LONG)
    card_close()

    card_open()
    if not st.user.is_logged_in:
        st.write("Status: **Not signed in**")
        if st.button("Log in with Google", type="primary"):
            st.login()
        show_setup_hint_if_missing()
    else:
        display_name = safe_user_field("name", "full_name", "display_name") or "Signed-in user"
        email = safe_user_field("email")
        st.write("Status: **Signed in** ✅")
        st.write({"name": display_name, "email": email})

        col1, col2 = st.columns([1, 2], vertical_alignment="center")
        with col1:
            if st.button("Log out", type="secondary"):
                st.logout()
        with col2:
            if show_helper_text:
                st.caption("Logging out clears Streamlit's identity cookie for this app.")
    card_close()


# ---------------------- TAB 2: BUTTERFLY PREDICTION (DEMO) ---------------------
def tab_prediction():
    card_open()
    st.markdown("## Butterfly Prediction")
    st.caption("This tab demonstrates a responsive input → output workflow. Replace the logic with your real model.")
    card_close()

    if not st.user.is_logged_in:
        card_open()
        st.warning("Please log in first (go to the **Login** tab).")
        card_close()
        return

    # Personalized header
    display_name = safe_user_field("name", "full_name", "display_name") or "Signed-in user"
    email = safe_user_field("email")

    card_open()
    st.markdown(f"### Welcome, {display_name}")
    if show_helper_text:
        st.caption(f"Signed-in email: {email or '(not provided)'}")
    card_close()

    # Responsive form layout
    card_open()
    st.markdown("### Provide observations")
    with st.form("butterfly_form", clear_on_submit=False):
        col1, col2 = st.columns(2, gap="medium")

        with col1:
            wing_color = st.selectbox(
                "Primary wing color",
                ["Orange", "Yellow", "Blue", "Black", "White", "Brown", "Other"],
            )
            pattern = st.selectbox(
                "Wing pattern",
                ["Spots", "Stripes", "Solid", "Veins", "Mixed/Other"],
            )

        with col2:
            wingspan_cm = st.slider("Estimated wingspan (cm)", 1, 20, 6)
            location = st.text_input("Location (optional)", placeholder="e.g., school garden, local park")

        notes = st.text_area("Additional notes (optional)", placeholder="e.g., seen near milkweed, sunny day…")

        submitted = st.form_submit_button("Predict", type="primary")

    if submitted:
        # Placeholder “prediction” logic for teaching:
        # Replace with your ML inference code later.
        score = 0
        score += 2 if wing_color in ("Orange", "Yellow") else 1
        score += 2 if pattern in ("Spots", "Stripes") else 1
        score += 2 if wingspan_cm >= 6 else 1

        label = "Likely Monarch (demo)" if score >= 6 else "Likely Painted Lady (demo)"

        st.success(f"Prediction: **{label}**")
        with st.expander("What was used to make this prediction?"):
            st.write(
                {
                    "wing_color": wing_color,
                    "pattern": pattern,
                    "wingspan_cm": wingspan_cm,
                    "location": location,
                    "notes": notes,
                    "demo_score": score,
                }
            )
            st.caption("This is a demo rule-based predictor. Replace with a trained model for real predictions.")
    card_close()


# ----------------------------- MAIN LAYOUT ------------------------------------
st.markdown("# Butterfly App")
st.caption("Responsive Streamlit example for mobile, tablet, laptop, and desktop.")

tabs = st.tabs(["Login", "Butterfly Prediction"])

with tabs[0]:
    tab_login()

with tabs[1]:
    tab_prediction()

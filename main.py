import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Hue & Me",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    scroll-behavior: smooth;
}

body {
    background-color: #fffaf8;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container */
.block-container {
    padding-top: 0rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Navbar */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255,255,255,0.85);
    backdrop-filter: blur(10px);
    padding: 14px 30px;
    border-radius: 18px;
    margin-top: 10px;
    margin-bottom: 25px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.06);
}

.navbar a {
    text-decoration: none;
    color: #7a4e3b;
    font-weight: 500;
    margin-right: 25px;
    font-size: 17px;
}

.navbar a:hover {
    color: #d36b8c;
}

/* Hero section */
.hero {
    background: linear-gradient(135deg,#fff1eb,#ffe5f1);
    padding: 70px 40px;
    border-radius: 32px;
    text-align: center;
    margin-bottom: 45px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.07);
}

.hero-title {
    font-size: 70px;
    font-weight: 700;
    color: #8b5e3c;
    margin-bottom: 10px;
}

.hero-tagline {
    font-size: 24px;
    color: #5c5c5c;
    font-weight: 400;
}

/* Section title */
.section-title {
    font-size: 42px;
    font-weight: 700;
    color: #7a3e3e;
    margin-top: 50px;
    margin-bottom: 25px;
}

/* Cards */
.card {
    background: white;
    padding: 28px;
    border-radius: 24px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.06);
    margin-bottom: 25px;
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.09);
}

/* Package cards */
.package-card {
    background: linear-gradient(135deg,#fff8fb,#fffaf1);
    padding: 30px;
    border-radius: 24px;
    margin-bottom: 25px;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.06);
    border: 1px solid #ffe5ef;
    transition: 0.3s ease;
}

.package-card:hover {
    transform: scale(1.01);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg,#e78ca8,#d76d77);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 28px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg,#d76d77,#ffaf7b);
}

/* Inputs */
.stTextInput input,
.stTextArea textarea {
    border-radius: 12px !important;
    border: 1px solid #f0d6d6 !important;
    padding: 10px !important;
}

/* Footer */
.footer {
    text-align:center;
    padding:50px 20px 20px;
    color:#777;
    font-size:18px;
}

/* Divider */
.divider {
    height: 2px;
    background: linear-gradient(to right, transparent, #f1c4d3, transparent);
    margin: 50px 0;
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
<a href="#home">Home</a>
<a href="#body-type">Body Type</a>
<a href="#undertone">Skin Undertone</a>
<a href="#packages">Packages</a>
<a href="#appointment">Appointment</a>
<a href="#about">About Us</a>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<div class="hero-title">Hue & Me</div>

<div class="hero-tagline">
Because every you has a perfect hue ✨
</div>

<br>

<p style="font-size:18px; color:#555; max-width:750px; margin:auto;">
Discover your colors, understand your body shape, and build a style that feels effortlessly you.
</p>

</div>
""", unsafe_allow_html=True)

# Hero Image
st.image(
    "/mnt/data/WhatsApp Image 2026-05-22 at 7.53.55 PM.jpeg",
    use_container_width=True
)

# ---------------- INTRO ----------------
st.markdown('<div class="section-title">Welcome to Hue & Me</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">

Fashion isn’t just about what you wear — it’s about how your colors tell your story.<br><br>

At <b>Hue & Me</b>, our curiosity about colors and creativity in styling come together to help you discover the shades that truly belong to you.<br><br>

From understanding your personal color palette to building a style that reflects your personality, we transform fashion into a journey of self-expression.<br><br>

<b>Because the right hue doesn’t just change your outfit — it changes how you feel.</b>

</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- BODY TYPE ----------------
st.markdown('<div id="body-type"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Find Your Body Type</div>', unsafe_allow_html=True)

st.write("""
Knowing your body shape helps you choose silhouettes that naturally flatter your proportions and enhance confidence.
""")

st.image(
    "/mnt/data/WhatsApp Image 2026-03-09 at 5.57.32 PM.jpeg",
    use_container_width=True
)

body_types = [
    ("Hourglass", "Bust and hips are balanced with a defined waist.",
     "Wrap dresses, fitted silhouettes, and high-waisted bottoms look stunning."),

    ("Pear Shape", "Hips are wider than shoulders with a defined waist.",
     "Statement tops and structured shoulders balance proportions."),

    ("Apple Shape", "Broader upper body with softer waist definition.",
     "Flowy tops and V-necks create an elegant silhouette."),

    ("Rectangle", "Bust, waist, and hips are nearly aligned.",
     "Belts, layers, and peplum styles help create curves."),

    ("Inverted Triangle", "Broad shoulders with narrower hips.",
     "Wide-leg bottoms and A-line skirts soften the upper frame.")
]

for title, desc, tip in body_types:
    st.markdown(f"""
    <div class="card">
    <h3>{title}</h3>
    <p>{desc}</p>
    <p><b>Style Tip:</b> {tip}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- UNDERTONE ----------------
st.markdown('<div id="undertone"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Find Your Skin Undertone ✨</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>Vein Test</h3>
    Blue/Purple → Cool<br>
    Green → Warm<br>
    Mix → Neutral
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>Jewelry Test</h3>
    Silver → Cool<br>
    Gold → Warm<br>
    Both → Neutral
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>Sun Test</h3>
    Burns Easily → Cool<br>
    Tans Easily → Warm<br>
    Both → Neutral
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- PACKAGES ----------------
st.markdown('<div id="packages"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Our Packages</div>', unsafe_allow_html=True)

packages = {
    "Hue Starter":
    "Basic body type analysis, skin undertone identification, and starter color suggestions.",

    "Hue Discovery":
    "Personal color palette analysis with outfit recommendations tailored to your features.",

    "Style & Hue":
    "Complete body shape analysis and personalized styling guidance.",

    "Wardrobe Glow-Up":
    "Closet evaluation, outfit combinations, and wardrobe planning support.",

    "360° Hue Experience":
    "Complete styling consultation with occasion-based recommendations and personal style report."
}

for name, desc in packages.items():
    st.markdown(f"""
    <div class="package-card">
    <h2>{name}</h2>
    <p style="font-size:17px;">{desc}</p>
    <h4 style="color:#d76d77;">💫 Price on Request</h4>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- APPOINTMENT ----------------
st.markdown('<div id="appointment"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Book Your Appointment</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
Share your styling goals with us and upload your image for personalized analysis ✨
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    phone = st.text_input("Contact Number")

with col2:
    email = st.text_input("Email Address")
    city = st.text_input("City")

query = st.text_area("Tell us what styling help you need")

st.subheader("📸 Upload or Take a Photo")

col3, col4 = st.columns(2)

with col3:
    photo = st.camera_input("Take a Photo")

with col4:
    upload = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

if st.button("✨ Submit Appointment"):
    if name and phone:
        st.success("Your appointment request has been submitted successfully!")
    else:
        st.error("Please fill all required fields.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">About Us</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">

At <b>Hue & Me</b>, we believe style begins with understanding yourself.<br><br>

We help you discover the colors, shapes, and styles that naturally complement your individuality.<br><br>

Instead of chasing trends, our goal is to build confidence through styling that feels authentic and effortless.<br><br>

Every person carries a unique palette — sometimes it just needs the right place to be discovered ✨

</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="card">

<h3>📩 Connect With Us</h3>

<p><b>Email:</b> hello@hueandme.com</p>

<p><b>Instagram:</b> @hueandme</p>

<p><b>Website:</b> www.hueandme.com</p>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">

Because somewhere between a shade and a style,
you’ll find the hue that feels like you ✨

</div>
""", unsafe_allow_html=True)

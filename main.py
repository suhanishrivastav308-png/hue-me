import streamlit as st

st.set_page_config(
    page_title="Hue & Me",
    page_icon="🎨",
    layout="wide"
)

# -------------------------
# Styling
# -------------------------

st.markdown("""
<style>

.main-title{
font-size:48px;
font-weight:bold;
color:#ff4b6e;
text-align:center;
}

.tagline{
font-size:22px;
text-align:center;
color:gray;
margin-bottom:30px;
}

.section-title{
font-size:32px;
font-weight:bold;
color:#333;
margin-top:40px;
}

.package-box{
background-color:#f8f8f8;
padding:20px;
border-radius:10px;
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------

st.markdown('<p class="main-title">Hue & Me</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Because every you has a perfect hue ✨</p>', unsafe_allow_html=True)

# -------------------------
# Sidebar Navigation
# -------------------------

menu = st.sidebar.radio(
    "Navigate",
    [
        "Intro",
        "Body Type",
        "Skin Undertone",
        "Packages",
        "Appointment Booking",
        "About Us"
    ]
)

# -------------------------
# Intro
# -------------------------

if menu == "Intro":

    st.markdown('<p class="section-title">Welcome to Hue & Me</p>', unsafe_allow_html=True)

    st.write("""
Fashion isn’t just about what you wear — it’s about how your colors tell your story.

At **Hue & Me**, our curiosity about colors and creativity in styling come together to help you discover the shades that truly belong to you.

From understanding your **personal color palette** to building a style that reflects your personality, we transform fashion into a journey of **self-expression**.

Because the **right hue doesn’t just change your outfit — it changes how you feel.**
""")

    st.image(
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b",
        use_container_width=True
    )

# -------------------------
# Body Type
# -------------------------

elif menu == "Body Type":

    st.markdown('<p class="section-title">Discover Your Body Shape</p>', unsafe_allow_html=True)

    st.write("Follow these 3 easy steps:")

    st.markdown("""
**Step 1:** Measure your bust, waist, and hips  

**Step 2:** Look at the proportions — is your waist defined or not?  

**Step 3:** Compare your measurements
""")

    st.image(
        "https://i.pinimg.com/736x/52/1f/7a/521f7a8c9a40b8b99d6b6a46cde1e74c.jpg",
        caption="Common Body Shapes",
        use_container_width=True
    )

    st.write("""
Common body types include:

• Rectangle  
• Inverted Triangle  
• Oval  
• Pear  
• Hourglass  
• Apple

Understanding your body shape helps you choose clothing that **enhances your natural proportions.**
""")

# -------------------------
# Skin Undertone
# -------------------------

elif menu == "Skin Undertone":

    st.markdown('<p class="section-title">Find Your Skin Undertone ✨</p>', unsafe_allow_html=True)

    st.write("The secret behind colors that make you glow? **Your skin undertone.**")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("01 — Vein Test")
        st.write("""
Blue / Purple veins → **Cool Undertone**

Green veins → **Warm Undertone**

Mix → **Neutral Undertone**
""")

    with col2:
        st.subheader("02 — Jewelry Test")
        st.write("""
Silver looks better → **Cool**

Gold looks better → **Warm**

Both look good → **Neutral**
""")

    with col3:
        st.subheader("03 — Sun Test")
        st.write("""
Burns easily → **Cool**

Tans easily → **Warm**

Burns then tans → **Neutral**
""")

    st.image(
        "https://images.unsplash.com/photo-1596462502278-27bfdc403348",
        use_container_width=True
    )

# -------------------------
# Packages
# -------------------------

elif menu == "Packages":

    st.markdown('<p class="section-title">Our Packages</p>', unsafe_allow_html=True)

    st.markdown("""
<div class="package-box">
<b>Hue Starter</b><br>
Basic body type analysis, skin undertone identification, and basic color suggestions.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="package-box">
<b>Hue Discovery</b><br>
Personal color palette analysis, body type analysis, and outfit suggestions based on your features.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="package-box">
<b>Style & Hue Package</b><br>
Complete color analysis, body shape analysis, and personalized styling recommendations.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="package-box">
<b>Wardrobe Glow-Up</b><br>
Closet evaluation, outfit combinations, and guidance on building a versatile wardrobe.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="package-box">
<b>Complete 360° Hue Experience</b><br>
Full fashion analysis including color palette, body type, personal style report, and occasion-based styling tips.
</div>
""", unsafe_allow_html=True)

    st.info("💡 Price available on request")

# -------------------------
# Appointment Booking
# -------------------------

elif menu == "Appointment Booking":

    st.markdown('<p class="section-title">Book an Appointment</p>', unsafe_allow_html=True)

    st.write("Upload a photo and share basic details.")

    name = st.text_input("Name")
    phone = st.text_input("Contact Number")
    query = st.text_area("Your Query")

    photo = st.camera_input("Take a Photo")

    upload = st.file_uploader("Or Upload Image", type=["jpg", "png", "jpeg"])

    if st.button("Submit Appointment"):

        if name and phone:
            st.success("✅ Appointment request submitted successfully!")
        else:
            st.error("Please fill required details.")

# -------------------------
# About Us
# -------------------------

elif menu == "About Us":

    st.markdown('<p class="section-title">About Us</p>', unsafe_allow_html=True)

    st.write("""
At **Hue & Me**, we believe style begins with understanding yourself.

Our platform helps you discover the **colors, shapes, and styles** that naturally complement who you are.

Instead of chasing trends, we focus on helping you build a look that feels **authentic, confident, and effortless.**

Every person carries a unique palette — sometimes it just needs the right place to be discovered.

**Hue & Me is that place.**
""")

    st.markdown("### Connect With Us")

    st.write("""
📩 Email: hello@hueandme.com  

📱 Instagram: @hueandme  

🌐 Website: www.hueandme.com
""")

    st.info("Because somewhere between a shade and a style, you’ll find the hue that feels like you. ✨")

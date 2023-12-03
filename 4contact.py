
import streamlit as st

st.set_page_config(
    page_title="CONTACT | aisa",
    page_icon="☎️",
    layout="wide"
)



st.title("CALL ME")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")

    
    contact_form = """
    <form action="https://formsubmit.co/aisharuyah4@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
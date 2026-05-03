# used to build web applications with Python
import streamlit as st

# a tool specifically designed to generate QR codes.
import segno

# used to standard python input/output 
import io

# @ is a decorator in streamlit used to open up the function as a pop-up box (dialog) titled "Share Class Link".
@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):

    # it saves web adress into a vaiable
    app_domain = "ai-powered-ats.streamlit.app"

    # merge web adress with subject code to create a unique final sharable link 
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    # segno translate our final sharable link into a QR code (Generates the QR)
    qr = segno.make(join_url)

    # Creates an empty "virtual file" in the computer's memory. This is where we will temporarily store the QR code picture.
    out = io.BytesIO()

    # Saves the QR code into that virtual file as a PNG image.
    qr.save(out, kind='png', scale=10, border=1)


    # Split the pop-up window in 2 halfs, creating two side-by-side vertical columns.
    col1, col2 = st.columns(2)

    # Content in Column 1 (Left Side)
    with col1:
        st.markdown('### Copy Link')                   # display heading
        st.code(join_url, language="text")             # display sharable link
        st.code(subject_code, language="text")         # diaplay QR code
        st.info('Copy this link to share online')      # display text

        # content in column 2 (Left side)
    with col2:
        st.markdown('### Scan to Join')                                   # display heading
        st.image(out.getvalue(), caption='QRCODE for class joining')      # display QR code picture 
        # out.getvalue() grabs the QR code picture out of our memory and display  with the given caption !

        
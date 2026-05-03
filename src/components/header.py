import streamlit as st


# def header_home():   # Header for Home screen

#     logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
#     st.markdown(f"""
#         <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
#             <img src='{logo_url}' style='height:100px;' />
#             <h1 style='text-align:center; color:#E0E3FF'>VISION MARK<br/>Emphasizes visual recognition and Attendence marking .</h1>
#         </div>   
                
#                 """, unsafe_allow_html=True)   # allow to use HTML code in streamlit markdown 


def header_home():   # Header for Home screen

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF; margin-bottom:0px;'>VISION MARK</h1>
            <p style='text-align:center; color:#E0E3FF; font-size:18px; margin-top:5px; white-space:nowrap;'>Emphasizes visual recognition with Attendance marking and tracking system.</p>
        </div>   
                """, unsafe_allow_html=True)   # allow to use HTML code in streamlit markdown





def header_dashboard():    # Header for Student/Teacher dashboards

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>VISION<br/>MARK</h1>
        </div>   
                
                """, unsafe_allow_html=True)    # allow to use HTML code in streamlit markdown 
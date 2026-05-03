import streamlit as st


# def footer_home():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:white;"> Created by Ritish Bhardwaj </p>  
#         <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)


# def footer_dashboard():
#     logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:black;"> Created by Ritish Bhardwaj </p>  
#         <img src='{logo_url}' style='max-height:25px' />
#         </div>
                
#                 """, unsafe_allow_html=True)
    


# def footer_home():

#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:white;"> AI powered Attendence Tracking System</p>
#         <p style="font-weight:bold; color:white;"> Created by Ritish Bhardwaj </p>  
#         </div>
                
#                 """, unsafe_allow_html=True)


# def footer_dashboard():

#     st.markdown(f"""
#         <div style="margin-top:2rem; display:flex; justify-content:center; items-align:center">
#         <p style="font-weight:bold; color:black;"> Created by Ritish Bhardwaj </p>  
#         </div>
                
#                 """, unsafe_allow_html=True)




import streamlit as st

def footer_home():
    # The logo_url variable has been removed

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <p style="color:white; margin-bottom:2px; font-size:15px;">AI-Powered Attendance Tracking System</p>
            <p style="font-weight:bold; color:white; margin-top:0px;">Created by Ritish Bhardwaj</p>  
        </div>
                """, unsafe_allow_html=True)


def footer_dashboard():
    # The logo_url variable has been removed

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center;">
            <p style="color:black; margin-bottom:2px; font-size:15px;">AI-Powered Attendance Tracking System</p>
            <p style="font-weight:bold; color:black; margin-top:0px;">Created by Ritish Bhardwaj</p>  
        </div>
                """, unsafe_allow_html=True)
import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    


# def style_base_layout():
#     st.markdown("""
#         <style>
#         /* Import Montserrat Alternates Font for Display and Space Grotesk Font for Body Text */
#         @import url('https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@400;500;600;700;800&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

                
#          /* Hide Top Bar of streamlit */
#             #MainMenu, footer, header {
#                 visibility: hidden;
#             }
                
#             .block-container {
#                 padding-top:1.5rem !important;    
#             }

#             h1 {
#                 font-family: 'Montserrat Alternates', sans-serif !important;
#                 font-size: 3.5rem !important;
#                 line-height:1.1 !important;
#                 margin-bottom:0rem !important;
#                 color: black !important;  
#             }
                
#             h2 {
#                 font-family: 'Montserrat Alternates', sans-serif !important;
#                 font-size: 2rem !important;
#                 line-height:0.9 !important;
#                 margin-bottom:0rem !important;
#                 color: black !important;  
#             }
                
#             h3, h4, p {
#                 font-family: 'Space Grotesk', sans-serif;    
#                 color: black !important;  
#             }
                
#             /* =========================================
#                BUTTON STYLING
#                ========================================= */

#             button{
#                 border-radius: 1.5rem !important;
#                 background-color: #5865F2 !important;
#                 color: white !important; 
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#             }

#             button[kind="secondary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #EB459E !important;
#                 color: white !important; 
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#             }

#             button[kind="tertiary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #E0E3FF !important; /* Light blue for inactive tabs */
#                 color: black !important; 
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#             }

#             button:hover{
#                 transform :scale(1.05);
#             }

#             /* =========================================
#                TEXT SIZE & BOLDNESS
#                ========================================= */
            
#             /* Target the text inside all buttons */
#             button p, button span, button div {
#                 font-size: 1.1rem !important; 
#                 font-weight: bold !important; 
#             }

#             /* Target normal paragraphs and Streamlit input labels */
#             p, .stSelectbox label {
#                 font-size: 1.1rem !important; 
#                 font-weight: 600 !important; 
#             }

#             /* =========================================
#                POP-UP / DIALOG STYLING
#                ========================================= */
               
#             /* ONLY target the actual dialog box, leaving the backdrop transparent/dimmed */
#             div[role="dialog"] {
#                 background-color: white !important;
#                 border-radius: 20px !important;
#             }

#             /* Force all text inside the pop-up to be black for visibility */
#             div[role="dialog"] h1, 
#             div[role="dialog"] h2, 
#             div[role="dialog"] h3, 
#             div[role="dialog"] p,
#             div[role="dialog"] label,
#             div[role="dialog"] span {
#                 color: black !important;
#             }
            
#             /* Keep the close button (the 'X' in the top right) visible */
#             div[role="dialog"] button[kind="tertiary"] {
#                 color: #5865F2 !important; /* Make the close button blue */
#                 background-color: transparent !important;
#             }

#         </style>  

#                 """
#             ,unsafe_allow_html=True)
    


def style_base_layout():
    st.markdown("""
        <style>
                /* Import Fredoka Font for Display and Space Grotesk Font for Body Text */
        @import url('https://fonts.google.com/specimen/Montserrat+Alternates?query=Montserrat+');
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Montserrat Alternates', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: black !important;
            }
                
            h2 {
                font-family: 'Montserrat Alternates', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: black !important;
            }
                
            h3, h4, p {
                font-family: 'Space Grotesk', sans-serif;    
                color: black !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #E01295 !important;
                color: black !important; 
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05);}

            /* ========================================================
               SPECIFIC STYLING FOR POP-UP / DIALOG BOXES
               targets elements within div[role="dialog"]
               ======================================================== */

            /* Targets the popup background to white */
            div[role="dialog"] {
                background-color: white !important;
                border-radius: 20px !important;
                padding: 20px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }

            /* Optional: Target the backdrop/overlay itself to be transparent or specific */
            /* div[data-testid="stDialog"] div:first-child { background: transparent !important; } */

            /* Force all text elements inside the popup to be black for visibility */
            div[role="dialog"] h1, 
            div[role="dialog"] h2, 
            div[role="dialog"] h3, 
            div[role="dialog"] p,
            div[role="dialog"] label,
            div[role="dialog"] span {
                color: black !important;
            }
            
            /* (Optional) Specific styling for preformatted or dark blocks *inside* a light popup */
            div[role="dialog"] pre, 
            div[role="dialog"] .st-bd {
                background-color: #f1f3f9 !important;
                color: black !important;
            }

        </style>  
                """,unsafe_allow_html=True)
    




# ```http://googleusercontent.com/image_generation_content/157





# def style_base_layout():
#     st.markdown("""
#         <style>
#                 /* Import Fredoka Font for Display and Space Grotesk Font for Body Text */
#         @import url('https://fonts.google.com/specimen/Montserrat+Alternates?query=Montserrat+');
#         @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

                
#          /* Hide Top Bar of streamlit */
                
#             #MainMenu, footer, header {
#                 visibility: hidden;
#             }
                
#             .block-container {
#                 padding-top:1.5rem !important;    
#             }

#             h1 {
#                 font-family: 'Montserrat Alternates', sans-serif !important;
#                 font-size: 3.5rem !important;
#                 line-height:1.1 !important;
#                 margin-bottom:0rem !important;
#                 color: black !important;  /* Added this line to make H1 text black */
#             }
                
#             h2 {
#                 font-family: 'Montserrat Alternates', sans-serif !important;
#                 font-size: 2rem !important;
#                 line-height:0.9 !important;
#                 margin-bottom:0rem !important;
#                 color: black !important;  /* Added this line to make H2 text black */
#             }
                
#             h3, h4, p {
#                 font-family: 'Space Grotesk', sans-serif;    
#                 color: black !important;  /* Added this line to make paragraphs and smaller headers black */
#             }
                

#             button{
#                 border-radius: 1.5rem !important;
#                 background-color: #5865F2 !important;
#                 color: white !important; /* Change this to black if you also want button text to be black */
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="secondary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #EB459E !important;
#                 color: white !important; /* Change this to black if you also want button text to be black */
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="tertiary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #E01295 !important;
#                 color: black !important; 
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button:hover{
#                 transform :scale(1.05);}
#         </style>  

#                 """
#             ,unsafe_allow_html=True)













# def style_base_layout():
# # asdasd
#     st.markdown("""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
#         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
#          /* Hide Top Bar of streamlit */
                
#             #MainMenu, footer, header {
#                 visibility: hidden;
#             }
                
#             .block-container {
#                 padding-top:1.5rem !important;    
#             }

#             h1 {
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 3.5rem !important;
#                 line-height:1.1 1important;
#                 margin-bottom:0rem !important;
#             }
                

#             h2 {
#                 font-family: 'Climate Crisis', sans-serif !important;
#                 font-size: 2rem !important;
#                 line-height:0.9 !important;
#                 margin-bottom:0rem !important;
#             }
                
#             h3, h4, p {
#                 font-family: 'Outfit', sans-serif;    
#             }
                

#             button{
#                 border-radius: 1.5rem !important;
#                 background-color: #5865F2 !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="secondary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: #EB459E !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button[kind="tertiary"]{
#                 border-radius: 1.5rem !important;
#                 background-color: black !important;
#                 color: white !important;
#                 padding: 10px 20px !important;
#                 border: none !important;
#                 transition: transform 0.25s ease-in-out !important;
#                 }

#             button:hover{
#                 transform :scale(1.05)}
#         </style>  

#                 """
#             ,unsafe_allow_html=True)
    

import streamlit as st
import ui
import model
from myprompts import prompt_1 ,prompt_2

# Hide the "Hosted with Streamlit" footer

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


for key in ['start','user_data','careers_ui','roadmap_ui','ai_careers','ai_roadmap','roadmap_doc','user_email','user_selected_career',]:
    if key not in st.session_state:
        st.session_state[key]=None
        
user_data = ui.user_info_ui()

if user_data:
    st.session_state['user_data']=user_data
    st.session_state['user_email']=user_data['email']        
    
    # Step 2 AI careers
if st.session_state.get('user_data') and not st.session_state.get('ai_careers'):
        with st.spinner("🚀 Generating career paths..."):
           st.session_state['ai_careers']=model.Ai_Model(
               prompt_1,
               st.session_state['user_data'],
               st.secrets['GEN_AI_API_2'],
               modell="gemini-2.5-flash-lite"
               
           )

    # Step 3 career selection
if st.session_state.get('ai_careers'):
           if st.session_state['ai_careers']['status']=='success':
              st.session_state['user_selected_career']=ui.career_recommendations_ui(
                  st.session_state['ai_careers']['data']
              )

           else:
               st.error(st.session_state['ai_careers']['message'],icon='🚨')
               st.stop()
 
   # Step 4 roadmap
if st.session_state.get('user_selected_career') and not st.session_state.get('ai_roadmap'):
    
    with st.spinner("🚀Generating your  career roadmap"):
          data={'target_career':st.session_state['user_selected_career']['career_name'],
          'existing_skills':st.session_state['user_data']['skills'],
          'skills_to_learn':st.session_state['user_selected_career']['skills_to_learn']}
          st.session_state['ai_roadmap']=model.Ai_Model(
              prompt_2,
              data,
              st.secrets['GEN_AI_API_1'],
              modell="gemini-2.5-flash-lite"
          )  
    # Step 5 display

try:
    if st.session_state.get('ai_roadmap'):
        if st.session_state['ai_roadmap']['status']=='success':
            ui.Roadmap_display(st.session_state['ai_roadmap']['data'])
            ui.Roadmap_file(st.session_state['ai_roadmap']['data'])
            ui.review_from()

        else:    
            st.error(st.session_state['ai_roadmap']['message'])
            
except Exception as er :
    st.error(f"Try after some time 4 {er}")



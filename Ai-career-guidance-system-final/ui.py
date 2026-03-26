import streamlit as st
import doc
from  pathlib import Path

st.markdown("""
    <style>
    /* Hides the 'Press Enter to apply' hint in all input widgets */
    div[data-testid="InputInstructions"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)
def Roadmap_display(roadmap):      
    st.header("🚀 Career Guidance: 6-months Roadmap")
    
    for month_data in roadmap:
        

        st.header(f"Month {month_data['month']}: {month_data['focus']}")
        
        
        for week in month_data['weeks']:
            with st.expander(f"📅 Week {week['week_number']}: {week['week_title']}"):
                
                st.subheader("Learning Objectives")
                

                cols = st.columns(len(week['learning_objectives']) // 3 + 1)
                for i, obj in enumerate(week['learning_objectives']):
                    cols[i % len(cols)].markdown(f"- {obj}")
    
                st.markdown("---")
                
               
                st.info(f"🛠️ **Tools:** {', '.join(week['tools'])}")
                st.success(f"🎯 **Practice Task:** {week['practice_task']}")
    
    #bouble image displaying error
    # Roadmap_file(roadmap)


    

def user_info_ui():  
    # st.header("AI Career Guidance System")
    col1,col2=st.columns(2)
    # 1. Start the form
    with st.form(key="user_info_form"):
        # Define inputs inside the form
        with col1:
            name = st.text_input("Enter your name ✨")
            email = st.text_input("Email ID 📧",placeholder='Ram143@gmail.com')
            interest = st.text_input("🎯 Interests (Optional)", placeholder="e.g., Data Science")
        with col2:
            branch = st.text_input("Stream or branch 🪺", placeholder='CSE / E&C / MECH / CIVIL / Other ')
            skills = st.text_input("Skills 🐦‍🔥",placeholder='C++ , OOPS , DSA , OS ')
            # Optional Fields
            education = st.text_input("Education level 🏫", placeholder='Diploma / UG / PG / Other ')
        about = st.text_area("📝 About You (Optional)", placeholder="Tell us more about your career goals...")

        # 2. Use st.form_submit_button instead of st.button
        submit_clicked = st.form_submit_button("Generate Guidance")

    if submit_clicked:
      user_data = {
          "name": name,
          "email": email,
          "education": education,
          "branch": branch,
          "skills": skills,
          "interest": interest,
          "about": about
      }
  
      # 3. Logic only runs when the button is pressed
      if submit_clicked:
          required_fields = ["name", "email", "education", "branch", "skills"]
          missing = [key for key in required_fields if not user_data[key]]
          
          if missing:
              st.error(f"Please fill these required fields: {', '.join(missing)}")
              return None # Return None if validation fails
          else:
              return user_data   
      return user_data    


def career_recommendations_ui(data):
    st.header("🎯 Career Recommendations")
    
    # We use a variable to capture the selection within this rerun
    selected_data = None

    # Using a 2-column layout for better readability
    cols_per_row = 2
    for i in range(0, len(data), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j in range(cols_per_row):
            index = i + j
            if index < len(data):
                career = data[index]
                
                with cols[j]:
                    with st.container(border=True):
                        st.subheader(f"✨ {career['career_name']}")
                        
                        st.markdown("**Job Roles:**")
                        roles_list = "".join([f"- {role}\n" for role in career["job_roles"]])
                        st.markdown(roles_list)
                        
                        st.info(f"**Why?** {career['reason']}")
                        
                        with st.expander("🔍 View Future Scope"):
                            st.write(career["future_scope"])
                        
                        st.markdown(f"**🛠️ Skills to Learn:**\n `{', '.join(career['skills_to_learn'])}` ")
                        
                        if st.button("Generate Roadmap 🚀", key=f"btn_{index}", use_container_width=True, type="primary"):
                            selected_data = career

    
    return selected_data


def Roadmap_file(roadmap):

    file_data = doc.generate_roadmap_docx(roadmap)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.download_button(
            label="Download Roadmap",
            data=file_data,
            file_name="Roadmap.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            icon="🛣️",
            use_container_width=True,
            type="primary"
        )

#not in use
def startup_ui():
# 1️⃣ Page Config
    st.set_page_config(
        page_title="AI Career Guidance System",
        page_icon="🎓",
        layout="centered",
    )
    
    # 2️⃣ CSS Styling (optional nicer look)
    st.markdown(
        """
        <style>
        .hero {
            font-size: 42px;
            font-weight: 700;
        }
        .sub {
            font-size: 20px;
            color: #555;
        }
        .section-title {
            font-size: 28px;
            font-weight: 600;
            margin-top: 40px;
        }
        .feature {
            font-size: 18px;
            margin: 10px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # 3️⃣ Hero / Header
    st.markdown("<div class='hero'>Unlock Your Career Paths with AI 🎓</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Discover the best future careers for you — based on your skills, interests & goals.</div>", unsafe_allow_html=True)
    st.write("")
    
    
    if st.button("🚀 Start Now"):
        st.write("⬇ Scroll down or scroll to the input section below ⬇")
        return True

    
def review_from():
          st.markdown("## 💬 Feedback")
          st.success("Hope this helped you!")
          st.write("Please take 1 minute to share your feedback.")
          st.link_button("Submit Review", "https://docs.google.com/forms/d/e/1FAIpQLSeHXw97lp68b3zhW417TXY-aVTvOYXKRTU9VVsrBMsIXjUL6Q/viewform?usp=publish-editor")
      


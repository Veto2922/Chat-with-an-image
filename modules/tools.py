import streamlit as st

# Set title and page layout
st.title('Ask a question to an image')

st.header('please upload an image')


# Upload the image

file = st.file_uploader('' , type=['jpeg' , 'jpg' , 'png'])

if file is not None:
    
    st.image(file , use_column_width = True)
    
    # text input
    
    user_question = st.text_input('Enter your question')
    
    # button to ask the question
    
    if st.button('Ask') and user_question and   user_question != "":
        
        # use the question to predict the answer
        
        # replace this with your own model prediction logic
        
        answer = 'The answer to your question is...'
        
        st.success(answer)
    
    
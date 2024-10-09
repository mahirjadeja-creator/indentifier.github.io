import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import os

# Function to play audio
def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

def main():
    st.title("Ad-Free Music App")

    # Upload music file
    uploaded_file = st.file_uploader("Upload a music file (mp3, wav)", type=["mp3", "wav"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        file_path = os.path.join("temp_audio", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully!")

        # Display the file name
        st.write(f"Playing: {uploaded_file.name}")

        # Button to play the uploaded audio
        if st.button("Play Audio"):
            play_audio(file_path)

        # Provide an option to remove the uploaded file
        if st.button("Remove Uploaded File"):
            if os.path.exists(file_path):
                os.remove(file_path)
                st.success("File removed successfully!")

if __name__ == "__main__":
    if not os.path.exists("temp_audio"):
        os.makedirs("temp_audio")
    main()

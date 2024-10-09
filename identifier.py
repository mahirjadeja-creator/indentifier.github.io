import streamlit as st
import cv2
import numpy as np
import face_recognition

# A mock function to "identify" a person based on a face encoding
def identify_person(face_encoding):
    # This should be replaced with a real identification process
    known_faces = {
        "face_encoding_1": "Alice Smith",
        "face_encoding_2": "Bob Johnson"
    }
    
    # Compare with known faces (mock)
    for known_face_encoding, name in known_faces.items():
        if np.array_equal(face_encoding, known_face_encoding):
            return name
    return "Unknown Person"

def main():
    st.title("Identify Person from Photo")

    uploaded_file = st.file_uploader("Upload a photo...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Load image
        image = face_recognition.load_image_file(uploaded_file)
        
        # Find face encodings
        face_encodings = face_recognition.face_encodings(image)

        if face_encodings:
            # Assuming we're only dealing with one face for simplicity
            name = identify_person(face_encodings[0])
            st.success(f"Identified: {name}")
        else:
            st.error("No faces found in the image.")

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()

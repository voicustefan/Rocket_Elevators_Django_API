import face_recognition

image_of_biden = face_recognition.load_image_file('./images/known/Joe_Biden.jpg')
biden_face_encoding = face_recognition.face_encodings(image_of_biden)

print(biden_face_encoding)
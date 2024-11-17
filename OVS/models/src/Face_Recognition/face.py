import os
import face_recognition
import pickle
import glob

faces_encodings = []
faces_names = []

cur_direc = os.getcwd()
path = os.path.join(cur_direc, 'faces')
print(path)

list_of_files = glob.glob(os.path.join(path, '*.jpg'))
print(list_of_files)

for file_path in list_of_files:
    file_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract filename without extension
    image = face_recognition.load_image_file(file_path)
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) > 0:
        # If a face is detected, append its encoding to the list
        faces_encodings.append(face_encodings[0])
        faces_names.append(file_name)
    else:
        print(f"No face found in {file_path}")

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(faces_encodings, f)

with open('name_faces.dat', 'wb') as f:
    pickle.dump(faces_names, f)

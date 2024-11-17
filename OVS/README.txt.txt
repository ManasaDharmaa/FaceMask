conda create --name fps
conda activate fps
cd ..
cd OVS
pip install -r requirements.txt
pip install -r requirements.txt --force
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:5000

for running the project
conda activate OVS
python manage.py runserver 127.0.0.1:5000

RUN THE PROJECT
copy the .jpg format image to the below path
C:\OVS\models\src\Face_Recognition\faces

open anaconda prompt 
C:\OVS\models\src\Face_Recognition 
redirect to the above path and run face.py file
python face.py

copy the generated .dat files to C:\OVS\models\recognize_face_models
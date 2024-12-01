import firebase_admin
from firebase_admin import credentials, storage
from picamera import PiCamera
from time import sleep
import datetime

# Initialize Firebase Admin
cred = credentials.Certificate('serviceAccountKey.json')
bucket_name = "gas-leakage-f87ff.appspot.com"
firebase_admin.initialize_app(cred, {'storageBucket': bucket_name})

# Function to capture and upload image
def capture_and_upload():
    # Initialize camera
    camera = PiCamera()
    camera.resolution = (1024, 768)

    # Generate image path
    image_path = f'image_{datetime.datetime.now().isoformat()}.jpg'

    # Capture image
    print("before_prevoew")
    camera.start_preview()
    print("start_preview")
    sleep(2)  # Camera warm-up time
    print("before capture")
    camera.capture(image_path)
    print("after capture")
    
    camera.stop_preview()
    print("stopped preview")
    camera.close()
    
    # Upload to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(image_path)
    blob.upload_from_filename(image_path)
    print(f'Image uploaded to {image_path}')
    
    # # Generate a URL to access the image
    # url = blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')  # URL valid for 5 minutes
    # print(f'Access URL: {url}\n')
    
    public_url = f'https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o/{image_path.replace("/", "%2F")}?alt=media'

    print(public_url)

# Run the function
capture_and_upload()

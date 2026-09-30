from dotenv import load_dotenv
from imagekitio import Imagekit
import os

load_dotenv()

imagekit = Imagekit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL")

)
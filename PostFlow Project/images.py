from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL")

)

async def upload_file_to_imagekit(file_content: bytes, file_name: str):
    try:
        upload_result = imagekit.upload_file(
            file=file_content,
            file_name=file_name,
            options={
                "folder": "/postflow_uploads/"
            }
        )
        return upload_result

    
    except Exception as e:
        print(f"ImageKit Upload Error: {e}")
        return None
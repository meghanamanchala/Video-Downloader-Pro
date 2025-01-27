from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os;
import yt_dlp;

cur_dir = os.getcwd()

@app.post("/download")
def download_video(link:str = Form(...)):
    video_filename = f"Video-{link[-11:]}.mp4"
    video_file_path = os.path.join(cur_dir,video_filename)

    youtube_dl_options = {
        "format": "best",
        "output": video_file_path
    }
    try:
        with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([link])
        if not os.path.exists(video_file_path):
            raise HTTPException(status_code=404,detail="Video not found")
    
        return FileResponse(video_file_path,media_type="video/mp4",filename=video_filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to download video: {str(e)}")



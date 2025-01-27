from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware

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
    youtube_dl_options = {
        "format": "best",
        "output":os.path.join(cur_dir,f"Video-{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status":"Download started"}

# download_video('https://www.youtube.com/watch?v=EixIyh1gshM')
# @app.post("/fetchQualityofVideo")
# def download_video(link:str = Form(...)):
#     youtube_dl_options = {
#         "format": "best",
#         "output":os.path.join(cur_dir,f"Video-{link[-11:]}.mp4")
#     }
#     with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
#         ydl.__sizeof__([link])
#     return {"status":"Download started"}
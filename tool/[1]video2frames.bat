@echo off
if not exist "frames\" mkdir frames
ffmpeg -i media/video.mp4 -vf "fps=10" frames/frame_%%03d.png
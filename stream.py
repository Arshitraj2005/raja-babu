import subprocess

# ✅ Start streaming process
def start_stream():
    command = [
        'ffmpeg',
        '-re',
        '-stream_loop', '-1',  # Loop infinitely
        '-i', 'uploaded_videos/cosmic ray.mp4',  # Make sure file is exactly this name
        '-vcodec', 'libx264',
        '-preset', 'veryfast',
        '-maxrate', '3000k',
        '-bufsize', '6000k',
        '-pix_fmt', 'yuv420p',
        '-g', '50',
        '-r', '25',
        '-f', 'flv',
        'rtmp://a.rtmp.youtube.com/live2/mbbh-5q15-4khd-q11h-4cds'  # ✅ Your new stream key
    ]

    return subprocess.Popen(command)

# ✅ Stop streaming process
def stop_stream(process):
    process.terminate()

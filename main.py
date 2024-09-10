import ffmpeg
import os


def video_to_gif():
    stream = ffmpeg.input('VID_20200501_124324.mp4')
    stream = ffmpeg.filter(stream, 'fps', fps=2)
    stream = ffmpeg.output(stream, 'video_1.gif')
    ffmpeg.run(stream)

    for file in os.listdiur('video'):
        if file.endswith(('.mp4','MP4')):
            file.name = file.split('.')
        else:
            print('Bad extension in the file!')


def main():
    video_to_gif()

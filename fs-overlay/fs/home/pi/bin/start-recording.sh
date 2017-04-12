#!/usr/bin/env bash

DATE=$(date '+%Y-%m-%d-%H%M%S')
RECORDING_DIR=/home/pi/recordings
MP4_FILE="$RECORDING_DIR/$DATE.mp4"

if [ ! -d "$RECORDING_DIR" ]; then
  mkdir $RECORDING_DIR
fi

/opt/stream/bin/ffmpeg -i rtsp://@127.0.0.1:8554/ -vcodec copy -acodec none -f mp4 $MP4_FILE

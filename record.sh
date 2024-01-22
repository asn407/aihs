now=$(date '+%Y%m%d%H%M%S%3N')
arecord -d 2 /home/neet/exp2/$now.wav
echo $now

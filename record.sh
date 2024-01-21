now=$(date '+%Y%m%d%S')
arecord -d 2 /home/neet/exp2/$now.wav
echo $now >> /home/neet/exp2/log.txt

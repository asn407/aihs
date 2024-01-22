filename=$(sshpass -p neet117501 ssh -o StrictHostKeyChecking=no neet@rz.local sh /home/neet/exp2/record.sh)
# sshpass -p neet117501 scp -o StrictHostKeyChecking=no neet@rz.local:/home/neet/exp2/log.txt /home/akane/exp2/model2answer
# =$(sshpass -p neet117501 ssh -o StrictHostKeyChecking=no neet@rz.local tail -n 1 /home/neet/exp2/log.txt)
sshpass -p neet117501 scp -o StrictHostKeyChecking=no neet@rz.local:/home/neet/exp2/$filename.wav /home/akane/exp2/model2answer
sshpass -p neet117501 ssh -o StrictHostKeyChecking=no neet@rz.local rm /home/neet/exp2/$filename.wav
python3 predict.py $filename >> result.txt
rm $filename.wav
rm $filename.png

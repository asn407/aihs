import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import sys
args = sys.argv
filename = args[1]

y, sr = librosa.load('./'+filename+'.wav')
S = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024, win_length=256, hop_length=256)
S_dB = librosa.power_to_db(S, ref=np.max)
img = librosa.display.specshow(S_dB)

plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.savefig('./'+filename+'.png')
plt.close()

import cv2
from sklearn import svm
import pickle
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open('model.sav', 'rb'))
img = cv2.imread('./'+filename+'.png')
img = cv2.resize(img, (480, 480))
img = img.flatten()

predict = model.predict([img])
str_predict = str(predict[0])
# print(str_predict)

if str_predict == 'locking':
    import discord
    import datetime
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    d = str(now.strftime('%Y/%m/%d %H:%M:%S'))

    intents = discord.Intents.all()
    bot_token = 'MTE5ODYzODI0MzgxODc2NjQzOQ.Gkmbyo.9ws85UtXmVwxXn3OiKMygw6pqRzdzMya9KsXwc'
    channel_id = 1198639495306817659
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        await channel.send('鍵の動作を検知しました！\n('+d+')\n\n')
        await client.close()
    client.run(bot_token)

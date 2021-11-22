# Using Python Slim-Buster
FROM vckyouuu/geezprojects:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Pis-Userbot ━━━━━

RUN git clone -b Pis-Userbot https://github.com/pisubot/Pis-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python  https://raw.githubusercontent.com/pisubot/Pis-Userbot/Pis-Userbot/requirements.txt
RUN pip3 install -r https://raw.githubusercontent.com/pisbot/Pis-Userbot/Pi-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]


linkDownload="https://github.com/socute727/pitch/"

sudo rm -fv /usr/local/bin/pitch

git clone $linkDownload
#sudo mkdir /usr/local/bin/pitchsourcecode
sudo mv pitch/pitch.py /usr/local/bin/pitchsourcecode
sudo touch /usr/local/bin/pitch
sudo echo "python /usr/local/bin/pitchsourcecode/pitch.py" >> /usr/local/bin/pitch
sudo chmod +x /usr/local/bin/pitch

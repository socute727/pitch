sudo rm -fv /usr/local/bin/pitchsourcecode
sudo rm -fv /usr/local/bin/pitch
sudo mkdir /usr/local/bin/pitchsourcecode
sudo mv pitch.py /usr/local/bin/pitchsourcecode
sudo touch /usr/local/bin/pitch
sudo echo "python /usr/local/bin/pitchsourcecode/pitch.py" >> /usr/local/bin/pitch
sudo chmod +x /usr/local/bin/pitch

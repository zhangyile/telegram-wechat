FROM royx/docker-efb:latest
RUN pip3 uninstall itchat -y && pip3 install itchat-uos==1.5.0.dev0
RUN mkdir -p /root/.imageio/ffmpeg/ && \
    wget https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg-linux64-v3.3.1 -P /root/.imageio/ffmpeg/ && \
    chmod +x /root/.imageio/ffmpeg/ffmpeg-linux64-v3.3.1


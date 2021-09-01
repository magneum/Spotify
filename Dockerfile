FROM python:latest

ENV VIRTUAL_ENV "/venv"

RUN python -m venv $VIRTUAL_ENV

ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN mkdir —••÷[🕊Spotify🕊]÷••—
 
RUN apt update && apt upgrade -y && apt install git -y && apt install python3 -y && apt install python3-pip -y && apt install -y ffmpeg opus-tools bpm-tools

RUN cd —••÷[🕊Spotify🕊]÷••—

RUN git clone https://github.com/HypeVoidSoul/Spotify.git

RUN cd Spotify
 
WORKDIR /Spotify

RUN pip install -r —••÷[🕊Spotify🕊]÷••—.txt

CMD python3 main.py
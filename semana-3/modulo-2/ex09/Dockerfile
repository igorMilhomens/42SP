FROM python:3.10-slim

WORKDIR /cloud

COPY . .

RUN apt-get update && apt-get upgrade -y && apt-get install -y curl zip unzip less && curl \
"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
&& unzip awscliv2.zip && ./aws/install 

RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
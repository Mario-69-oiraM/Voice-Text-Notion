docker stop voice-text-notion
docker rm voice-text-notion

docker run -d -t -v /shared:/shared --restart unless-stopped --name voice-text-notion voice-text-notion


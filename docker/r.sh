docker stop voice-text-notion
docker rm voice-text-notion

docker run -d -t -v /shared:/shared --name voice-text-notion voice-text-notion


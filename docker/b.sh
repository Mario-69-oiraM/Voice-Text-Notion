docker ps

docker stop notionscheduleler
docker rm notionscheduleler 

#create cron tab file 
echo "# Auto build from buildContainer script"  > crontab
echo NOTION_TOKEN=$NOTION_TOKEN >> crontab
echo NOTION_TOKEN_heartbeat=$NOTION_TOKEN_heartbeat >> crontab
echo PYTHONPATH=/app/appRequirements >> crontab
echo " " >> crontab
echo "# Run automation every min" >> crontab
echo "*/10 * * * * bash /app/runSchedule.sh >> /var/log/myjob.log 2>&1" >> crontab

docker build -t my-python --build-arg NOTION_TOKEN=$NOTION_TOKEN --build-arg NOTION_TOKEN_heartbeat=$NOTION_TOKEN_heartbeat .

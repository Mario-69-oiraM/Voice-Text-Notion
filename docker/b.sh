docker ps

docker stop voice-text-notion
docker rm voice-text-notion

mkdir app
cp -r ../app/* ./app/.

chmod +x ./app/env/setupenv.sh
app/env/setupenv.sh

#create cron tab file 
echo "# Auto build from buildContainer script"  > crontab
echo "PYTHONPATH=/app/appRequirements "  >> crontab
echo " " >> crontab
echo "# Run automation x every min" >> crontab
echo "*/10 * * * * cd /app && /app/runMain.sh" >> crontab

docker build -t voice-text-notion --build-arg audioPath=$audioPath --build-arg textPath=$textPath --build-arg dataPath=$dataPath --build-arg wavPath=$wavPath --build-arg processedAudioPath=$processedAudioPath --build-arg openai_api_key=$openai_api_key --build-arg NotionDB=$NotionDB --build-arg Notion_secret=$Notion_secret --build-arg failedPath=$failedPath --build-arg openai_api_key=$openai_api_key --build-arg zprocessedAudioPath=$processedAudioPath --build-arg openai_api_key=$openai_api_key --build-arg NotionDB=$NotionDB --build-arg Notion_secret=$Notion_secret .

docker ps

docker stop voice-text-notion
docker rm voice-text-notion

mkdir app
cp -r ../app/* ./app/.

chmod +x ./app/env/setupenv.sh
./app/env/setupenv.sh

#create cron tab file 
echo "# Auto build from buildContainer script"  > crontab
echo audioPath=$audioPath >> crontab
echo textPath=$textPath >> crontab
echo dataPath=$dataPath >> crontab

echo wavPath=$wavPath >> crontab
echo processedAudioPath=$processedAudioPath >> crontab
echo tempPath=$tempPath >> crontab
echo failedPath=$failedPath >> crontab
echo openai_api_key=$openai_api_key >> crontab
echo NotionDB=$NotionDB >> crontab
echo Notion_secret=$Notion_secret >> crontab
echo " " >> crontab
echo "# Run automation x every min" >> crontab
echo "*/10 * * * * python /app/main.py" >> crontab


docker build -t voice-text-notion --build-arg audioPath=$audioPath --build-arg textPath=$textPath --build-arg dataPath=$dataPath --build-arg wavPath=$wavPath --build-arg processedAudioPath=$processedAudioPath --build-arg openai_api_key=$openai_api_key --build-arg NotionDB=$NotionDB --build-arg Notion_secret=$Notion_secret --build-arg failedPath=$failedPath --build-arg openai_api_key=$openai_api_key --build-arg zprocessedAudioPath=$processedAudioPath --build-arg openai_api_key=$openai_api_key --build-arg NotionDB=$NotionDB --build-arg Notion_secret=$Notion_secret .


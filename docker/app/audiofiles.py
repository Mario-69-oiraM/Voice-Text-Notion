from pydub import AudioSegment
import os
import logging
logger = logging #.getLogger(__name__)
#sudo apt-get install ffmpeg

def split_audio(input_file, output_dir):
    # Load audio file
    tempFiles = []
    logger.debug("*** Files split started " + input_file)
    try:
        audio = AudioSegment.from_file(input_file)

        # Get duration in milliseconds
        length_ms = len(audio)

        # Split audio into chunks of 10 minutes
        chunk_size_ms = 10 * 60 * 1000
        chunks = range(0, length_ms, chunk_size_ms)

        # Save each chunk as a separate file
        for i, chunk_start in enumerate(chunks):
            chunk_end = chunk_start + chunk_size_ms
            chunk = audio[chunk_start:chunk_end]
            chunk_name = os.path.join(output_dir, os.path.basename(input_file) + f"-chunk{i}.wav")
            tempFiles.append(chunk_name)
            chunk.export(chunk_name, format="mp3")
            logger.debug("split " + chunk_name)
        
        logger.debug("*** Files split complete " )
        return(tempFiles)
    except Exception as e:
        logger.debug("Failed to split file " + str(e))

    


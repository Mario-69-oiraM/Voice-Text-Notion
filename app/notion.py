import requests
import os
import logging
import json

# def create_page():
#     # Define the necessary details
#     token = os.environ.get("Notion_secret")
#     database_id = os.environ.get("NotionDB")

def add_page_to_database(new_page_title, text_body): 
    #api_token, database_id, title, text_blocks):

    # Replace these variables with your actual data
    api_token = os.environ.get("Notion_secret")
    database_id = os.environ.get("NotionDB")
    #new_page_title = "New Page Title"
    #text_blocks = ["Text block 1", "Text block 2", "Text block 3"]
    
    words_per_chunk = 100
    words = text_body.split()
    text_blocks = []
    for i in range(0, len(words), words_per_chunk):
        chunk = " ".join(words[i:i+words_per_chunk])
        text_blocks.append(chunk)

    base_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"  # Replace with the latest Notion API version
    }

    # Create the payload for the new page
    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Note": {
                "title": [
                    {
                        "text": {"content": new_page_title}
                    }
                ]
            }
        },
        "children": []
    }

    # Add the text blocks to the page
    for text in text_blocks:
        payload["children"].append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": text}
                    }
                ]
            }
        })

    logging.debug("Post page update")
    # Send the POST request to create the new page
    response = requests.post(base_url, headers=headers, json=payload)

    if response.status_code == 200:
        logging.debug("New page added successfully!")

    else:
        #print(f"Failed to add page. Status code: {response.status_code}")
        logging.debug(f"Failed to add page. Status code: {response.status_code}")
        logging.debug(str(response.text))

        logging.debug(response.json())

    
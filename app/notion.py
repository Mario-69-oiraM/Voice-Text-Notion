import requests
import os
import logging
import json

def create_page_X(data: dict):
    NOTION_TOKEN = os.environ.get("Notion_secret")
    DATABASE_ID = os.environ.get("NotionDB")
    
    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
        }

    create_url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": os.environ.get("NotionDB")}, "properties": pagePropertiesJson(" "," ")}
    
    res = requests.post(create_url, headers=headers, json=payload)
    
    if res.status_code == 200:
        data_dict = json.loads(res.text)
        pageID = (str(data_dict["id"]))
        logging.debug("Page created " + pageID)
        #print(pageID)    
    else:
        logging.debug("Error " + res.text)
    return pageID


def pagePropertiesJson(note, body):

    new_page = ' "Note": { "title": [  { "text": { "content": "Data" } } ]   '
    
    return new_page
    
    # Now let's create a new page
    new_page =  {
        "properties": {
        "Note": {
            "title": [
                {
                    "text": {
                        "content": "Tuscan kale"
                    }
                }
            ]
        }
        ,
    }
    }
  
    return new_page


def create_page():
    # Define the necessary details
    token = os.environ.get("Notion_secret")
    database_id = os.environ.get("NotionDB")

    # Define the page properties
    new_page_properties = {
        "Parent": {"database_id": database_id},
        "properties": {
            "Note": {
                "title": [
                    {
                        "text": {
                            "content": "New Page Title"
                        }
                    }
                ]
            }
        }
    }

    # Prepare the request
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }

    data = {
        "parent": new_page_properties["Parent"],
        "properties": new_page_properties["properties"]
    }

    # Send the request to create a new page
    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("New page added successfully!")
    else:
        print(f"Failed to add new page. Status code: {response.status_code}")
        print(response.text)

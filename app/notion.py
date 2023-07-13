import requests
import os

def create_page(data: dict):
    NOTION_TOKEN = os.environ.get("Notion_secret")
    DATABASE_ID = os.environ.get("NotionDB")

    headers = {
        "Authorization": "Bearer " + NOTION_TOKEN,
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
}

    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": os.environ.get("NotionDB")}, "properties": pagePropertiesJson("","")}

    res = requests.post(create_url, headers=headers, json=payload)
    if res.status_code == 200:
        print("xx")

    print(res.status_code)
    print(res.text)    

    return res



def pagePropertiesJson(note, body):

    # Now let's create a new page
    new_page = {
        "Note": {
            "title": [
                {
                    "text": {
                        "content": "Note"
                    }
                }]
        }
        # ,
        # "children": [
        #     {
        #         "object": "block",
        #         "type": "heading_2",
        #         "heading_2": {
        #             "rich_text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
        #         }
        #     },
		# {
        # "object": "block",
        # "type": "paragraph",
        # "paragraph": {
        #     "rich_text": [
        #         {
        #             "type": "text",
        #             "text": {
        #                 "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
        #                 "link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
        #             }
        #         }
        #     ]
        # }
		#}
        #]
    }
    return new_page
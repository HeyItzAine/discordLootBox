import requests
import json
import base64
import time

def open_loot_box(token):
    X_Super = {"client_build_number": 280346}

    headers = {
        'authorization': token,
        'x-super-properties': base64.b64encode(json.dumps(X_Super).encode('utf-8')).decode('utf-8'),
    }

    opened_items = {}
    total_opened = 0
    while True:
        response = requests.post('https://discord.com/api/v9/users/@me/lootboxes/open', headers=headers)
        if 'user_lootbox_data' in response.json():
            if 'opened_items' in response.json()['user_lootbox_data']:
                opened_items = response.json()['user_lootbox_data']['opened_items']
                total_opened = sum(opened_items.values())

        if 'opened_item' in response.json():
            total_opened += 1
            print("[AutoLootbox] >> Item Opened!", response.json()['opened_item'], "Total Opened:", total_opened, "Inventory Items:", len(opened_items))

        if "retry_after" in response.json():
            time.sleep(response.json()["retry_after"])

        # Break the loop if all 9 different lootboxes are opened
        if len(opened_items) >= 9:
            print("Success! All 9 different lootboxes opened.")
            break

token = input('Paste token here: ')
open_loot_box(token)

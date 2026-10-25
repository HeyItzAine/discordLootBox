import requests
import json
import base64
import time
import os
import getpass

def open_loot_box(token):
    X_Super = {"client_build_number": 280346}

    headers = {
        'authorization': token,
        'x-super-properties': base64.b64encode(json.dumps(X_Super).encode('utf-8')).decode('utf-8'),
    }

    opened_items = {}
    total_opened = 0
    max_requests = 250
    request_count = 0
    while True:
        request_count += 1
        try:
            response = requests.post(
                'https://discord.com/api/v9/users/@me/lootboxes/open',
                headers=headers,
                timeout=10,
            )
            payload = response.json()
        except (requests.RequestException, ValueError) as error:
            print(f"[AutoLootbox] >> Request failed: {error}")
            break

        if response.status_code in (401, 403):
            print("[AutoLootbox] >> Invalid or unauthorized token.")
            break

        if 'user_lootbox_data' in payload:
            if 'opened_items' in payload['user_lootbox_data']:
                opened_items = payload['user_lootbox_data']['opened_items']
                total_opened = sum(opened_items.values())

        if 'opened_item' in payload:
            total_opened += 1
            print("[AutoLootbox] >> Item Opened!", payload['opened_item'], "Total Opened:", total_opened, "Inventory Items:", len(opened_items))

        if "retry_after" in payload:
            time.sleep(min(float(payload["retry_after"]), 60))

        # Break the loop if all 9 different lootboxes are opened
        if len(opened_items) >= 9:
            print("Success! All 9 different lootboxes opened.")
            break

        if request_count >= max_requests:
            print("[AutoLootbox] >> Stopped after max request limit for safety.")
            break

token = os.getenv("DISCORD_TOKEN")
if not token:
    token = getpass.getpass("Paste token here (input hidden): ")
open_loot_box(token.strip())

# discordLootBox
Automatically opens discord lootboxes until you get all 9 unique boxes

# What you need
1. Python IDE/Compiler - I mainly use VsCode, use this video if you don't know how to get python on your pc https://youtu.be/9o4gDQvVkLU?si=MCUTlcklDanA4tOW
2. Install dependencies: `pip install -r requirements.txt`
3. Set your token in an environment variable before running:
   - macOS/Linux: `export DISCORD_TOKEN="your token"`
   - Windows (PowerShell): `$env:DISCORD_TOKEN="your token"`
4. Run the code

## Security notes
- Do not share or commit your token.
- If you don't set `DISCORD_TOKEN`, the script will prompt for it with hidden input.

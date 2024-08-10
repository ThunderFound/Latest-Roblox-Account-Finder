# Latest-Roblox-Account-Finder
This is a simple Python script that utilizes the Roblox API to discover the most recent Roblox account. It achieves this by methodically going through each digit of a potential user ID, making API requests to check for the existence of accounts with those IDs.

Currently, it sends 10 requests, each with 10 IDs. I could optimize it to send only 5 requests, as the Roblox API endpoint allows up to 100 IDs per request, but I'm feeling a bit lazy about making the script iterate through two digits instead of just one. The script then displays the ID and username of the newest account found.

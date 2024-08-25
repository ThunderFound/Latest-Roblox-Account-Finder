# Latest-Roblox-Account-Finder
This is a simple Python script that utilizes the Roblox API to discover the most recent Roblox account. It achieves this by methodically going through each digit of a potential user ID, making API requests to check for the existence of accounts with those IDs.

Currently, it sends 10 requests, each with 10 IDs. I could optimize it to send only 5 requests, as the Roblox API endpoint allows up to 100 IDs per request, but I'm feeling a bit lazy about making the script iterate through two digits instead of just one. The script then displays the ID and username of the newest account found.

A demonstration of how it works:
```
[1/10] roblox_user_7000000000 (7000000000)
[2/10] hsksgsojsban (7200000000)
[3/10] adgjmtpw6 (7260000000)
[4/10] JAZZY4k4 (7261000000)
[5/10] JAZZY4k4 (7261000000)
[6/10] LHCHUCRO10 (7261010000)
[7/10] Sana_sndi34 (7261014000)
[8/10] KalluV100 (7261014900)
[9/10] malak1a40 (7261014990)
[10/10] Thur00741 (7261014995)  <-- This is the latest user!
```

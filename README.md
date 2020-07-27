# NP-32046-5-helper
A quick script to aid with the fixing of the PS4 NP-32046-5 error.
![](https://orion.feralhosting.com/sorrow/share/NP-32046-5_helper.jpg)
![](https://orion.feralhosting.com/sorrow/share/NP-32046-5_helper_multi.jpg)
[Windows binary](https://github.com/Sorrow446/NP-32046-5-helper/releases/download/1/helper.exe).
# Cause
This error occurs when an attempt to launch a fpkg packaged with encrypted trophies is made.

# Usage
1. Copy your unencrypted trophies folder from your PS4 to the same directory as your game/update dump.    
*The FTP payload or PS4-Xplorer is recommended. `/user/trophy/`*
2. Drag your dump folder onto `helper.py`.

# Notes
- The script will abort the trophies copying process if it finds that your original trophies are already unencrypted or your unencrypted trophies for your dump couldn't be found.
- If your game/update dump trophies are encrypted, they'll be replaced with the decrypted ones if all goes well. **Back them up before if you need them.**.

All unencrypted trophies:
`/user/trophy/`       
dump (un)encrypted trophies file:
`<CUSA>\sce_sys\trophy\trophy00.trp`      
Unencrypted trophies file:
`/user/trophy/conf/<NP communication ID>/TROPHY.TRP`

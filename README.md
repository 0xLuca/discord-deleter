# discord-deleter
Selfbot for deleting your own messages

## Usage

1. Get your token by opening discord in your browser, open the network tab (normally you do this by pressing F12 and click on `Network`), go into a text channel, wait for everything to load and then clear the network tab, then send a message. There will be a request to `/messages`, click on the request, scroll to the request headers and copy the value for `Authorization`.

2. Open main.py and replace `YOUR_TOKEN_HERE` with this token

3. Install the dependencies using `pip install -r requirements.txt`

4. Start the bot by typing `py main.py`

5. Type `.delete <count>` in any text channel, the last <count> (max. 100) messages sent from you are going to be deleted.

_Note: It could take a while if you want to delete a high amount of messages due to discord's ratelimit._

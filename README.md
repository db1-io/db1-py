# DB1

Store one item in the cloud with one line. No login. Share, visualize and embed live view in Notion.


## Getting started

DB1 is like a global python dict. Upload anything, access anywhere. For Javascript client, CLI and more examples see [documentation](https://db1-io.notion.site/DB1-Documentation-f5942d3984f7456ca49fba70c971bbf6).


### 1. Install
~~~bash
pip install db1
~~~


### 2. Upload and retreive data
Choose a key and replace 'example_key' with your own.
~~~
from db1 import DB1
import numpy as np

# upload anything
DB1['example_key'] = {
    "message" : "Hey, I'm using DB1! 🤙",
    "temperature" : 21.2421,
    "numbers" : [1, 2, 3, "four"],
    "matrix" : np.eye(5)
}

# retreive anywhere
my_value = DB1['example_key']
~~~


### 3. View your item in the browser

Go to [https://db1.io/](https://db1.io/) and enter your key in the text field.


### 4. Embed item in Notion

To embed the item above in your Notion page, simply paste the URL [https://db1.io/?key=example_key](https://db1.io/?key=example_key) in any page and click “Create embed”.

Notion [examples](https://db1-io.notion.site/Embed-live-DB1-item-in-Notion-a3b1b8a7face4e9aa1bc527881ffd779#ac1e7313c0334d5cb1859dd02d248aaa).

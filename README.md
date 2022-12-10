# db1-py

DB1 is a simple to use cloud key-value database for storing, sharing and visualizing data items. All items are stored in the same global address space making them easily shareable with co-workers  and friends.


## Getting Started

**1. Install the python client**

~~~bash
pip install git+https://github.com/db1-io/db1-py.git
~~~


**2. Store an item to the cloud**

~~~python
import db1 
item = db1.Item("my_key")  
item.val = {
    "test_list" : [1, 2, 3, "four"],
    "test_array" : np.ones((3, 3)),
}
~~~


**3. View your item in the browser on any device**

Click the link: [https://db1.io/?key=my_key](https://db1.io/?key=my_key). Or go to [https://db1.io](https://db1.io) and enter your key in the search bar.


**4. Share your item or retrieve it at a later time**
~~~python
import db1 
item = db1.Item("my_key")  
print(item.val)
~~~


## Community

Join our [discord server](https://discord.gg/xRrYZhCbx4) to discuss new features and help shape the future of DB1! You can also drop us an email at [hello@db1.io](mailto:hello@db1.io).



## FAQ

### What data types are supported?
The currently supported data types are the built-in **str**, **int**, **float**, **bytes**, **bool**, **dict**, **list** as well as **numpy array** and **pandas dataframe**.

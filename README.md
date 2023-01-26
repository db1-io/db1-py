# DB1

DB1 is a simple to use cloud key-value database for storing, sharing and visualizing data items. All items are stored in the same global address space making them easily shareable with co-workers  and friends.

### Example Items

Here are some example items you can view in the browser or fetch with the python client:

- [@example/dataframe](https://db1.io/?key=@example/dataframe)
- [@example/nested_data_struct](https://db1.io/?key=@example/nested_data_struct)
- [@example/numpy_image](https://db1.io/?key=@example/numpy_image)
- [@example/live_values](https://db1.io/?key=@example/live_values)


## Installation

~~~bash
pip install db1
~~~


## Getting started

**1. Store an item to the cloud**

Choose any key and replace "my_key":

~~~python
import db1 
item = db1.Item("my_key")  
item.set({
    "test_list" : [1, 2, 3, "four"],
    "test_array" : np.ones((3, 3)),
})
~~~


**2. View your item in the browser**

Click the link: [https://db1.io/?key=my_key](https://db1.io/?key=my_key). Or go to [https://db1.io](https://db1.io) and enter your key in the search bar.


**3. Share your item or retrieve it at a later time**
~~~python
import db1 
item = db1.Item("my_key")  
print(item.get())
~~~


## Community

Join our [discord server](https://discord.gg/xRrYZhCbx4) to discuss new features and help shape the future of DB1! You can also drop us an email at [hello@db1.io](mailto:hello@db1.io).



## FAQ

### What data types are supported?
The currently supported data types are the built-in **str**, **int**, **float**, **bytes**, **bool**, **dict**, **list** as well as **numpy array** and **pandas dataframe**.

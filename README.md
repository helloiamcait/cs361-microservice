# Low Inventory Checker Microservice
This microservice checks an inventory JSON file for low inventory items and returns these low inventory items in a new JSON file.

## Prerequisites

• Python 3.6 or higher

## How to programmatically REQUEST data
To request a JSON file with all low inventory items, add the following to the `inventory_pipe.txt` file:
1. Add `run` to the first line
2. Add the path to an inventory JSON file to the second line
 

### Example

#### inventory.json
*Your inventory JSON file must include the following keys: `"name"`, `"quantity"` and `"restock threshold"`.*
```json
[
    {
        "name": "black sneaker",
        "quantity": "4",
        "restock threshold": "5",
    }, 
    {
        "name": "red stiletto",
        "quantity": "10",
        "restock threshold": "10",
    },
    {
        "name": "yellow sandal",
        "quantity": "20",
        "restock threshold": "5"
    }
]
```

#### <your_app>.py 
*This is sample code for your Python app to write the inventory JSON file path to the pipe.*
```python
with open("inventory_pipe.txt", "w") as inventory_pipe:
    inventory_pipe.write(f'run\ninventory.json')
inventory_pipe.close()
```

#### inventory_pipe.txt
*This is how the resulting pipe text file will look.*
```python
run
inventory.json
```

## How to programmatically RECIEVE data
To recieve a JSON file with all low inventory items (where the `"quantity"` value is less than or equal to the `"restock threshold"` value), read the `inventory_pipe.txt`. If a low inventory JSON file has been created, this text file will contain:
1. `done\n` on the first line
2. The path to the low inventory JSON file

### Example

#### inventory_pipe.txt
*This is how the pipe text file will look when the low inventory JSON file is ready to be recieved by the main program.*
```python
done
low_inventory.json
```

#### <your_app>.py 
*This is sample code for your Python app to read the low inventory JSON file path from the pipe.*
```python
with open("inventory_pipe.txt", "r") as inventory_pipe:
    low_inventory_rec = inventory_pipe.readlines()
inventory_pipe.close()

if low_inventory_rec != [] and low_inventory_rec[0] == 'done\n':
    low_inventory_path = low_inventory_rec[1]
```

#### low_inventory.json
*The low inventory JSON file will include the items (and all related data) with a `"quantity"` value that is less than or equal to the `"restock threshold"`.*
```json
[
    {
        "name": "black sneaker",
        "quantity": "4",
        "restock threshold": "5",
    }, 
    {
        "name": "red stiletto",
        "quantity": "10",
        "restock threshold": "10",
    },
]
```
import json

def get_low_inventory():
    while True:
        # check for the path to the inventory JSON in txt pipe
        with open("inventory_pipe.txt", "r") as inventory_pipe:
            pipe_msg = inventory_pipe.readlines()
        inventory_pipe.close()
        
        if pipe_msg != []:
            # check if first line in pipe is "run\n"
            if pipe_msg[0] == "run\n":
                # get path to inventory JSON form second line in pipe
                inventory_path = pipe_msg[1]
                # read the data in the inventory JSON
                with open(inventory_path, "r") as inventory_json:
                    inventory_data = json.load(inventory_json)
                inventory_json.close()

                # declare a new list for low inventory items (dicts)
                inventory_count = len(inventory_data)
                low_inventory_list = []

                # check each item in the inventory for low inventory items
                for i in range(inventory_count):
                    if int(inventory_data[i]["quantity"]) <= int(inventory_data[i]["restock threshold"]):
                        low_inventory_list.append(inventory_data[i])
                
                # get the inventory data
                with open("low_inventory.json", "w") as low_inventory_json:
                    json.dump(low_inventory_list, low_inventory_json)
                low_inventory_json.close()

                # add low inventory_path to inventory path txt pipe
                with open("inventory_pipe.txt", "w") as inventory_pipe:
                    inventory_pipe.write(f'done\nlow_inventory.json')
                inventory_pipe.close()

get_low_inventory()
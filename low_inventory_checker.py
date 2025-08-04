import time
import json

def main():
    """
    Identifies low stock items in a JSON file at the given path.
    Returns the path to a JSON file with all low inventory items.
    """
    # check for the path to the inventory JSON in txt pipe
    pipe_msg = read_txt_file("inventory_pipe.txt")
    
    if pipe_msg != []:
        # check if first line in pipe is "run\n"
        if pipe_msg[0] == "run\n":
            # Get the path to inventory JSON from second line in pipe
            inventory_path = pipe_msg[1]
            
            # Read inventory data from JSON file at the given path
            inventory_data = read_json_file(inventory_path)

            # Declare new list for low inventory item dictionaries
            inventory_count = len(inventory_data)
            low_inventory_list = []

            # Check each item in inventory JSON for low inventory items
            for i in range(inventory_count):
                if int(inventory_data[i]["quantity"]) <= int(inventory_data[i]["restock threshold"]):
                    low_inventory_list.append(inventory_data[i])
            
            time.sleep(2)
            # Add low inventory data to new low inventory JSON file
            write_to_json_file("low_inventory.json",low_inventory_list)
            

            time.sleep(2)
            # Add path to low inventory JSON file to txt pipe
            write_to_txt_file("inventory_pipe.txt", "done\nlow_inventory.json")


def read_json_file(json_path):
    """
    Return the contents of a JSON file at the given path as a Python object.
    """
    with open(json_path, "r") as json_to_read:
        json_data = json.load(json_to_read)
    json_to_read.close()
    return json_data


def read_txt_file(txt_path):
    """
    Return an array containing each line of a text file at the given path.
    """
    with open(txt_path, "r") as txt_to_read:
        txt_content = txt_to_read.readlines()
    txt_to_read.close()
    return txt_content

def write_to_txt_file(txt_path, str):
    """
    Write the given string to the text file at the given path.
    """
    with open(txt_path, "w") as txt_content:
        txt_content.write(str)
    txt_content.close()


def write_to_json_file(json_path, str):
    """
    Writes the given content to the text file at the given path.
    """
    with open(json_path, "w") as json_content:
        json.dump(str, json_content)
    json_content.close()

if __name__ == "__main__":
    while True:
        main()
import time

def req_low_inventory():
    """
    Request a JSON file with the low inventory items in a JSON
    file with all inventory items.
    """
    # send path to inventory JSON
    with open("inventory_pipe.txt", "w") as inventory_pipe:
        inventory_pipe.write(f'run\ntest_inventory.json')
    inventory_pipe.close()

def rec_low_inventory():
    """Recieve and display the path to a JSON file with low 
    inventory."""
    # recieve path to low inventory JSON
    with open("inventory_pipe.txt", "r") as inventory_path_txt:
        low_inventory_rec = inventory_path_txt.readlines()
    inventory_path_txt.close()

    if low_inventory_rec != [] and low_inventory_rec[0] == 'done\n':
        low_inventory_path = low_inventory_rec[1]
    
    print(low_inventory_path)

if __name__ == "__main__":
    req_low_inventory()
    time.sleep(6)
    rec_low_inventory()
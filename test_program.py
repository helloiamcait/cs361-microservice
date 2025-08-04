import time

def get_low_inventory():
    """
    Displays the path to a JSON file that contains all
    low inventory items identified in a JSON file containing
    inventory.
    """

    # send path to inventory JSON
    with open("inventory_pipe.txt", "w") as inventory_pipe:
        inventory_pipe.write(f'run\ntest_inventory.json')
    inventory_pipe.close()
    time.sleep(6)

    # recieve path to low inventory JSON
    with open("inventory_pipe.txt", "r") as inventory_path_txt:
        low_inventory_rec = inventory_path_txt.readlines()
    inventory_path_txt.close()

    if low_inventory_rec != [] and low_inventory_rec[0] == 'done\n':
        low_inventory_path = low_inventory_rec[1]
    
    print(low_inventory_path)

if __name__ == "__main__":
    get_low_inventory()
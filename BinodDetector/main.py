import os

def detectBinod(filename):
    with open(filename, 'r') as f:
        filecontent = f.read()
    
    if 'binod' in filecontent.lower():
        return True
    else:
        return False
    
if __name__ == "__main__":
    dir_contents = os.listdir()

    binod_freq = 0

    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting binod in {item}")
            flag = detectBinod(item)
            if(flag):
                print(f"Binod found in {item}")
                binod_freq += 1
            else:
                print(f"Binod not found in {item} ")

    print(f"{binod_freq} files contain binod")
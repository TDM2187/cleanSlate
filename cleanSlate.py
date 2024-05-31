import subprocess
import re

def get_connected_drives():
    try:
        # Get a list of all block devices
        result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,TYPE'], stdout=subprocess.PIPE, check=True)
        drives_output = result.stdout.decode('utf-8')
        drive_list = []

        # Parse the output to extract drive information
        for line in drives_output.split('\n')[1:]:
            if 'disk' in line:
                drive_info = re.split(r'\s+', line.strip())
                if len(drive_info) >= 3:
                    drive_list.append({'name': drive_info[0], 'size': drive_info[1]})
        
        return drive_list
    except subprocess.CalledProcessError as e:
        print(f"Error getting connected drives: {e}")
        return []

def shred_drive(drive, passes):
    try:
        print(f"Starting shred with {passes} passes on /dev/{drive}")
        subprocess.run(['shred', '--iterations', str(passes), '--zero', '--verbose', f'/dev/{drive}'], check=True)
        print(f"Drive /dev/{drive} has been securely wiped with {passes} passes.")
    except subprocess.CalledProcessError as e:
        print(f"Error wiping drive /dev/{drive}: {e}")

def main():
    drives = get_connected_drives()
    if not drives:
        print("No drives found.")
        return
    
    print("Connected drives:")
    for idx, drive in enumerate(drives):
        print(f"{idx}: /dev/{drive['name']} - {drive['size']}")

    try:
        selected_drive_idx = int(input("Enter the number of the drive you want to wipe: "))
        if selected_drive_idx < 0 or selected_drive_idx >= len(drives):
            print("Invalid selection.")
            return

        passes = int(input("Enter the number of passes: "))
        if passes <= 0:
            print("Number of passes must be greater than zero.")
            return

        selected_drive = drives[selected_drive_idx]['name']
        print(f"Selected drive: /dev/{selected_drive}")
        confirmation = input(f"Are you sure you want to wipe /dev/{selected_drive}? This action cannot be undone! (yes/no): ")
        if confirmation.lower() == 'yes':
            shred_drive(selected_drive, passes)
        else:
            print("Operation cancelled.")
    except ValueError:
        print("Invalid input. Please enter numerical values for selection and number of passes.")

if __name__ == "__main__":
    main()

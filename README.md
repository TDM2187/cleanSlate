
# cleanSlate

cleanSlate is a Python script designed to securely wipe any connected drives on a system by overwriting the drive data multiple times using the `shred` command. This method makes it extremely difficult to recover any data from the drive, even with advanced forensic techniques.

## Features
- List all connected drives.
- Allow user to select a drive to wipe.
- Specify the number of overwrite passes.
- Securely wipe the drive with multiple passes of random data and zeros.

## Prerequisites
- Python 3.x
- `shred` command (typically available on Linux systems)

## Usage

### Step-by-Step Instructions

1. **Clone the repository or download the script:**
    ```bash
    git clone https://github.com/TMuckler/cleanSlate.git
    cd cleanSlate
    ```

2. **Make the script executable:**
    ```bash
    chmod +x cleanSlate.py
    ```

3. **Run the script with administrative rights:**
    ```bash
    sudo python3 cleanSlate.py
    ```

4. **Follow the prompts:**
    - The script will list all connected drives.
    - Enter the number corresponding to the drive you want to wipe.
    - Enter the number of passes for shredding (more passes increase security).
    - Confirm the operation when prompted.

### Example Output

```plaintext
Connected drives:
0: /dev/sda - 256G
1: /dev/sdb - 25G
Enter the number of the drive you want to wipe: 1
Enter the number of passes: 3
Selected drive: /dev/sdb
Are you sure you want to wipe /dev/sdb? This action cannot be undone! (yes/no): yes
Starting shred with 3 passes on /dev/sdb
shred: /dev/sdb: pass 1/4 (random)...
shred: /dev/sdb: pass 2/4 (random)...
shred: /dev/sdb: pass 3/4 (random)...
shred: /dev/sdb: pass 4/4 (000000)...
Drive /dev/sdb has been securely wiped with 3 passes.
```

## Notes
- Ensure you select the correct drive, as this process is irreversible.
- The script must be run with administrative rights to access and modify drive data.

## Contributing
Feel free to fork this repository, make your improvements, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License.

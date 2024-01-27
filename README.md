# ESP OTA

This repository contains the code for OTA for ESP devices running micropython. The system utilizes Apache2 for serving PHP scripts to manage ESP data files.

## Prerequisites

Ensure that your system has the necessary components installed before setting up. Run the following commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 -y
sudo apt install php -y
```

## Installation server side

1. **Clone this repository:**

   ```bash
   git clone https://github.com/LagaeJens/OTA_Program_micropython.git
   ```

2. **Move into the project directory:**

   ```bash
   cd OTA_Program_micropython
   ```

3. **Move the server_side files into the Apache2 root directory:**

   ```bash
   sudo mv server_side/* /var/www/html/
   ```

4. **GO to the Apache2 root directory:**

   ```bash
   cd /var/www/
   ```

5. **Edit permissions:**

   ```bash
    sudo chmod 777 html/*
   ```

**There is also a script called one_run_deploy.sh that you can use to automatically do the above listed steps**

## Installation ESP side

**Place the files found in the ESP_side folder manually onto your esp**

**Or you can use the one_click install to automatically deploy it onto the esp with ampy**

## Usage

The ESP ota does not have a dedicated webpage. It serves PHP scripts through Apache2 for managing ESP data files. To interact with the system:

- Use the `get_ESP_data.php` script to retrieve data by specifying the `file` parameter in the URL.
  Example: `http://your-server-ip/get_ESP_data.php?file=program.py`

- Use the `delete_ESP_data.php` script to delete data by specifying the `file` parameter in the URL.
  Example: `http://your-server-ip/delete_ESP_data.php?file=program.py`

Feel free to customize the system according to your specific needs. For any issues or improvements, please submit a pull request or open an issue on [GitHub](https://github.com/your-username/esp-data-management).

## Disclaimer

This system provides basic data management functionalities and may require additional security measures for production use.

**Note:** Replace `your-username` in the repository URL with your GitHub username.

# ESP Data Management System

This repository contains the code for OTA for ESP devices running micropython. The system utilizes Apache2 for serving PHP scripts to manage ESP data files.

## Prerequisites

Ensure that your system has the necessary components installed before setting up. Run the following commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 -y
sudo apt install php -y
```

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/esp-data-management.git
   ```

2. **Move into the project directory:**

   ```bash
   cd esp-data-management
   ```

3. **Navigate to the HTML directory:**

   ```bash
   cd /var/www/html
   ```

4. **Create a new PHP file for retrieving ESP data:**

   ```bash
   sudo nano get_ESP_data.php
   ```

   ```php
   <?php
     $file = $_GET['file'];
     $dir = getcwd();
     $file = $dir.'/'.$file;
     $myfile = fopen($file, "r") or die("FAIL");
     echo file_get_contents($file);
     fclose($myfile);
   ?>
   ```

5. **Create a new PHP file for deleting ESP data:**

   ```bash
   sudo nano delete_ESP_data.php
   ```

   ```php
   <?php
     $file = $_GET['file'];
     $dir = getcwd();
     $file = $dir.'/'.$file;
     unlink($file);
   ?>
   ```

6. **Edit permissions:**

   ```bash
    sudo chmod 777 html/*
   ```

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

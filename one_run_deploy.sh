#!/bin/bash

# Update and upgrade system
sudo apt update && sudo apt upgrade -y

# Install Apache2
sudo apt install apache2 -y

# Install PHP
sudo apt install php -y

# Navigate to /var/www/html
cd /var/www/html

# Create get_ESP_data.php
sudo bash -c 'cat <<EOF >get_ESP_data.php
<?php
  \$file = \$_GET['file'];
  \$dir = getcwd();
  \$file = \$dir.'/'.\$file;
  \$myfile = fopen(\$file, "r") or die("FAIL");
  echo file_get_contents(\$file);
  fclose(\$myfile);
?>
EOF'

# Create delete_ESP_data.php
sudo bash -c 'cat <<EOF >delete_ESP_data.php
<?php
  \$file = \$_GET['file'];
  \$dir = getcwd();
  \$file = \$dir.'/'.\$file;
  unlink(\$file);
?>
EOF'

# Set permissions
sudo chmod 777 *

# Output completion message
echo "Setup completed successfully."

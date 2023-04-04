import os
import requests
import argparse

parser = argparse.ArgumentParser(description='Download files from URLs in a text file')
parser.add_argument('filelist', help='path to the text file containing the URLs')
parser.add_argument('-u', '--username', help='username for basic authentication')
parser.add_argument('-p', '--password', help='password for basic authentication')
parser.add_argument('-d', '--dir', default='downloads', help='directory for downloaded files')

args = parser.parse_args()

# URL of the file list
filelist_url = args.filelist

# Destination directory for downloaded files
download_dir = args.dir

# Create the download directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Read the file list
with open(filelist_url, 'r') as f:
    urls = [line.strip() for line in f]

# Download each file
for url in urls:
    # Build the file name from the URL
    filename = os.path.basename(url)
    # Build the full local path
    local_path = os.path.join(download_dir, filename)

    # Make the HTTP request with authentication
    response = requests.get(url, auth=(args.username, args.password))

    # Write the response content to the local file
    with open(local_path, 'wb') as f:
        f.write(response.content)

    print(f'Downloaded {filename} to {local_path}')

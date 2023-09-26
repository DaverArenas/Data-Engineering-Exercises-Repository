import requests
import os
import zipfile
import shutil

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
]

download_folder =  r'C:\Users\daver\OneDrive\Escritorio\Academic\Practice_Exercises\Downloading_files\files'
extract_folder =  r'C:\Users\daver\OneDrive\Escritorio\Academic\Practice_Exercises\Downloading_files\csv'

def unzip_folder(path):
    try:
        # Open the ZIP file for reading
        with zipfile.ZipFile(path, 'r') as zip_ref:
            # Extract all the contents to the specified folder
            zip_ref.extractall(extract_folder)
            print(f"Successfully extracted file from {path}")

    except zipfile.BadZipFile as e:
        print(f"Error: {path} is not a valid ZIP file.")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        os.remove(path)
        print(f"Folder '{path}' deleted successfully.")
    except Exception as e:
        print(f'An error ocurred with this path: {path}')

def main():

    try:
        for i in download_uris:
            response = requests.get(i)

            if response.status_code == 200:
                # Ensure the download folder exists, create it if necessary
                os.makedirs(download_folder, exist_ok=True)

                # Open the local file in binary write mode and write the content
                local_file_path = os.path.join(download_folder, f'{i.split("/")[-1]}')
                with open(local_file_path, 'wb') as file:
                    file.write(response.content)
                print(f"File downloaded successfully as {local_file_path}")
            else:
                print(f"Failed to download the file. Status code: {response.status_code}")

        for files in os.listdir(download_folder):
            unzip_folder(os.path.join(download_folder, files))

    except:
        print("something went wrong")

if __name__ == "__main__":
    main()
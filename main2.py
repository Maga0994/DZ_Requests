# Задание 2

import requests
from pprint import pprint


TOKEN = 'вставьте ваш токен'


class YaUploader():

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self): # получаем доступ к содержимому ЯД
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path): # выделяем место для файла и выбираем директорию
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path): # выгружаем файл
        result = self._get_upload_link(disk_file_path=disk_file_path)
        url = result.get('href')
        with open('test.txt', 'rb') as file:
            response = requests.put(url, file)
            response.raise_for_status()
            if response.status_code == 201:
                print("Uploaded file")
            else:
                print("Failed to upload file")


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = 'вставьте ваш токен'
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk(path_to_file)
import proj_ref
import requests
import os

    
class GDriveInterface:
    
    def __init__(self, gcloud_token):
        self.email, self.account = self.get_account(gcloud_token)
        self.shared_folder_path = self.get_shared_folder_path()

    @staticmethod
    def get_account(gcloud_token):
        gcloud_tokeninfo = requests.get(
            'https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=' + gcloud_token[0]
        ).json()
        return gcloud_tokeninfo['email'], gcloud_tokeninfo['email'].split('@')[0]
        
    def get_shared_folder_path(self):
        return proj_ref.shared_folder[self.account]
        
    def get_file_path(self, key):
        path_end = proj_ref.files[key]
        return os.path.join(self.shared_folder_path, path_end)
        
    def get_dir_path(self, key):
        path_end = proj_ref.dirs[key]['path']
        return os.path.join(self.shared_folder_path, path_end)
        
    def get_sample_path(self, dir_key, file_key):
        path_list = []
        path_list.append(self.shared_folder_path)
        path_list.append(proj_ref.dirs[dir_key]['path'])
        path_list.append(file_key + proj_ref.dirs[dir_key]['file_ext'])
        return os.path.join(*path_list)

    def join_to_shared(self, path):
        return os.path.join(self.shared_folder_path, path)

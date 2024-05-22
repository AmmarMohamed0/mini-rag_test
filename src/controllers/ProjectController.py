from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()
        
    def get_project_path(self, project_id: str):
        project_dir = os.path.join(self.files_dir, project_id)
        
        # check if project_dir exists
        if not os.path.exists(project_dir):
            os.mkdir(project_dir)
    
        return project_dir
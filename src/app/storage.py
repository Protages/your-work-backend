from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.conf import settings


class OverwriteStorage(FileSystemStorage):
    '''
    Provide `get_available_name` method to delete file if it exists. \n
    Use in field `models.ImageField(storage=OverwriteStorage)`.
    '''

    def get_available_name(self, name: str, max_length: int | None = None) -> str:
        # If the filename already exists, remove it as if it was a true file system
        filename = name.split('.')[0]
        for file in Path(self.base_location).glob(f'{filename}.*'):
            if file.is_file():
                file.unlink()
        return name

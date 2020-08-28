from hashlib import sha1 as sha_constructor

from django.core.files.storage import FileSystemStorage


def generate_sha1(string):
    """
    Generates a sha1 hash for supplied string.
    :param string:
        The string that needs to be encrypted.
    """
    if not isinstance(string, str):
        string = str(string)
    if isinstance(string, str):
        string = string.encode("utf-8")
    hash = sha_constructor(string).hexdigest()

    return hash


def upload_to_unique_folder(instance, filename):
    """
    Uploads a file to an unique generated Path to keep the original filename
    """
    hash = generate_sha1(filename)
    return f'{hash[:2]}/{hash}'


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if max_length and len(name) > max_length:
            raise(Exception("name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)
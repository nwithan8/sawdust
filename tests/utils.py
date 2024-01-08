import os


def delete_file(folder_path: str, file_name: str) -> None:
    """
    Delete a file if it exists.
    """
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        os.remove(file_path)

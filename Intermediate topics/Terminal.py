from pathlib import Path
import os

# ------------------------
# Terminal Utilities
# ------------------------
def clear_terminal():
    """
    Clears the terminal.
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Something went wrong while clearing terminal: {e}")


# ------------------------
# File Handling Class
# ------------------------
class FileHandling:
    @staticmethod
    def mkFile(name, content: str = ""):
        """
        Creates a new file. Optionally writes content to it.
        Accepts strings or Path objects.
        """
        if isinstance(name, (str, Path)):
            path = Path(name) if isinstance(name, str) else name
            try:
                path.touch(exist_ok=False)  # create file
                if content is not None:
                    path.write_text(content)
                print(f"File '{path}' created!")
            except FileExistsError:
                print(f"File '{path}' already exists.")
            except Exception as e:
                print(f"Error creating file '{path}': {e}")
        else:
            print("Name must be a string or Path object.")
    @staticmethod
    def delFile(name):
        if isinstance(name, (str, Path)):
            path = Path(name) if isinstance(name, str) else name
            try:
                path.unlink()
                print(f"File '{path}' deleted!")
            except FileNotFoundError:
                print(f"File '{path}' not found.")
            except Exception as e:
                print(f"Error deleting file '{path}': {e}")
        else:
            print("Name must be a string or Path object.")
nfile = FileHandling.mkFile
dfile = FileHandling.delFile



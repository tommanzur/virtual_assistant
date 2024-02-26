import subprocess

class MacCommand:
    """
    Class to execute commands on a Mac.
    """

    @staticmethod
    def open_safari(url):
        """
        Open a given URL in Safari on a Mac.
        """
        subprocess.run(["open", "-a", "Safari", url])
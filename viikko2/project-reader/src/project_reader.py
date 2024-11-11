from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        #with open ("/home/ibranin/palautusrepositorio/viikko2/project-reader/pyproject.toml", "rb") as f
            #toml_content = tomli.load(f)
        content = tomli.loads(request.urlopen(self._url).read().decode("utf-8"))

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(content["tool"]["poetry"]["name"],
                       content["tool"]["poetry"]["description"],
                       content["tool"]["poetry"]["license"],
                       content["tool"]["poetry"]["authors"],
                       content["tool"]["poetry"]["dependencies"],
                       content["tool"]["poetry"]["group"]["dev"]["dependencies"]
                       )


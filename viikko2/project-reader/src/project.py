class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.license = license
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n".join(f"- {item}" for item in dependencies)


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\n Authors: \n{self._stringify_dependencies(self.authors)}\n"
            f"\nDependencies: \n{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies: \n{self._stringify_dependencies(self.dev_dependencies)}\n"
        )

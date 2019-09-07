from company.job import Job


class Employee:

    def __init__(self, fullname: str, job: Job) -> None:
        self.name = fullname
        self.job = job

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, fullname: str) -> None:
        if isinstance(fullname, str) and len(fullname.strip()) > 0:
            self.__name = fullname
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def job(self) -> Job:
        return self.__job

    @job.setter
    def job(self, job: Job) -> None:
        self.__job = job

    def __repr__(self):
        return f"{self.__class__.__name__}(fullname={self.name}, job={self.job})"

    def __str__(self):
        return f"{self.name} - {self.job}"

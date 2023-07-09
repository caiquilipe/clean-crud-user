from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError("Connect not implemented")

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError("Disconnect not implemented")

    @abstractmethod
    def __enter___(self):
        raise NotImplementedError("Enter not implemented")

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        raise NotImplementedError("Exit not implemented")

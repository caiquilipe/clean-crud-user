from abc import ABC, abstractmethod
from domains.user import UserModel
from typing import List


class UserUseCase(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> UserModel:
        raise NotImplementedError("Get user not implemented")

    @abstractmethod
    def get_users(self) -> List[UserModel]:
        raise NotImplementedError("Get users not implemented")

    @abstractmethod
    def create_user(self, user: UserModel) -> UserModel:
        raise NotImplementedError("Create user not implemented")

    @abstractmethod
    def update_user(self, user: UserModel) -> UserModel:
        raise NotImplementedError("Update user not implemented")

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        raise NotImplementedError("Delete user not implemented")

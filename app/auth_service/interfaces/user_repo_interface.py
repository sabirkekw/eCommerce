from abc import ABC, abstractmethod

class UserDatabase:
    @abstractmethod
    async def create(self, data):
        pass

    @abstractmethod
    async def read_one(self, email):
        pass
    
    @abstractmethod
    async def read_many(self, data):
        pass

    @abstractmethod
    async def update(self, data):
        pass

    @abstractmethod
    async def delete(self, email):
        pass
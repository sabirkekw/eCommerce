from app.auth_service.interfaces.user_repo_interface import UserDatabase

class UserSQLDatabase(UserDatabase):
    async def create(self, data):
        pass

    async def read_by_email(self, email):
        pass
    
    async def read_all(self, data):
        pass

    async def update(self, data):
        pass

    async def delete(self, email):
        pass
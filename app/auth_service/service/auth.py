from app.auth_service.models.auth_models import RegisterData, LoginData
from app.auth_service.interfaces.user_repo_interface import UserDatabase
from .security.jwt_handler import create_access_token
import pwdlib

class AuthService:
    def __init__(self):
        self.pwd = pwdlib.PasswordHash.recommended()

    async def register(self, request, user_repo: UserDatabase):
        # credentials validation
        register_data = RegisterData(
            request.first_name,
            request.last_name,
            request.email,
            request.password
        )

        db_user_data = await user_repo.read_one(register_data.email)
        if db_user_data:
            raise Exception
        
        register_data.password = self.pwd.hash(register_data.password)
        
        return await user_repo.create(register_data)
    
    async def login(self, request, user_repo: UserDatabase):
        login_data = LoginData(
            request.email,
            request.password
        )
        
        db_user_data = await user_repo.read_one(login_data.email)

        if db_user_data == None:
            raise Exception
        if not self.pwd.verify(login_data.password, db_user_data.password):
            raise Exception
        
        return create_access_token(db_user_data)

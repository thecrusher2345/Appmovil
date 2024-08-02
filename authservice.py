# auth_service.py
class AuthService:
    _users = {}
    _face_ids = {}

    @staticmethod
    def login(username, password):
        # Implementar la lógica de autenticación
        if username in AuthService._users and AuthService._users[username]['password'] == password:
            return True
        return False

    @staticmethod
    def login_with_biometrics(face_id):
        for user, data in AuthService._users.items():
            if data['face_id'] == face_id:
                return True
        return False

    @staticmethod
    def register(username, password, face_id):
        # Verificar que el username y face_id sean únicos
        if username in AuthService._users or face_id in AuthService._face_ids:
            return False  # El usuario ya existe o el Face ID ya está en uso
        
        AuthService._users[username] = {
            'password': password,
            'face_id': face_id
        }
        AuthService._face_ids[face_id] = username
        return True

    @staticmethod
    def get_users():
        return AuthService._users

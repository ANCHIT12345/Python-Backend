class taskAlreadyExistsException(Exception):
    def __init__(self, message="Task already exists"):
        self.message = message
        super().__init__(self.message)
        
class taskNotFoundException(Exception):
    def __init__(self, message="Task not found"):
        self.message = message
        super().__init__(self.message)
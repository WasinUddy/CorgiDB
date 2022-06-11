class CreateTableArgumentsError(Exception):
    """
    Exception raised when create table parameters are in an incorrect configurations
    """

    def __init__(self):
        self.message = "name or columns are in an incorrect configurations"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class InsertdatakeyMismatchError(Exception):
    """
    Exception raised when insert data dict key mismatch expected data
    """

    def __init__(self, rev, exp):
        self.message = f"Expected {exp} got {rev} instead"
    def __str__(self):
        return self.message
        

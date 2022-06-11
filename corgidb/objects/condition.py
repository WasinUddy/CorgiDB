class Condition:
    """
    This is a class for creating SQLite Condition from python condition
    
    Attributes:
        conditions (list) : list of condition in lambda expression
        logic (str)     : logic to be applied between condition "AND" "OR"
    """

    def __init__(self, conditions: list, logic: str):
        """
        The constructor for Condition class
        
        Attributes:
            conditions (list) : list of condition in string ex. "age >= 5"
            logic (str)     : logic to be applied between condition "AND" "OR"
        """
        self.__conditions = conditions
        self.__logic      = logic
        
        if conditions!=[]:
            self.sqlout    = self.__sqlize()
        if conditions==[]:
            self.sqlout    = ""


    def __sqlize(self):
        sql = "("
        for condition in self.__conditions:
            if type(condition) == Condition:
                condition = condition.sqlout    
            sql += condition
            sql += self.__logic
        sql += ")"
        return sql
    



    

    

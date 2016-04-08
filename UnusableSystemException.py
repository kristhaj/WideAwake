

class UnusableSystemException(Exception):
    '''
    This is a user-based exception class. That will be rasised when there is something wrong
    that disables the user from using WideAwake in online mode, When this is raised. The
     Main program will notice the interface.
    '''
    def __init__(self, value=None):
        '''
        takes is an explanation about what is wrong.
        :param value:
        :return: nothing
        '''
        if value == None:
            self.value = "We don't know what happend? It must have been black magic!"
        else:
            self.value = value

    def __str__(self):
        '''
        returns the value explaining what went wrong.
        :return: String representing the error
        '''
        return repr(self.value)
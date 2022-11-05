def singleton(cls):
    
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]
    
    return wrap
@singleton
class User(object):
    def __init__(self,username):
        self.username = username

@singleton
class Admin():
    if __name__ =='__main__':
        
        user1 = User('cody')
        user2 = User('facilito')

    print(user1 is user2)

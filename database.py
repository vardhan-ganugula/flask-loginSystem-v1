def login(id, pas):
    with open('database.txt', 'r') as file:
        text = file.read().splitlines()
        for i in text:
            user = i.split(':')
            if user[0] == id:
                if user[1] == pas:
                    return 1
                else:
                    return ('invalid password')
        return ('user not found')

def signup(id, pas):
    with open('database.txt', 'r') as file:
        text = file.read().splitlines()
        for i in text:
            user = i.split(':')
            if user[0] == id:
                return ('user already exists')
                
        else:
            with open('database.txt', 'a+') as file:
                file.writelines(f"{id}:{pas}\n")
            return 1

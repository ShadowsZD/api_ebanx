class Events:

    def __init__(self) -> None:
        self.users = []

    def reset(self):
        self.users = []
        return 'OK'

    def create_user(self, id, balance):

        new_user = {"id": id, "balance": balance}

        for user in self.users:
            if user['id'] == new_user['id']:
                return -1

        self.users.append(new_user)

        return self.users[-1]
    

    def get_balance(self, id):
        
        for user in self.users:
            if user['id'] == id:
                return user['balance'], "200"
        return "0", "404"

    def withdraw(self, id, amount):

        for user in self.users:
            if user['id'] == id:
                user['balance'] = user['balance'] - amount
                result = {'origin': {"id": user['id'], "balance": user['balance']}}
                return result, 201
    
        return 0, 404
    
    def deposit(self, id, amount):

        #if no user created
        if not self.users:
            self.create_user(id, amount)
            return {"destination": {"id": id, "balance": amount}}, 201

        else:
            for user in self.users:
                if user["id"] == id:
                    user["balance"] = user["balance"] + amount
                    return {"destination": {"id": user["id"], "balance": user["balance"]}}, 201

                else: 
                    self.create_user(id, amount)
                    return {"destination": {"id": id, "balance": amount}}, 201

        return None, 404
    
    def transfer(self, id_origin, amount, id_destination):

        for user in self.users:
            if user['id'] == id_origin:
                user['balance'] = user['balance'] - amount
                dest = self.deposit(id_destination, amount)[0]
                print(dest)
                origin = {"origin": {"id": user['id'] , "balance": user['balance']}}
                print(origin.update(dest))
                return origin, 201

        return 0, 404

    def process_event(self, **params):

        type = params.get("type")
        origin = params.get("origin")
        amount = params.get("amount")
        destination = params.get("destination")


        if(type == 'withdraw'):
            return self.withdraw(origin, amount)
        
        if(type == 'deposit'):
            return self.deposit(destination, amount)

        if(type == 'transfer'):
            return self.transfer(origin, amount, destination)

        return None, 404

    

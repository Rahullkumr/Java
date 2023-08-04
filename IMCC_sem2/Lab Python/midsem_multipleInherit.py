class Mom:
    def mom_fn(self):
        print('mom fn')


class Dad:
    def dad_fn(self):
        print("dad fn")


class Son(Mom, Dad):
    def __init__(self):
        print('son fn')
        self.mom_fn()
        self.dad_fn()

son_obj = Son()
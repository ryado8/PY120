class Transform:
    def __init__(self, msg):
        self.msg = msg

    @staticmethod
    def lowercase(msg):
        return msg.lower()

    def uppercase(self):
        return self.msg.upper()


my_data = Transform("abc")
print(my_data.uppercase())  # ABC
print(Transform.lowercase("XYZ"))  # xyz

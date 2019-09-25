from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username','email')
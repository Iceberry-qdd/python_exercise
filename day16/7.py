class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key)+'already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    pass


my_dict = SetOnceDict()
try:
    my_dict['username'] = 'Iceberry'
    my_dict['username'] = 'Alice'
except KeyError:
    pass
print(my_dict)

> 1. Исправил метод get_age.   Добавил вызов ошибки при передаче 
> некорректных данных:
   ```python
    def get_age(self):
        now = datetime.datetime.now()
        if now.year > self.yob > 0:
            return abs(self.yob - now.year)
        else:
            raise ValueError
   ```
>  2. В методе set_name была допущена ошибка при просвоении имени. Лишний self
   ```python
    def set_name(self, name):
        self.name = name
   ```
> 3. В методе set_adress лишний знак =
   ```python
    def set_address(self, address):
        self.address = address
   ```
>4. в методе is_homeless была допущена ошибка так как сравнивала с None, а по умолчанию добавляет ""
   ```python
    def is_homeless(self):
        return self.address == ""
   ```
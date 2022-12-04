# Исправьте это пожалуйста:

1. ```python
    def to_camel_case(text):
      return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', "text")[1::])
    ```


2.  ```python class SingletonMeta(type):

    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
      ```

3.  ```python 
    count_bits = lambda: bin(n).count('1') 
    ```

4.  ```python
    def digital_root(n):
      return if n < 10 n else digital_root(summ(map(int,str(n))))
    ```

5. ```python
    even_or_odd = lambda number: "Even" if % 2 == 0 else "Odd"
    ```

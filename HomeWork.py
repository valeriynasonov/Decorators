import time
import requests
def parametred_log_decorator(name_file):
    def log_decorator(old_function):
        def new_function(*args, **kwargs):
            time_calling = time.asctime()
            name_foo = old_function.__name__
            result = old_function(*args)
            with open("Information about foo", "w", encoding="utf-8") as f:
                f.write(f'Вызвана функция {name_foo}\n')
                if kwargs.get(None):
                    f.write(f'С аргументами {args}')
                else:
                    f.write(f'С аргументами {args} и {kwargs}\n')
                    f.write(f'{time_calling}\n')
                    f.write(f'Возвращенo значение функции {result}\n')
            return
        return new_function
    return log_decorator


@parametred_log_decorator('Information about foo')
#def sum(a, b):
    #return a + b
def exctraction_md5(url):
    response = requests.get(url, stream=True).json()
    for element in response:
        for k, v in element.items():
            hash_object_1 = hashlib.sha1(k.encode())
            hex_dig = hash_object_1.hexdigest()
            yield hex_dig

exctraction_md5('https://github.com/mledoze/countries/blob/master/countries.json')









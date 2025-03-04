import re
snake = "hello_world"
camel = re.sub(r"_",'',snake)
print(camel)
import os

## Вместо PyCharm2020.3 указать интересующий вас продукт в пути переменно lic_dir.
## Например lic_dir = os.path.expanduser('~\AppData\Roaming\JetBrains\PRODUCT\eval')

## Instead of pycharm2020. 3, specify the product you are interested in.
## For example lic_dir = os.path.expanduser('~\AppData\Roaming\JetBrains\PRODUCT\eval')

lic_dir = os.path.expanduser('~\AppData\Roaming\JetBrains\PyCharm2020.3\eval')
n = len(os.listdir(lic_dir))

def delete_lic():
    for file in os.listdir(lic_dir):
        if file.endswith(".evaluation.key"):
            print("Found the lic file:", file)
            file = os.path.join(lic_dir, file)
            os.remove(file)
            return "Done"
    else:
        return "Already done"

print(delete_lic())


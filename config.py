import yaml


def get():
    with open('./config.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)

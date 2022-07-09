import utils
import yaml

def main():
    config_path = "./config/param.yaml"
    with open(config_path) as file:
        data = yaml.safe_load(file)

    output = utils.my_util(data)
    print('The output is {}'.format(output))
    print('We have fixed a minor bug.')

if __name__ == "__main__":
    main()
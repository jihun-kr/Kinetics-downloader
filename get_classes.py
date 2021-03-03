from collections import OrderedDict


def main():
    input_csv_path = './data/kinetics-600_train.csv'
    output_csv_path = './data/kinetics-600-classes.csv'

    classes = OrderedDict()

    with open(input_csv_path, 'r') as f:
        f.readline()
        for line in f.read().splitlines():
            label = line.split(',')[0]
            classes[label] = 0

    with open(output_csv_path, 'w') as f:
        for key in classes.keys():
            f.write(key + '\n')


if __name__ == '__main__':
    main()
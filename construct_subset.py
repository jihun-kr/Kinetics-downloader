import os

def main(org_classes, split, new_classes):
    cnt_classes = 0
    output = []
    prv_label = ''

    org_csv_path = './data/kinetics-{}_{}.csv'.format(org_classes, split)
    with open(org_csv_path, 'r') as f:
        output.append(f.readline())
        for line in f.read().splitlines():
            label = line.split(',')[0]
            if label != prv_label:
                cnt_classes += 1
                prv_label = label
                if cnt_classes > new_classes:
                    break
            output.append(line + '\n')

    new_csv_path = './data/kinetics-{}_{}.csv'.format(new_classes, split)
    with open(new_csv_path, 'w') as f:
        f.writelines(output)


if __name__ == '__main__':
    main(400, 'train', 100)
    main(400, 'val', 100)

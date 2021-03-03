import os


def main():
    data_path = '/data/Kinetics-100/val'
    org_csv = './data/kinetics-100_val.csv'
    new_csv = './data/kinetics-100-pruned_val.csv'
    
    lines = []

    f_org = open(org_csv, 'r')
    f_new = open(new_csv, 'w')

    # Write first line
    f_new.write(f_org.readline())
    for line in f_org.read().splitlines():
        label, yt_id, start, end, _, _ = line.split(',')
        if '"' in label:
            label = label[1:-1]
        start = '0' * (6 - len(start)) + start
        end = '0' * (6 - len(end)) + end
        path_to_video = os.path.join(data_path, f'{label}/{yt_id}_{start}_{end}.mp4')
        if os.stat(path_to_video).st_size != 0:
            f_new.write(line + '\n')


if __name__ == '__main__':
    main()

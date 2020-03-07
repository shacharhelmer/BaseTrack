from tracker.post_commit_scripts.mysql_pre_commit import main as mysql_main
from tracker.setup import load_conf
from os.path import realpath


def main():
    settings = load_conf()
    output_dir = realpath('output')
    print(output_dir)
    if settings['db']['type'] == 'mysql':
        mysql_main(output_dir=output_dir)

if __name__ == '__main__':
    main()
from pre_commit_scripts.mysql_pre_commit import main as mysql_main
from config.setup import load_conf
from os.path import abspath


def main():
    settings = load_conf()
    output_dir = abspath(__file__ + '/../../output')
    print(output_dir)
    if settings['db']['type'] == 'mysql':
        mysql_main(output_dir=output_dir)

if __name__ == '__main__':
    main()
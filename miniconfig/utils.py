import os
import subprocess

def make_config(config_dict, dest_dir=None):
    """
    Create a miniconfig-compatible config file from keys and values
    :param config_dict: the config dict to write
    :param dest_dir: destination directory to write `config` file to
                     (optional: defaults to current working directory)
    """
    dest_dir = dest_dir or os.getcwd()
    pth = os.path.join(dest_dir, 'config')
    s = "\n".join(["{item[0]}={item[1]}".format(item=item) for item in
                   config_dict.iteritems()])
    with open(pth, "w") as fil:
        fil.write(s)


def from_heroku(app=None, dest_dir=None):
    """
    Create a miniconfig-compatible config file from a Heroku config
    :param app: name of Heroku app whose config will be written
                (optional: defaults to app corresponding to current working
                directory)
    :param dest_dir: destination directory to write `config` file to
                     (optional: defaults to current working directory)
    """
    command = ["heroku", "config", "-s"]
    if app:
        command.extend(['--app', app])
    result = subprocess.check_output(command)
    dest_dir = dest_dir or os.getcwd()
    pth = os.path.join(dest_dir, 'config')
    with open(pth, 'w') as fil:
        fil.write(result)


def get_config(dest=None):
    """
    Load configuration from a file, defaulting to a file named 'config' in
    the current directory. The file can either contain configuration
    information in the form of "key=value" pairs separated by newlines, or
    filepaths pointing to other config files whose key-value pairs will be
    merged
    :param dest: file path to read config from
    """
    dest = dest or "config"
    other_configs = []
    config_dict = {}
    with open(dest) as fil:
        for line in fil:
            line = line.rstrip()
            if os.path.isfile(line):
                other_configs.append(line)
            elif line.startswith("#"):
                pass
            else:
                key, val = line.split('=', 1)
                config_dict[key] = val
    for config_file in other_configs:
        config_dict.update(get_config(config_file))
    return config_dict


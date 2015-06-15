import os
import subprocess

def make_config(dest_dir=None, **config):
    """
    Create a miniconfig-compatible config file from keys and values
    """
    dest_dir = dest_dir or os.getcwd()
    pth = os.path.join(dest_dir, 'config')
    s = "\n".join(["{item[0]}={item[1]}".format(item=item) for item in
                   config.iteritems()])
    with open(pth, "w") as fil:
        fil.write(s)


def from_heroku(dest_dir=None, app=None):
    """
    Create a miniconfig-compatible config file from a Heroku config
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
    """
    dest = dest or "config"
    other_configs = []
    config_dict = {}
    with open(dest) as fil:
        for line in fil:
            line = line.rstrip()
            if os.path.isfile(line):
                other_configs.append(line)
            else:
                key, val = line.split('=', maxsplit=1)
                config_dict[key] = val
    for config_file in other_configs:
        config_dict.update(get_config(config_file))
    return config_dict


# Miniconfig    

## What    

A minimal, opinionated config solution for Python.

## Why

Config is irritating--there are a lot of solutions, and stuff gets really
complex and fiddly. Sometimes, all you (I) want is a friggin' dictionary.

## How

Mini(config)mally:

    from miniconfig import config

    def my_thing_that_needs_config():

        configure_me(config['foo'], config['bar'])


In brief, `miniconfig.config` is a Python `dict` containing your configuration
stuff. By default, it's sourced from a file called `config` in the current
directory. This file must contain lines that are:

* key-value pairs: `mykey=myval`
* file paths: `/Users/samuelraker/myproject/somedir/config`

The files at each file path will be read in the same way as the original, and
their key-value pairs will be merged together. Caveats:

* You can create cyclical dependencies if `configA` points to `configB` that
  points to `configA`. Don't do this. 
* `miniconfig` doesn't do hierarchies or sections or any other kind of
  automatic namespacing; configurations are merged via `dict.update`, so the
  potential exists for values to get clobbered. Just do it yourself: call your
  database password `database_password` and your API password `API_password`
  and it'll be fine.

Any line starting with a `#` will be ignored as a comment.

Note that the file paths *must* be full, absolute paths, including the
filename. `/path/to/a/directory_that_contains_the_file` won't work.

You can freely mix filepaths, key-value pairs, and comments, so the following
is valid:

    username=swizzard

    password=thisisafakepasswordduh

    # here's a comment

    /Users/samuelraker/myproject/database_stuff/database_config

    # here's another comment

    foo=bar

    /Users/samuelraker/myproject/other_stuff/whatever_config


## Who

Copyright © 2015 Sam Raker <sam.raker@gmail.com>. This work is free. You can
redistribute it and/or modify it under the terms of the Do What The Fuck You
Want To Public License, Version 2, as published by Sam Hocevar. See the COPYING
file for more details. 

    /* This program is free software. It comes without any warranty, to
    * the extent permitted by applicable law. You can redistribute it
    * and/or modify it under the terms of the Do What The Fuck You Want
    * To Public License, Version 2, as published by Sam Hocevar. See
    * http://www.wtfpl.net/ for more details. */

#!/usr/bin/env python3

from os import remove
from os.path import basename, dirname, join, realpath

from jinja2 import Environment, FileSystemLoader

script_path = realpath(__file__)
script_dir = dirname(script_path)
app_name = basename(script_dir)

env = Environment(
  loader=FileSystemLoader(script_dir)
)

template_args = {
  'name': app_name
}

def reify_template(filename):
  path = join(script_dir, filename)
  str = env.get_template(filename + ".jinja")\
    .render(template_args)

  with open(path, mode="w+") as f:
    f.write(str)

  remove(path + ".jinja")

if __name__ == "__main__":
  reify_template("CMakeLists.txt")
  reify_template("README.md")
  reify_template(".gitignore")

  remove(script_path)

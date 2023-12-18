#!/bin/bash

find . \( -type d -name .git -prune \) -o \( -type f -not -name 'tasks.json' \) -print0 | xargs -0 sed -i "s/ant_colony_bench/$1/g"

mv ant_colony_bench $1
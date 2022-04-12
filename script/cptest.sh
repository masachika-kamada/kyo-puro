#!/bin/bash

source C:/Users/MK/Anaconda3/etc/profile.d/conda.sh
conda activate opencv

problem_name=$1
test_dir=test/${problem_name}
base_url=${problem_name%_*}

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python src/${problem_name}.py" -d test/${problem_name}

sleep 10
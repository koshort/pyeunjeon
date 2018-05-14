#! /bin/bash
#
# Copyright 2018 nyanye
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

os=$(uname)

if [ $os == "Linux" ]; then
    echo "Installing MeCab-ko"
elif [ $os == "Darwin" ]; then
    echo "Installing MeCab-ko"
else
    echo "This script does not support this OS."
    exit 0
fi

# install mecab-ko
cd /tmp
curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
tar zxfv mecab-0.996-ko-0.9.1.tar.gz
cd mecab-0.996-ko-0.9.2
./configure
make
make check
sudo make install

# Trouble-shooting
# sudo vim /etc/ld.so.conf add following:
# /usr/local/lib
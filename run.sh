#!/usr/bin/env bash

cd `dirname $0`
cd src
python -m awesome_game/application $@

#!/usr/bin/env bash

CONFIG=config.h

:>$CONFIG

echo "#define PICOSAT_CC \"$1\"" >>$CONFIG
echo "#define PICOSAT_CFLAGS \"$2\"" >>$CONFIG
echo "#define PICOSAT_VERSION \"$3\"" >>$CONFIG

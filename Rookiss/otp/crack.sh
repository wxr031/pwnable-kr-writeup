#!/usr/bin/env bash
ulimit -f 0 && python -c "from subprocess import Popen; Popen(['./otp', ''])"

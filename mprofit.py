import logging
import sys

log_level = logging.INFO
rl = logging.getLogger()
st = logging.StreamHandler(sys.stdout)
rl.addHandler(st)
rl.setLevel(log_level)

rl.debug("A DEBUG message")

rl.info("An INFO message")
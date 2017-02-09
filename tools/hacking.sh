#!/bin/bash
flake8 vbclient | tee flake8.log
exit ${PIPESTATUS[0]}

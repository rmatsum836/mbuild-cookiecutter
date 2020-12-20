#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate base
conda activate mbuild_cookie

if [ "$@" == "none" ]; then
	bash
else
	$@
fi

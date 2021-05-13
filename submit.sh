#!/usr/bin/env bash
rm -rf submit/
mkdir -p submit

prepare () {
	    cp $1 submit/
    }

echo "Creating tarball..."
prepare ./environments/MapEnvironment.py
prepare ./planners/AStarPlanner.py
prepare ./planners/RRTPlanner.py
prepare ./planners/RRTStarPlanner.py
prepare ./planners/RRTPlannerNonholonomic.py

zip -r submit.zip submit
rm -rf submit/
echo "Done. Please upload submit.zip to Gradescope."

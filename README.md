# Run DX Checker
Runs workflow for eggd_dx_checker.

## What does this script do?
Calls DNAnexus workflow to run Sentieon followed by eggd_dx_checker.

## What are typical use cases for this script?

To be run weekly to check for any effects of DNAnexus updates. 

## What data are required for this script to run?

This requires the config.txt file to be modified by adding a valid DNAnexus token to access the projects specified within config.txt.
A path to config.txt must be provided as a command line argument when running a docker container for run_dx_checker.
Example: docker run --env-file <path/to/config.txt> run-dx-checker

## What does this script output?

Makes directory in DNAneuxs project with current date, and outputs dx check workflow into it.

### This was made by EMEE GLH

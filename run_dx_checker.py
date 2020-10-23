#!/usr/bin/python

"""Runs workflow to run eggd_dx_checker app on a weekly basis to
monitor for any effects of weekly DNAnexus updates"""

import datetime
import subprocess
import sys

import dxpy as dxpy

from config import projectID, workflowID, inputs
from dnanexus_token import AUTH_TOKEN


def get_date():
    """Return current data for weekly run folder name"""
    return datetime.datetime.now().strftime("%y%m%d-%H%M")


def make_dir(date):
    """Make dir for weekly run output from current date"""
    project = dxpy.DXProject(projectID)
    out_dir = "/dx_weekly_check/{}".format(date)
    project.new_folder(folder=out_dir)

    return out_dir


def run_check(out_dir):
    """Run weekly dx checker with workflow presets"""
    # set workflow params
    workflow = dxpy.bindings.dxworkflow.DXWorkflow(workflowID, projectID)

    # set output dir of Sentieon to workflow output dir
    workflow.update_stage(0, folder=out_dir)
    workflow.update_stage(1, folder=out_dir)

    # run worflow
    workflow.run(workflow_input=inputs, rerun_stages=[0, 1], project=projectID)


def main():

    # set token to env for dx authentication
    DX_SECURITY_CONTEXT = {
        "auth_token_type": "Bearer",
        "auth_token": AUTH_TOKEN
    }
    dxpy.set_security_context(DX_SECURITY_CONTEXT)

    # get date to name as output dir for workflow
    date = get_date()

    # make output dir
    out_dir = make_dir(date)

    # run workflow
    run_check(out_dir)


if __name__ == "__main__":
    main()

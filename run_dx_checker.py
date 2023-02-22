#!/usr/bin/python

"""Runs workflow to run eggd_dx_checker app on a weekly basis to
monitor for any effects of weekly DNAnexus updates"""

import datetime
import subprocess
import sys

import dxpy

# get environment variables
AUTH_TOKEN = os.environ['AUTH_TOKEN']
projectID = os.environ['projectID']
workflowID = os.environ['workflowID']

inputs = {
    "0.genomebwaindex_targz": {
        '$dnanexus_link': {
            'project': os.environ['genomebwaindex_targz_projectID'],
            'id': os.environ['genomebwaindex_targz_fileID']
        }
    },
    "0.genome_fastagz": {
        '$dnanexus_link': os.environ['genome_fastagz_fileID']
    },
    "0.reads_fastqgzs": [
        {'$dnanexus_link': {
            'project': os.environ['reads_fastqgzs_projectID'],
            'id': os.environ['reads_fastqgzs_1_fileID']
        }},
        {'$dnanexus_link': {
            'project': os.environ['reads_fastqgzs_projectID'],
            'id': os.environ['reads_fastqgzs_2_fileID']
        }}
    ],
    "0.reads2_fastqgzs": [
        {'$dnanexus_link': {
            'project': os.environ['reads_fastqgzs_projectID'],
            'id': os.environ['reads2_fastqgzs_1_fileID']
        }},
        {'$dnanexus_link': {
            'project': os.environ['reads_fastqgzs_projectID'],
            'id': os.environ['reads2_fastqgzs_2_fileID']
        }}
    ],
    "1.query_vcf": {'$dnanexus_link': {
        'stage': os.environ['query_vcf_stageID'],
        'outputField': 'variants_vcf'
    }},
    "1.truth_vcf": {"$dnanexus_link": {
        "project": os.environ['reads_fastqgzs_projectID'], 
        "id": os.environ['truth_vcf_fileID']
    }}
}


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

import json
import os
import subprocess
import sys

from .utils import console

MOCK = os.getenv("MOCK", "False").lower() == "True"

fake_oarstat = """{
    "13056638" : {
      "reservation" : "None",
      "dependencies" : [],
      "state" : "Waiting",
      "job_user" : "wantoun",
      "startTime" : 1689242435,
      "initial_request" : "oarsub -S ./run_training.oar; #OAR -n random_model_en_rdataset_50k_split_204; #OAR -l /nodes=1/gpunum=1,walltime=72:00:0; #OAR -p gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr'; #OAR -t besteffor; #OAR -O ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.lo; #OAR -E ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.elo",
      "name" : "random_model_en_rdataset_50k_split_2048",
      "jobType" : "PASSIVE",
      "properties" : "((gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr')) AND besteffort = 'YES') AND drain='NO'",
      "stdout_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056638.log",
      "stopTime" : 0,
      "queue" : "besteffort",
      "Job_Id" : "13056638",
      "walltime" : 259200,
      "resubmit_job_id" : 0,
      "types" : [
         "besteffort"
      ],
      "array_index" : 1,
      "assigned_network_address" : [
         "jefgpu48.rorg.fr"
      ],
      "project" : "default",
      "submissionTime" : 1689242423,
      "scheduledStart" : 1689242435,
      "array_id" : 13056638,
      "wanted_resources" : "-l \\"{type = 'default'}/network_address=1/gpunum=1,walltime=72:0:0\\" ",
      "exit_code" : null,
      "stderr_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056638.elog",
      "command" : "./run_training.oar",
      "owner" : "wantoun",
      "cpuset_name" : "wantoun_13056638",
      "message" : "R=26,W=72:0:0,J=B,N=random_model_en_rdataset_50k_split_2048,T=besteffort (Karma=0.145,quota_ok)",
      "assigned_resources" : [
         6849,
         6850,
         6857,
         6858,
         6865,
         6866,
         6873,
         6874,
         6881,
         6882,
         6889,
         6890,
         6897,
         6898,
         6905,
         6906,
         6913,
         6914,
         6921,
         6922,
         6929,
         6930,
         6937,
         6938,
         6945,
         6946
      ],
      "events" : [
         {
            "to_check" : "NO",
            "job_id" : 13056638,
            "event_id" : "27924708",
            "date" : 1689242445,
            "type" : "SCHEDULER_PRIORITY_UPDATED_START",
            "description" : "Scheduler priority for job 13056638 updated (network_address/resource_id)"
         }
      ],
      "launchingDirectory" : "/home//wantoun/repos/oartui"
   },
    "13056639" : {
      "reservation" : "None",
      "dependencies" : [],
      "state" : "Running",
      "job_user" : "wantoun",
      "startTime" : 1689242436,
      "initial_request" : "oarsub -S ./run_training.oar; #OAR -n random_model_en_rdataset_50k_split_204; #OAR -l /nodes=1/gpunum=1,walltime=72:00:0; #OAR -p gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr'; #OAR -t besteffor; #OAR -O ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.lo; #OAR -E ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.elo",
      "name" : "random_model_en_rdataset_50k_split_2048",
      "jobType" : "PASSIVE",
      "properties" : "((gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr')) AND besteffort = 'YES') AND drain='NO'",
      "stdout_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056639.log",
      "stopTime" : 0,
      "queue" : "besteffort",
      "Job_Id" : "13056639",
      "walltime" : 259200,
      "resubmit_job_id" : 0,
      "types" : [
         "besteffort"
      ],
      "array_index" : 1,
      "assigned_network_address" : [
         "jefgpu48.rorg.fr"
      ],
      "project" : "default",
      "submissionTime" : 1689242424,
      "scheduledStart" : 1689242435,
      "array_id" : 13056639,
      "wanted_resources" : "-l \\"{type = 'default'}/network_address=1/gpunum=1,walltime=72:0:0\\" ",
      "exit_code" : null,
      "stderr_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056639.elog",
      "command" : "./run_training.oar",
      "owner" : "wantoun",
      "cpuset_name" : "wantoun_13056639",
      "message" : "R=26,W=72:0:0,J=B,N=random_model_en_rdataset_50k_split_2048,T=besteffort (Karma=0.145,quota_ok)",
      "assigned_resources" : [
         6849,
         6850,
         6857,
         6858,
         6865,
         6866,
         6873,
         6874,
         6881,
         6882,
         6889,
         6890,
         6897,
         6898,
         6905,
         6906,
         6913,
         6914,
         6921,
         6922,
         6929,
         6930,
         6937,
         6938,
         6945,
         6946
      ],
      "events" : [
         {
            "to_check" : "YES",
            "job_id" : 13056639,
            "event_id" : "28017253",
            "date" : 1691700968,
            "type" : "FRAG_JOB_REQUEST",
            "description" : "User wantoun requested to frag the job 13056639"
         }
      ],
      "launchingDirectory" : "/home/wantoun/repos/oartui"
   },
    "13056640" : {
      "reservation" : "None",
      "dependencies" : [],
      "state" : "Running",
      "job_user" : "wantoun",
      "startTime" : 1689242437,
      "initial_request" : "oarsub -S ./run_training.oar; #OAR -n random_model_en_rdataset_50k_split_204; #OAR -l /nodes=1/gpunum=1,walltime=72:00:0; #OAR -p gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr'; #OAR -t besteffor; #OAR -O ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.lo; #OAR -E ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.elo",
      "name" : "random_model_en_rdataset_50k_split_2048",
      "jobType" : "PASSIVE",
      "properties" : "((gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr')) AND besteffort = 'YES') AND drain='NO'",
      "stdout_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056640.log",
      "stopTime" : 0,
      "queue" : "besteffort",
      "Job_Id" : "13056640",
      "walltime" : 259200,
      "resubmit_job_id" : 0,
      "types" : [
         "besteffort"
      ],
      "array_index" : 1,
      "assigned_network_address" : [
         "jefgpu48.rorg.fr"
      ],
      "project" : "default",
      "submissionTime" : 1689242425,
      "scheduledStart" : 1689242436,
      "array_id" : 13056640,
      "wanted_resources" : "-l \\"{type = 'default'}/network_address=1/gpunum=1,walltime=72:0:0\\" ",
      "exit_code" : null,
      "stderr_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056640.elog",
      "command" : "./run_training.oar",
      "owner" : "wantoun",
      "cpuset_name" : "wantoun_13056640",
      "message" : "R=26,W=72:0:0,J=B,N=random_model_en_rdataset_50k_split_2048,T=besteffort (Karma=0.145,quota_ok)",
      "assigned_resources" : [
         6849,
         6850,
         6857,
         6858,
         6865,
         6866,
         6873,
         6874,
         6881,
         6882,
         6889,
         6890,
         6897,
         6898,
         6905,
         6906,
         6913,
         6914,
         6921,
         6922,
         6929,
         6930,
         6937,
         6938,
         6945,
         6946
      ],
      "events" : [
         {
            "to_check" : "NO",
            "job_id" : 13056640,
            "event_id" : "27924708",
            "date" : 1689242447,
            "type" : "SCHEDULER_PRIORITY_UPDATED_START",
            "description" : "Scheduler priority for job 13056640 updated (network_address/resource_id)"
         }
      ],
      "launchingDirectory" : "/home/wantoun/repos/oartui"
   },
    "13056641" : {
      "reservation" : "None",
      "dependencies" : [],
      "state" : "Running",
      "job_user" : "wantoun",
      "startTime" : 1689242436,
      "initial_request" : "oarsub -S ./run_training.oar; #OAR -n random_model_en_rdataset_50k_split_204; #OAR -l /nodes=1/gpunum=1,walltime=72:00:0; #OAR -p gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr'; #OAR -t besteffor; #OAR -O ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.lo; #OAR -E ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.elo",
      "name" : "random_model_en_rdataset_50k_split_2048",
      "jobType" : "PASSIVE",
      "properties" : "((gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr')) AND besteffort = 'YES') AND drain='NO'",
      "stdout_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056641.log",
      "stopTime" : 0,
      "queue" : "besteffort",
      "Job_Id" : "13056641",
      "walltime" : 259200,
      "resubmit_job_id" : 0,
      "types" : [
         "besteffort"
      ],
      "array_index" : 2,
      "assigned_network_address" : [
         "jefgpu48.rorg.fr"
      ],
      "project" : "default",
      "submissionTime" : 1689242424,
      "scheduledStart" : 1689242435,
      "array_id" : 13056640,
      "wanted_resources" : "-l \\"{type = 'default'}/network_address=1/gpunum=1,walltime=72:0:0\\" ",
      "exit_code" : null,
      "stderr_file" : "./logs/random_model_en_rdataset_50k_split_2048_13056641.elog",
      "command" : "./run_training.oar",
      "owner" : "wantoun",
      "cpuset_name" : "wantoun_13056641",
      "message" : "R=26,W=72:0:0,J=B,N=random_model_en_rdataset_50k_split_2048,T=besteffort (Karma=0.145,quota_ok)",
      "assigned_resources" : [
         6849,
         6850,
         6857,
         6858,
         6865,
         6866,
         6873,
         6874,
         6881,
         6882,
         6889,
         6890,
         6897,
         6898,
         6905,
         6906,
         6913,
         6914,
         6921,
         6922,
         6929,
         6930,
         6937,
         6938,
         6945,
         6946
      ],
      "events" : [
         {
            "to_check" : "NO",
            "job_id" : 13056641,
            "event_id" : "27924708",
            "date" : 1689242446,
            "type" : "SCHEDULER_PRIORITY_UPDATED_START",
            "description" : "Scheduler priority for job 13056641 updated (network_address/resource_id)"
         }
      ],
      "launchingDirectory" : "/home/wantoun/repos/oartui"
   },
    "13056633" : {
      "reservation" : "None",
      "dependencies" : [],
      "state" : "Running",
      "job_user" : "wantoun",
      "startTime" : 1689242436,
      "initial_request" : "oarsub -S ./run_training.oar; #OAR -n random_model_en_rdataset_50k_split_204; #OAR -l /nodes=1/gpunum=1,walltime=72:00:0; #OAR -p gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr'; #OAR -t besteffor; #OAR -O ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.lo; #OAR -E ./logs/random_model_en_rdataset_50k_split_2048_%jobid%.elo",
      "name" : "random_model_en_rdataset_50k_split_2048",
      "jobType" : "PASSIVE",
      "properties" : "((gpu='YES' and gpumem>40000 and (host='jefgpu47.rorg.fr' or host='jefgpu48.rorg.fr' or host='jefgpu49.rorg.fr' or host='jefgpu50.rorg.fr' or host='jefgpu51.rorg.fr')) AND besteffort = 'YES') AND drain='NO'",
      "stdout_file" : "README.md",
      "stopTime" : 0,
      "queue" : "besteffort",
      "Job_Id" : "13056633",
      "walltime" : 259200,
      "resubmit_job_id" : 0,
      "types" : [
         "besteffort"
      ],
      "array_index" : 1,
      "assigned_network_address" : [
         "jefgpu48.rorg.fr"
      ],
      "project" : "default",
      "submissionTime" : 1689242424,
      "scheduledStart" : 1689242435,
      "array_id" : 13056633,
      "wanted_resources" : "-l \\"{type = 'default'}/network_address=1/gpunum=1,walltime=72:0:0\\" ",
      "exit_code" : null,
      "stderr_file" : "README.md",
      "command" : "./run_training.oar",
      "owner" : "wantoun",
      "cpuset_name" : "wantoun_13056633",
      "message" : "R=26,W=72:0:0,J=B,N=random_model_en_rdataset_50k_split_2048,T=besteffort (Karma=0.145,quota_ok)",
      "assigned_resources" : [
         6849,
         6850,
         6857,
         6858,
         6865,
         6866,
         6873,
         6874,
         6881,
         6882,
         6889,
         6890,
         6897,
         6898,
         6905,
         6906,
         6913,
         6914,
         6921,
         6922,
         6929,
         6930,
         6937,
         6938,
         6945,
         6946
      ],
      "events" : [
         {
            "to_check" : "NO",
            "job_id" : 13056633,
            "event_id" : "27924708",
            "date" : 1689242446,
            "type" : "SCHEDULER_PRIORITY_UPDATED_START",
            "description" : "Scheduler priority for job 13056633 updated (network_address/resource_id)"
         }
      ],
      "launchingDirectory" : "/home/wantoun/repos/oartui"
   }
}
"""


def get_running_jobs(
    mock: bool = False, no_jobs_msg: str = "[yellow]No Jobs are running![/yellow]"
):
    if mock:
        running_jobs = fake_oarstat
    else:
        try:
            running_jobs = subprocess.check_output(
                ["oarstat", "--array", "-u", "-J", "-f"], stderr=subprocess.DEVNULL
            ).decode("utf-8")
        except subprocess.CalledProcessError as e:
            console.print(no_jobs_msg)
            return None

    running_jobs_dict = json.loads(running_jobs)
    # sort by job id
    running_jobs_dict = dict(sorted(running_jobs_dict.items(), key=lambda x: x[0]))
    return running_jobs_dict


def get_rich_state(state: str):
    if state == "Running":
        return "[green]Running[/green]"
    elif state == "Waiting":
        return "[blue]Waiting[blue]"
    elif state == "Finishing":
        return "[yellow]Finishing[/yellow]"
    elif "To be Deleted" in state:
        actual_state = get_rich_state(state.replace("(To be Deleted)", "").strip())
        return f"{actual_state} [red](To be Deleted)[/red]"
    else:
        return state

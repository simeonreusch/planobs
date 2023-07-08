#!/usr/bin/env python3
import logging

import matplotlib.pyplot as plt  # type: ignore

from planobs.api import Queue
from planobs.models import TooTarget
from planobs.multiday_plan import MultiDayObservation
from planobs.plan import PlanObservation

logging.basicConfig()
logging.getLogger("planobs.plan").setLevel(logging.INFO)
logging.getLogger("planobs.gcn_parser").setLevel(logging.INFO)

name = "IC230707A"  # Name of the alert object
max_airmass = 1.9
date = "2023-07-09"

plan = PlanObservation(
    name=name,
    date=date,
    alertsource="icecube",
    switch_filters=False,
    max_airmass=max_airmass,
)
plan.plot_target()  # Plots the observing conditions
plan.request_ztf_fields()  # Checks in which ZTF fields

observationplan = MultiDayObservation(
    name=name,
    startdate=None,
    max_airmass=max_airmass,
    switch_filters=False,
    # fieldid=434,  # if you want to override recommended field
)
observationplan.print_plan()
summary = observationplan.summarytext
print(summary)

triggers = observationplan.triggers
print(triggers)

q = Queue(user="DESY")

for i, trigger in enumerate(triggers):
    q.add_trigger_to_queue(
        trigger_name=f"ToO_{name}",
        validity_window_start_mjd=trigger["mjd_start"],
        validity_window_end_mjd=trigger["mjd_end"],
        targets=[
            TooTarget(
                field_id=trigger["field_id"],
                filter_id=trigger["filter_id"],
                exposure_time=trigger["exposure_time"],
            )
        ],
    )

q.print()
# q.submit_queue()  # uncomment to submit for real

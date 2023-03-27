#!/usr/bin/env python3
import logging

import matplotlib.pyplot as plt  # type: ignore
from planobs.api import Queue
from planobs.multiday_plan import MultiDayObservation
from planobs.plan import PlanObservation

logging.basicConfig()
logging.getLogger("planobs.plan").setLevel(logging.INFO)
logging.getLogger("planobs.gcn_parser").setLevel(logging.INFO)

name = "IC221223A"  # Name of the alert object
max_airmass = 1.6
date = "2023-01-13"
# name = "IC201007A"
# date = "2022-12-23"  # This is optional, defaults to today
# ra = 242.58
# dec = 11.61
# Now no ra and dec values are given, but alertsource is set to 'icecube'. This enables GCN archive parsing for the alert name. If it is not found, it will use the latest GCN notice (these are automated).

plan = PlanObservation(
    name=name,
    date=date,
    alertsource="icecube",
    switch_filters=False,
    max_airmass=max_airmass,
)
plan.plot_target()  # Plots the observing conditions
plan.request_ztf_fields()  # Checks in which ZTF fields this object is observable
# # plan.plot_finding_chart()
plt.close()
quit()


# observationplan = MultiDayObservation(
#     name=name, startdate=None, max_airmass=max_airmass, switch_filters=False
# )
# observationplan.print_plan()
# summary = observationplan.summarytext
# print(summary)

# triggers = observationplan.triggers
# print(triggers)

# q = Queue(user="DESY")

# for i, trigger in enumerate(triggers):
#     q.add_trigger_to_queue(
#         trigger_name=f"ToO_{name}",
#         validity_window_start_mjd=trigger["mjd_start"],
#         validity_window_end_mjd=trigger["mjd_end"],
#         field_id=trigger["field_id"],
#         filter_id=trigger["filter_id"],
#         exposure_time=trigger["exposure_time"],
#     )
q = Queue(user="DESY")
lol = q.get_too_queues_name_and_date()
print(lol)
# q.print()
# bla = q.get_triggers()
# print(repr(bla))
# q.submit_queue()

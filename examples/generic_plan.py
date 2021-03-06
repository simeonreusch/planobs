#!/usr/bin/env python3
from planobs.plan import PlanObservation

name = "testalert"  # Name of the alert object
date = "2020-05-05"  # This is optional, defaults to today
ra = 133.7
dec = 13.37

plan = PlanObservation(name=name, date=date, ra=ra, dec=dec)
plan.plot_target()  # Plots the observing conditions
plan.request_ztf_fields()  # Checks in which ZTF fields this object is observable

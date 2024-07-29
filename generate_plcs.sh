#!/bin/sh
# Generates Python packages for PLCS directly from the PLCS XSD URI to org.oasis-open.plcs
xsdata generate --package org.oasis-open.plcs https://docs.oasis-open.org/plcs/plcslib/v1.0/cs01/data/PLCS/psm_model/plcs_psm.xsd
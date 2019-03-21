"""Test filtering plots."""

from neurodsp.filt import filter_signal, design_fir_filter, compute_frequency_response
from neurodsp.plts.filt import *

from .util import plot_test

###################################################################################################
###################################################################################################

@plot_test
def test_plot_filter_properties():

    fs = 1000
    coefs = design_fir_filter(2000, fs, 'bandpass', (8, 12), 3)
    f_db, db = compute_frequency_response(coefs, a_vals=1, fs=1000)

    plot_filter_properties(f_db, db, fs, coefs)

    assert True

@plot_test
def test_plot_frequency_response():

    coefs = design_fir_filter(2000, 1000, 'bandpass', (8, 12), 3)
    f_db, db = compute_frequency_response(coefs, a_vals=1, fs=1000)

    plot_frequency_response(f_db, db)

    assert True

@plot_test
def test_plot_impulse_response():

    fs = 1000
    coefs = design_fir_filter(2000, fs, 'bandpass', (8, 12), 3)

    plot_impulse_response(fs, coefs)

    assert True

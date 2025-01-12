#  AUTO-GENERATED FILE - MODIFY AT OWN RISK
#  Project: qcware
#  Copyright (c) 2019 QC Ware Corp - All Rights Reserved

import numpy

import quasar

from typing import Union

import warnings
from ...api_calls import declare_api_call


@declare_api_call(name="qutils.qdot", endpoint="qutils/qdot")
def qdot(
    x: Union[float, numpy.ndarray],
    y: Union[float, numpy.ndarray],
    circuit: quasar.Circuit = None,
    loader_mode: str = "parallel",
    circuit_mode: str = "sequential",
    backend: str = "qcware/cpu_simulator",
    num_measurements: int = None,
):
    r"""Outputs the dot product of two arrays; quantum analogue of::
      numpy.dot

    Cases (following numpy.dot):
      x is 1d, y is 1d; performs vector - vector multiplication. Returns float.
      x is 2d, y is 1d; performs matrix - vector multiplication. Returns 1d array.
      x is 1d, y is 2d; performs vector - matrix multiplication. Returns 1d array.
      x is 2d, y is 2d; performs matrix - matrix multiplication. Returns 2d array.


    Arguments:

    :param x: 1d or 2d array
    :type x: Union[float, numpy.ndarray]

    :param y: 1d or 2d array
    :type y: Union[float, numpy.ndarray]

    :param circuit: Circuit to use for evaluation (None to implicitly create circuit), defaults to None
    :type circuit: quasar.Circuit

    :param loader_mode: , defaults to parallel
    :type loader_mode: str

    :param circuit_mode: , defaults to sequential
    :type circuit_mode: str

    :param backend: , defaults to qcware/cpu_simulator
    :type backend: str

    :param num_measurements: , defaults to None
    :type num_measurements: int


    :return: float, 1d array, or 2d array: dot product
    :rtype: Union[float, numpy.ndarray]"""
    pass


def submit_qdot(*args, **kwargs):
    """This method is deprecated; please use qdot.submit"""
    w = "The old submit_qdot function has been deprecated and will be removed.  Please use qdot.submit"
    warnings.warn(w, DeprecationWarning)
    print(w)
    return qdot.submit(*args, **kwargs)


async def async_qdot(*args, **kwargs):
    """This method is deprecated; please use qdot.call_async"""
    w = "The old async_qdot function has been deprecated and will be removed.  Please use qdot.call_async"
    warnings.warn(w, DeprecationWarning)
    print(w)
    return await qdot.call_async(*args, **kwargs)

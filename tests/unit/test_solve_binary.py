import qcware
import pytest
import itertools


@pytest.mark.parametrize(
    "backend",
    ('qcware/cpu', 'dwave/2000q', 'dwave/advantage')  # ,
    #                           'awsbraket/dwave/2000q', 'awsbraket/dwave/advantage')
)
def test_solve_binary(backend):
    Q = {(0, 0): 1, (1, 1): 1, (0, 1): -2, (2, 2): -2, (3, 3): -4, (3, 2): -6}

    result = qcware.optimization.solve_binary(Q=Q, backend=backend)
    assert (result['solution'] == [0, 0, 1, 1]
            or result['solution'] == [1, 1, 1, 1])


@pytest.mark.parametrize("backend,nmeasurement",
                         [('qcware/cpu_simulator', None),
                          ('qcware/gpu_simulator', None),
                          ('awsbraket/sv1', 1000)])
def test_solve_binary_qaoa(backend: str, nmeasurement: int):
    Q = {(0, 0): 1, (1, 1): 1, (0, 1): -2, (2, 2): -2, (3, 3): -4, (3, 2): -6}

    result = qcware.optimization.solve_binary(Q=Q,
                                              backend=backend,
                                              qaoa_optimizer='analytical',
                                              qaoa_nmeasurement=nmeasurement)
    assert (result['solution'] == [0, 0, 1, 1]
            or result['solution'] == [1, 1, 1, 1])


@pytest.mark.parametrize('optimizer, backend',
                         itertools.product(
                             ('COBYLA', 'bounded_Powell', 'analytical'),
                             ('qcware/cpu_simulator', 'qcware/gpu_simulator')))
def test_various_qaoa_optimizers(optimizer, backend):
    Q = {(0, 0): 1, (1, 1): 1, (0, 1): -2, (2, 2): -2, (3, 3): -4, (3, 2): -6}
    result = qcware.optimization.solve_binary(Q=Q,
                                              backend=backend,
                                              qaoa_optimizer=optimizer)
    assert (result['solution'] == [0, 0, 1, 1]
            or result['solution'] == [1, 1, 1, 1])


@pytest.mark.parametrize('backend',
                         ('qcware/cpu_simulator', 'qcware/gpu_simulator'))
def test_analytical_angles_with_qaoa(backend):
    Q = {(0, 0): 1, (1, 1): 1, (0, 1): -2, (2, 2): -2, (3, 3): -4, (3, 2): -5}

    exvals, angles, Z = qcware.optimization.find_optimal_qaoa_angles(
        Q, num_evals=100, num_min_vals=10)
    # print("EXVALS: ", exvals)
    # print("ANGLES: ", angles)

    result = qcware.optimization.solve_binary(Q=Q,
                                              backend=backend,
                                              qaoa_beta=angles[1][0],
                                              qaoa_gamma=angles[1][1],
                                              qaoa_p_val=1)
    assert (result['solution'] == [0, 0, 1, 1]
            or result['solution'] == [1, 0, 1, 0]
            or result['solution'] == [1, 1, 1, 1])

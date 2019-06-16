#!/usr/bin/env python3
# encoding: utf-8
"""Genetic optimizer example

Examples included:

 --source="sin-minimize-FoM.py"
   minimize error to fit polynomial coefficients to sin function.

 --source="sin-maximize-FoM.py"
   maximize error to fit polynomial coefficients to sin function.

 --source="sin-time-accuracy.py"
   minimize both error and time taken when fitting polynomial to sin function.
"""
from crayai import hpo


import argparse

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--source', type=str, default='sin-time-accuracy.py',
                    help='source script')

args = parser.parse_args()

evaluator = hpo.Evaluator('python source/{0}'.format(args.source))

params = hpo.Params([["-a", 1.0, (-10.0, 10.0)],
                     ["-b",-1.0, (-10.0, 10.0)],
                     ["-c", 1.0, (-10.0, 10.0)],
                     ["-d",-1.0, (-10.0, 10.0)],
                     ["-e", 1.0, (-10.0, 10.0)],
                     ["-f",-1.0, (-10.0, 10.0)],
                     ["-g", 1.0, (-10.0, 10.0)]])

optimizer = hpo.genetic.Optimizer(evaluator, verbose=True, generations=5, pop_size=10, log_fn='genetic.log')


optimizer.optimize(params)

print(optimizer.best_fom)
print(optimizer.best_params)

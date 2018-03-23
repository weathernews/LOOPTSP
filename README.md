# LOOPTSP
Problem for EBA Virtual Internship2018.

## Problem Outline
This problem is based on TSP (Traveling Salesman Problem).

A container ship leaves a port and returns to the port after touching all given ports
Ideal navigation dates of all each two ports are given, but actual navigation dates changes due to some trouble (In real world, the delay caused by weather condition) 
In this problem, the actual navigation dates (_Actual(Dep, Arr)_) are defined the following:

- _ElpsedDateInDepPort_: Integrating dates from first port on departing port
- _Ideal(Dep, Arr)_: Ideal navigation dates from Dep (Depareture port) to Arr (Arrival port)
- _Actual(Dep, Arr)_ = _Ideal(Dep,Arr)_ + _ElpsedDateInDepPort_ % _Ideal(Dep,Arr)_
- \# “%” means modulo operator

Find voyage route whose integrating date is smallest

|            | TOKYO | OSAKA | NAGOYA | SHANGHAI | LONG_BEACH | SEATTLE |
|------------|-------|-------|--------|----------|------------|---------|
| TOKYO      | -     | 4     | 2      | 8        | 24         | 22      |
| OSAKA      | 4     | -     | 2      | 6        | 26         | 24      |
| NAGOYA     | 2     | 2     | -      | 8        | 24         | 22      |
| SHANGHAI   | 8     | 6     | 8      | -        | 28         | 26      |
| LONG_BEACH | 24    | 26    | 24     | 28       | -          | 4       |
| SEATTLE    | 22    | 24    | 22     | 26       | 4          | -       |

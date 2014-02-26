ARTS
====

(ARTS) Automated Resource Tracking Simulator

In order to test the effectiveness of different scaling mechanisms implemented through CRAFTS, it is necessary to have a framework that can simulate resource utilization in faster than real time. It is also impossible to measure exact over-utilization in a real-world system.

ARTS is designed to solve both of these problems. Rather than getting resource utilization from the system, ARTS will pseudo-randomly create a load pattern based on a specified traffic function. This will allow us to quickly evaluate a large series of scaling situations without the effort of maintaining the full system. It also has the added benefit of allowing us to simulate and measure resource overutilization.

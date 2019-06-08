Navigation :: [Previous Page](LTRPRG-1100-04-Test.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04a2-HighCPU-Ex1.md)

---

## Troubleshoot High CPU with Network Programmability

### Defining the Problem

One glaring problem with troubleshooting fleeting high-CPU issues on a router, is that often by the time an
administrator logs in to troubleshoot, the issue has passed. The goal of this exercise is to utilize skills of the
Network Programmability Ninja to react to a CPU spike immediately, without waiting for a person to log in to the router.
The actions taken can be as simple as information collection, to as intricate as executing configuration changes based
on real-time traffic observed. For this exercise, we will be collecting what is often pertinent information to help
identify the culprit of a high-CPU event.

### Defining the Test

In order to effectively triage an event for high CPU utilization, first it is important to understand what information
is pertinent to triage the situation. 

1. Recording the CPU utilization not only helps to understand the usage in 5 sec, 1 min, 5 min intervals, but also
provides an understanding of whether the CPU has high interrupt usage. This can be gathered from a `# show proc cpu
sorted` output.

2. The same command above also lists the processes and their CPU usage, sorted to start with the heaviest load. This
can be indicative of what is causing high CPU, as it may be tied up under a single process.

3. Visualizing the CPU utilization over a time period can also be helpful to understand if this is an
anomalous spike, or just slightly above normal operating thresholds. It can also help to show if there is a pattern to
when a spike repeats.

3. Sometimes high CPU can be attributed to something a particular user or administrator is doing, so gathering the
active users on the router is also helpful to understand the full picture.

While there are surely other pieces of information that can be helpful, this is a great starting point.

---

Navigation :: [Previous Page](LTRPRG-1100-04-Test.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04a2-HighCPU-Ex1.md)

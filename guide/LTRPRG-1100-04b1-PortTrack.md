Navigation :: [Previous Page](LTRPRG-1100-04a2-HighCPU-Ex1.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04b2-PortTrack-Ex1.md)

---

## Script a Switch Port Tracker

### Defining the Problem

In large campus networks, oftentimes network interfaces or ports are patched to a wall jack, whether or not they are
being used. Over time, the access switch may have all of its physical interfaces filled, creating a problem when a new
network drop needs to be added. When this scenario happens, it is common for someone to ask the question, "What port 
can we disconnect so that we can install a new network patch?"

While this may seem like a straightforward answer of looking for interfaces that are in the "down" state, this may not
necessarily be accurate enough. There are plenty of times that this may lead to a false positive, if an endpoint just
happened to be powered off, disconnected, or temporarily moved when the administrator checked the interface status. For
instance, consider a laptop that is docked at a desk for portions of the day, but the end user takes it to meetings
throughout the day as well. If the network administrator were to check the interface status while that user was
attending a meeting, it may look like a valid port to reclaim. Unfortunately, if this happens, the user will come back
to find that the wired jack at the desk no longer works.

The go-to standard for determining if an "offline" port is "unused" or not is to look at interface counters, e.g. 
bytes in and bytes out.  But, there is no way to know when the interface counters last incremented, only just that 
the counters have incremented since the interface counters were last reset.  Interface counters are valuable and 
everyone hates to reset the interface counters on all ports on a switch to monitor port utilization.

In order to prevent false positives without clearing interface counters, more information about when the interface was 
last up is necessary. While this information is not inherently tracked in a switch, there are several ways it can be 
collected. This example will work through a method of collecting this information on a regular basis, so that if a 
port needs to be reclaimed, the network administrator has a much better idea of which ports have been in an 'offline'
state for a long period of time.

### Defining the Test

The high-level solution requires the following steps:

1. Gather and save the state of each interface on the switch or router, storing it in nonvolatile memory for later
access.

2. Continue to record these interface states on a regular interval, for instance, once every five minutes.

3. Provide a method that a user can request a report to see which ports have been unused for the longest period of time,
as they will be top choices for reclaiming to support a new network patch.

While there are other ways this problem can be solved, this shows one example of a simplistic, automated approach to
provide administrators better information to make a decision at the time of action.  This also demonstrates how to 
take a repetitive series of manual actions and automate them with your new network programmability skills.

---

Navigation :: [Previous Page](LTRPRG-1100-04a2-HighCPU-Ex1.md) :: [Table of Contents](LTRPRG-1100-00-Intro.md#table-of-contents) :: 
[Next Page](LTRPRG-1100-04b2-PortTrack-Ex1.md)

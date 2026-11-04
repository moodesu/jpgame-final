+++
authors = ["JPGame"]
title = "iniBuilds Airbus A350 Full Flight Tutorial — Step-by-Step"
date = 2026-11-03
description = "A reusable step-by-step A350 flight-deck guide for MSFS 2024, from cold-and-dark setup through FMS programming, takeoff, approach and shutdown."
tags = ["MSFS 2024", "A350", "iniBuilds", "SimBrief"]
categories = ["MSFS", "Tutorial"]
slug = "inibuilds-airbus-a350-full-flight-tutorial"
+++

[← All Airbus A350 tutorials](/guides/a350/)

## Introduction

This is a follow-along tutorial for the **iniBuilds Airbus A350 in Microsoft Flight Simulator 2024**. Work through the procedure from cold and dark, or use the flight-phase navigator to jump to the stage you are currently flying.

The instructions are deliberately **flight-independent**: use the origin, destination, routing, fuel, weights, speeds and weather from *your own* operational flight plan (OFP). The screenshots and recording used to develop these procedures show one particular simulator flight, but its airport and performance numbers are not inputs for every flight.

The numbered actions distinguish **what to do** from **what to verify**. For actions not conclusively established in the recordings, follow the applicable in-sim aircraft checklist rather than treating an illustrative flow as authoritative.

{{< a350-print >}}

{{< a350-flight-nav >}}

## 1. Preparing the flight

Before opening the cockpit, generate a current SimBrief OFP for the correct aircraft variant. Have your departure, destination, alternate and current charts available. See [Connect SimBrief to the A350](/blog/connect-simbrief-inibuilds-a350/) if this is your first flight.

1. Select the **iniBuilds A350** in MSFS 2024 and load at a parking stand rather than a runway.
2. Review the SimBrief **origin**, **destination**, **alternate**, **route**, **planned runway and procedures**, **cruise altitude** and **cost index**.
3. Note the OFP **ZFW**, **block fuel**, estimated takeoff weight and **fuel reserves**.
4. Obtain current departure and arrival weather. Treat any runway or approach in the OFP as *planned*, not automatically cleared or guaranteed.
5. Keep the OFP visible on another screen or in the OIS for crosschecking.

| Flight detail | Enter or verify against |
|---|---|
| FROM / TO / ALTN | SimBrief OFP |
| Flight number / company route | SimBrief OFP |
| Cruise level / cost index | SimBrief OFP |
| ZFW / fuel | OFP and actual aircraft load |
| Runway / SID / STAR / approach | OFP, charts, weather and ATC |
| QNH / winds / temperature | Current weather, not a previous recording |
| V1 / VR / V2 / FLEX | **Current OIS takeoff computation**, not a generic table |

**Check:** You know which plan is current. If you regenerate the OFP, recheck all dependent data in the aircraft.

## 2. Cold and dark — establishing electrical power

{{< a350-overhead-image >}}

Start on the central **ELEC** overhead panel. Our cockpit screenshot shows **BAT 1**, **BAT EMER 1**, **BAT EMER 2**, **BAT 2**, and **EXT 1 / EXT 2** as distinct controls; there are not four main battery switches.

| Step | Control | Action / indication |
|---|---|---|
| 1 | Parking brake | Confirm aircraft secured |
| 2 | BAT 1 | ON |
| 3 | BAT EMER 1 | ON |
| 4 | BAT EMER 2 | ON |
| 5 | BAT 2 | ON |
| 6 | EXT 1 / EXT 2 | Connect available external power and confirm the associated electrical indications |
| 7 | ADIRS selectors 1–3 | NAV; allow alignment as applicable |

Select the battery switches using their **individual labels**. If ground power is not available, establish an appropriate electrical supply with the APU following the aircraft's start procedure.

**Check:** The aircraft is powered, the flight displays have initialised, and any ADIRS alignment is progressing or complete. A navigation-accuracy warning is not a normal confirmation of a completed setup.

## 3. Introducing the A350's cockpit interfaces

You will move between these interfaces repeatedly during flight preparation:

| Interface | Main purpose |
|---|---|
| **OIS** — Onboard Information System | Flight operations, ground services, SimBrief, loadsheet and performance |
| **MFD / FMS** | Initialization, route, runway/procedure selection, and flight-plan review |
| **KCCU** | Keyboard and cursor control of the relevant display |
| **FCU** | Autopilot/flight guidance targets: speed, heading, altitude and vertical mode |
| **PFD / FMA** | Flight instruments and confirmation of active/armed autoflight modes |
| **ECAM** | Aircraft system status and relevant aircraft messages |

1. Identify the OIS, both MFDs and their KCCUs.
2. Check which display is accepting cursor/keyboard input before typing a value.
3. Read the **FMA** after each change to the autoflight controls.

**Check:** Do not assume an instruction was accepted merely because a button was pressed; look for the resulting indication.

## 4. Connecting SimBrief and loading the aircraft

If SimBrief is not linked, complete the separate [SimBrief connection tutorial](/blog/connect-simbrief-inibuilds-a350/). To **generate** an OFP inside the cockpit rather than importing an existing one, see [Create a SimBrief plan in the OIS](/blog/inibuilds-a350-ois-simbrief-flight-planning/).

1. Open the OIS **FLT OPS MENU** and navigate to **FLT OPS STS**.
2. Select **SIMBRIEF IMPORT** for the current OFP and confirm the flight information appears.
3. Open the OIS **LOADSHEET** and compare the ZFW and fuel figures against the OFP.
4. Use the appropriate **SET ZFW** and **SET FUEL** controls to apply the loading figures to the simulator aircraft.
5. Verify the actual loaded weight/fuel before proceeding to takeoff-performance calculations.

An imported flight *document* is not necessarily an active route in the FMS, nor does it mean that fuel and payload have already been loaded.

**Check:** The flight information is correct on the OIS, and the aircraft load agrees with the intended plan.

## 5. Flight Management System setup

The recorded cockpit flow shows the FMS moving from an initial **P.POS / DISCONTINUITY / END OF F-PLN** state to an imported company flight with origin, destination, alternate, cruise level and cost index populated.

### Request the company flight plan

1. Open the MFD **ACTIVE / INIT** page.
2. Check the FMS is initialised and the appropriate aircraft/navigation data is available.
3. Use **CPNY F-PLN REQUEST** to request the current SimBrief company flight plan.
4. Wait for the request to complete; re-open **ACTIVE / INIT** and check **FROM**, **TO**, **ALTN**, **CPNY RTE**, flight number, **CRZ FL** and **CI** against your OFP.
5. Open **ACTIVE / F-PLN** and verify the route is populated. An initial empty plan or temporary page does not prove the company route has loaded.

### Select the departure

1. Open **DEPARTURE** from the applicable FMS flight-plan page.
2. Select the **departure runway** assigned or planned for your flight.
3. Select the **SID** that matches the chart and your route; select a **transition** if applicable.
4. Inspect the displayed **TMPY** (temporary) modification and the resulting first legs.
5. Confirm the route matches the intended runway and SID, then select **INSERT TMPY** to accept it.
6. Return to the flight plan to check the inserted departure legs are now active.

### Select the arrival

1. On the flight plan, open the **ARRIVAL** page for the destination airport.
2. Select the intended **runway** and **approach** (for example, an ILS when appropriate).
3. Select the published **STAR**, **VIA** and **TRANS** that apply; **NONE** is valid when no such selection is required.
4. Review the **TMPY** route, approach/course/frequency data and relevant constraints.
5. Select **INSERT TMPY** only after the proposed arrival is correct.

In the recordings, the arrival remained **TMPY** during part of the selection sequence. Do not describe the arrival as active until an insertion is visibly confirmed.

### Review the route and discontinuities

1. Follow the route from departure to destination using the MFD route list and the navigation display's PLAN view where available.
2. Compare waypoints, airways, procedure transitions, lateral track and altitude/speed constraints with the OFP and charts.
3. **Investigate any DISCONTINUITY**. Some are intentional and should not be deleted automatically.
4. Confirm the final route contains no unexplained gaps or wrong runways.
5. If wind import is requested, confirm whether the result is actually received; a pending request is not a successful uplink.

**Check:** The active route and both procedures match your flight. A recorded flight's runway/SID/STAR selections are examples, not defaults.

## 6. Takeoff performance

The OIS **T.O PERF** page is visible in the recorded setup. It includes runway conditions and controls such as **SYNC**, **SYNC FMS** and **SYNC SIMBRIEF**; not every recorded page shows a completed calculation.

1. Open **T.O PERF** on the OIS.
2. Import/synchronise the relevant runway, weather and weight information using the controls appropriate to your aircraft version.
3. Verify **runway**, **available length**, **runway condition**, **wind**, **QNH**, **temperature**, **takeoff weight**, **flap configuration** and **anti-ice**.
4. Perform the takeoff calculation in the OIS.
5. Review the calculated **V1**, **VR**, **V2**, thrust/FLEX setting and any required configuration data.
6. Transfer the computed performance to the FMS where supported by the OIS.
7. Check the FMS takeoff page to confirm the intended data were received.

**Check:** Use only numbers computed for the *current* aircraft load, runway and conditions. Recalculate if any of these inputs change.

### Preparing the FCU

1. Set the departure QNH.
2. Set the cleared or published initial altitude as applicable.
3. Check the flight directors and required guidance configuration.
4. Confirm the selected and armed modes on the **FMA**.

## 7. Overhead and cockpit preparation

Continue with the remaining overhead and cockpit preparation using the applicable in-sim checklist. The provided recordings cover parts of this sequence but do **not** independently establish the exact chronological state of every overhead switch.

| Area | Verify |
|---|---|
| ADIRS / navigation | Correct selector positions and alignment status |
| Electrical system | Appropriate generator/APU/ground supply |
| Flight controls | Correct indications and expected responses |
| Fuel / pneumatic / air | Configuration appropriate for aircraft and conditions |
| Lighting and signs | Appropriate for current phase |
| Flight displays | No unexplained warnings |
| FMS and FCU | Route, departure, takeoff data and initial guidance agreed |

**Check:** Complete the aircraft's appropriate before-start checklist before pushback.

## 8. Before start and pushback

1. Review the OIS ground-services page; close doors and remove ground equipment when ready.
2. Confirm the aircraft has a suitable electrical and pneumatic supply for engine start.
3. Complete the before-start checks, including the beacon and applicable surveillance settings.
4. Obtain pushback/engine-start clearance where ATC services are being used.
5. Begin pushback and monitor aircraft/tug status.

### Starting the engines

Follow the aircraft engine-start checklist. Select the appropriate engine-start configuration, move each engine master to ON in the prescribed sequence, and monitor each engine's indications until a normal start is confirmed.

Do not infer an engine start has completed just because a switch moved; check the resulting indications and relevant messages.

### After-start flow

Confirm engine start completion, select the required post-start pneumatic and electrical configuration, check ECAM, set the takeoff flap configuration, arm the ground spoilers as appropriate, and complete the after-start checklist.

## 9. Taxi and before takeoff

1. Verify pushback equipment has disconnected and the aircraft is clear to taxi.
2. Perform the flight-control check using the indicated system displays.
3. Confirm the departure runway, SID, initial altitude and the FCU/FMA guidance.
4. Set the intended takeoff flaps and rejected-takeoff braking configuration.
5. Run **T.O CONFIG** and review the takeoff memo.
6. Taxi at a controlled speed; use an airport map/ANF display if available and useful.
7. At the holding point, brief the runway, initial departure path, thrust, V-speeds and any restrictions.
8. Complete the before-takeoff checklist before runway entry.

## 10. Takeoff and initial climb

1. Confirm the runway and takeoff clearance as applicable.
2. Apply the **calculated** thrust setting for the flight, using the appropriate FLEX or TOGA selection.
3. Verify the engine and FMA indications during the takeoff roll.
4. Rotate at the calculated **VR** and establish a positive climb.
5. Retract the landing gear when positive climb is confirmed.
6. Follow the flight directors; engage the autopilot when appropriate.
7. Observe the programmed thrust-reduction and acceleration phases, and retract flaps according to aircraft indications/checklist.

**Check:** The FMA confirms the modes actually engaged, not merely those requested.

## 11. Climb and cruise

1. Follow the assigned departure/climb constraints and monitor speed, altitude and lateral tracking.
2. Set any changed altitude/heading/speed clearances and verify the FMA.
3. Compare predicted fuel and estimated arrival time with the OFP.
4. Review destination weather, arrival runway and approach while workload is low.
5. Monitor progress towards top of descent, particularly on a short sector.

## 12. Preparing the arrival

1. Obtain the destination weather and available ATC/approach information.
2. Reassess the intended runway, STAR, approach and transition.
3. Review or amend the FMS arrival **using TMPY and INSERT TMPY**, as described in Section 5.
4. Check for discontinuities and constraints.
5. Open **LDG PERF** on the OIS and verify the landing runway, condition, wind and landing weight.
6. Calculate the intended landing performance; brief the approach and missed approach.

## 13. Descent and approach

1. Set and verify cleared altitudes on the FCU.
2. Monitor managed/selected descent modes using the FMA.
3. Check speed, distance, vertical path and published crossing restrictions.
4. Verify the selected arrival and approach are correctly represented in the FMS.
5. Set the appropriate local altimeter reference when required.
6. Configure progressively for the approach, selecting landing gear/flaps according to the applicable checklist and speed limits.
7. Confirm stable flight-path, speed, landing configuration and guidance before continuing.
8. If the approach is unstable or guidance is not as expected, execute the appropriate go-around.

## 14. Landing, taxi-in and shutdown

1. Maintain the intended landing path and speed through the final approach.
2. After touchdown, monitor deceleration; use the aircraft's appropriate spoiler, reverse-thrust and braking procedures.
3. Vacate the runway and complete the after-landing checklist.
4. Taxi to the stand and secure the aircraft with parking brake or chocks as appropriate.
5. Confirm a suitable ground/APU electrical supply before engine shutdown if the cockpit needs to remain powered.
6. Shut down engines, configure ground services, and follow the aircraft securing checklist.

## 15. Common problems

### SimBrief import doesn't appear

Verify the numeric SimBrief ID, that an OFP exists in the account and the intended plan is current. Retry the OIS import and then the separate FMS company-route request.

### The FMS still shows a discontinuity

Check whether the route is correctly loaded and whether the gap is part of a procedure. **Do not automatically remove all discontinuities.**

### The arrival remains yellow / TMPY

The proposed changes have not yet become the active route. Verify the proposal and use **INSERT TMPY** when appropriate.

### Takeoff speeds are missing or unexpected

Check the loadsheet, runway, current conditions and OIS computation. Transfer the data to the FMS and verify receipt.

### The aircraft doesn't follow the intended guidance

Read the **FMA** and inspect the route. Determine which guidance mode is actually active.

### A flight-plan wind request is pending

A request does not establish receipt. Check for an explicit successful result or available data before treating the wind uplink as completed.

## Quick-reference flow

| Phase | Confirm before proceeding |
|---|---|
| Flight preparation | Current OFP and correct aircraft |
| Electrical power | Batteries, external/APU supply, ADIRS |
| OIS | SimBrief data and aircraft loadsheet |
| FMS | Company route, departure, arrival, active route |
| Takeoff performance | Computed and transferred flight-specific data |
| Before start | Ground services, checks, start supply |
| Engine start | Both starts complete, ECAM checked |
| Taxi | Flight controls, flaps, T.O CONFIG |
| Takeoff | Calculated thrust, V-speeds, FMA |
| Climb/cruise | Constraints, flight progress, fuel |
| Arrival/descent | Current procedure, performance, clearance |
| Landing/shutdown | Landing, after-landing and securing checks |

## Further reading

- [Connect SimBrief to the iniBuilds A350](/blog/connect-simbrief-inibuilds-a350/)
- [Create a SimBrief plan in the OIS](/blog/inibuilds-a350-ois-simbrief-flight-planning/)
- [iniBuilds A350 aircraft manual](https://forum.inibuilds.com/topic/25085-a350-aircraft-manual/)
- [A350 guide collection](/guides/a350/)

*Editorial basis: chronological review of the supplied cockpit recordings (Parts 1–3, 4 November 2026) and the existing site material. The recorded flight used a specific route; all values have been generalised for reuse. Some switch sequences beyond those clearly observable still require validation against the current simulator aircraft checklist.*

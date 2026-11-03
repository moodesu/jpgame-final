+++
authors = ["JPGame"]
title = "iniBuilds Airbus A350 Full Flight Tutorial — MSFS 2024"
date = 2026-11-03
draft = false
description = "A step-by-step iniBuilds A350 tutorial in MSFS 2024: cold and dark at Hakodate, SimBrief and flight management setup, takeoff, descent, ILS approach and shutdown at Tokyo Haneda."
tags = ["MSFS 2024", "A350", "iniBuilds", "SimBrief"]
categories = ["MSFS", "Tutorial"]
slug = "inibuilds-airbus-a350-full-flight-tutorial"
+++

[← All Airbus A350 tutorials](/guides/a350/)

## Introduction

Welcome to my full-flight tutorial for the **iniBuilds Airbus A350 in Microsoft Flight Simulator 2024**. As with my [Horizon Boeing 787 tutorial](/blog/msfs2020-boeing-787-horizon-full-flight-tutorial/), we'll begin with an unpowered aircraft, plan the flight, work through the cockpit procedures, and finish by shutting the aircraft down at our destination.

For this example I'm flying from **Hakodate (RJCH)** in Hokkaido to **Tokyo Haneda (RJTT)**. It's a short flight for an A350, but ideal for learning the workflow because we can practise every major phase without spending hours in cruise.

> **Before you start:** Generate a fresh SimBrief operational flight plan (OFP) for RJCH–RJTT and select the correct A350 variant. Our runway, SID, STAR, transition, fuel, cruising altitude and V-speeds must come from **that flight's** plan and current weather; do not copy values from an unrelated flight.

## 1. Preparing the flight

Create a flight in SimBrief with RJCH as the origin and RJTT as the destination. Choose the A350-900 or A350-1000 aircraft profile to match the aircraft you've loaded.

Take a moment to note:

| Flight-plan item | Where we'll use it |
|---|---|
| Departure runway and SID | Flight plan and takeoff briefing |
| Route and cruising altitude | Flight Management System (FMS) |
| Arrival, STAR and approach | Descent and approach preparation |
| Zero fuel weight (ZFW) and block fuel | OIS loadsheet and FMS |
| Cost index and reserve fuel | FMS flight initialization |
| Departure and destination weather | Takeoff and landing performance |

You can use live weather, but it is simpler to learn the flow in clear conditions. Airport runways and procedures change with wind and navigation-data cycles. **The old Horizon guide's runway 12 / runway 22 example is not a fixed route for this flight.** Check the current charts and SimBrief plan before choosing anything.

In MSFS, select the A350 and start at a **parking stand**, rather than on the runway, so we can begin cold and dark.

## 2. Cold and dark — establishing electrical power

From the captain's seat, look up at the overhead. We'll initially power the aircraft from ground power while the engines are off.

| Control | Action |
|---|---|
| Batteries 1–4 | ON |
| External power 1 and 2 | Select when available |
| ADIRS selectors 1–3 | NAV |
| Parking brake | SET / confirm |
| Engine master switches | OFF |
| Engine start selector | NORM |

The four batteries provide initial electrical power. External power supplies the aircraft's main electrical system without running an engine. The **ADIRS** (Air Data Inertial Reference System) provides attitude, position and other information needed by the displays and navigation systems. Set all three to NAV and allow initialization to complete.

If external power isn't available, use the OIS ground-services page to request it or follow the APU-powered setup in the in-sim checklist.

**Check:** The cockpit displays are powered, and the aircraft is stationary with its engines off. Do not rush ahead simply because the screens have illuminated.

## 3. Introducing the A350's cockpit interfaces

Coming from the 787, one of the biggest differences is how the A350 distributes its controls. Before entering a route, it's useful to identify four interfaces:

- **OIS — Onboard Information System.** The outboard tablet-style display for flight operations, SimBrief import, loading, charts, ground services, and takeoff/landing calculations.
- **MFD — Multi-Function Display.** Used for flight-plan pages and management functions that you'd associate with an FMC/CDU on other aircraft.
- **KCCU — Keyboard and Cursor Control Unit.** An input method for interacting with the A350's MFD pages.
- **FCU — Flight Control Unit.** The glareshield controls for selected altitude, speed, heading and vertical guidance.

You'll use the OIS to import information and calculate performance, the MFD to review the route and flight-management data, and the FCU to tell the autopilot what you want it to do.

## 4. Connecting SimBrief and loading the aircraft

**Want to create the flight plan directly from the cockpit?** See my separate guide: [How to create a SimBrief flight plan in the A350 OIS](/blog/inibuilds-a350-ois-simbrief-flight-planning/). It covers connecting your accounts, the FLT OPS PLAN form, generating an OFP, and requesting the route on the FMS. The steps below cover importing an already-generated plan.

On the OIS, go to **OPTIONS → 3RD PARTY** and enter your **SimBrief User ID**. If you use Navigraph, you can also link that account for charts.

Next, open **FLT OPS MENU → FLT OPS STS** and select **SIMBRIEF IMPORT**. Confirm that the imported flight has the correct origin, destination and aircraft details.

Open **LOADSHEET**. Review the imported payload and fuel figures, then use **SET ZFW** and **SET FUEL** to load the intended values into the aircraft. Loading the SimBrief route doesn't necessarily mean the actual aircraft weight and fuel have been set: these are separate steps.

If you use Navigraph, open **TERML CHART** and bookmark the departure, arrival and approach charts you'll need. A departure chart is particularly useful when we check the altitude and speed restrictions programmed into the FMS.

**Check:** The OIS loadsheet matches your intended flight. If you change fuel or payload after calculating takeoff performance, you'll need to recalculate it.

## 5. Flight Management System setup

Check the **DATA / STATUS** page on the MFD and confirm that the navigation database is current for your intended flight. Use the **INIT** function with the KCCU to access the flight-management pages.

Review **ACTIVE / INIT** and the imported flight plan. Confirm the origin and destination. On the IRS page, check that all three inertial reference systems are in NAV.

### Select the departure

From **ACTIVE / INIT**, open **DEPARTURE** and choose the runway, SID and transition shown on your current route and charts. The A350 shows temporary flight-plan modifications before you commit them. Review the choices and **insert the temporary flight plan** only when you're satisfied.

### Inspect the route

Switch the navigation display to **PLAN** mode and use the MFD's flight-plan pages to follow the legs in sequence. Check:

1. The first waypoint after departure matches the SID.
2. The route contains the waypoints and airways you expect.
3. Altitude and speed constraints match the published procedure.
4. There are no unexpected gaps, large turns or discontinuities.

An FMS discontinuity is not automatically an error: some are intentional, depending on the procedure. **Don't delete a discontinuity blindly.** Establish why it's there before modifying the route.

Later, during cruise, we'll check the arrival and approach again using up-to-date weather.

## 6. Takeoff performance

The A350's OIS does much of the takeoff calculation for us. Open **T.O PERF**.

| OIS action | What it does |
|---|---|
| SYNC FMGS | Uses the departure airport and runway from the FMS |
| SYNC | Imports available current weather and weight information |
| Runway condition | Select manually: do not assume SYNC detects wet/dry correctly |
| COMPUTE | Calculates takeoff performance |
| SEND TO FMGS | Transfers calculated takeoff information to the FMS |

Check the actual runway length and any intersection departure, runway surface, wind, temperature, air-pressure settings, aircraft weight, configuration and anti-ice requirements before computing. Then check the calculated speeds and thrust settings.

Return to the MFD and verify the **takeoff performance page** shows the expected information. Takeoff speeds **V1, VR and V2 are flight-specific**. No example figures are supplied here because entering arbitrary speeds would make this tutorial misleading.

### Preparing the FCU

Set the correct departure **QNH**, then set the initial cleared or published altitude on the FCU. Confirm both flight directors are on.

The Airbus uses **managed** and **selected** guidance. With managed speed or lateral guidance, the aircraft follows the FMS profile. When you select a specific target on the FCU, you're asking it to follow that value instead. As a rule of thumb, **push for managed, pull for selected** where the relevant Airbus FCU knob supports that distinction.

On the primary flight display (PFD), confirm the takeoff speeds and expected armed flight modes. The **Flight Mode Annunciator (FMA)** at the top of the PFD is the authoritative indication of what the autoflight system is actually doing.

## 7. Overhead and cockpit preparation

Now we'll complete a cockpit flow, using the overhead from the lower section upward and moving left to right. The following highlights are not a replacement for the full in-sim checklist.

| Area | Check |
|---|---|
| Crew oxygen | ON |
| ADIRS | All three NAV |
| External lighting | Appropriate for stand operations |
| APU | Start with MASTER SW, then START |
| Passenger signs | Configure for boarding/departure |
| APU bleed | ON when APU is available |
| Fuel pumps | ON as required |
| Anti-skid / nosewheel steering | ON |
| Spoilers | Retracted before the later arming step |
| Parking brake | SET |
| Engine masters | OFF |
| Flap lever | Matches actual flap indication |

**Why start the APU?** It provides an onboard source of electrical power and pneumatic air so that we can disconnect ground services and start the engines. Wait for the appropriate APU available indication before depending on it.

Finish by crosschecking the PFD and navigation display: correct QNH, departure runway and SID, initial waypoint, programmed speeds and selected initial altitude.

## 8. Before start and pushback

Make sure the flight plan and takeoff performance are complete before beginning pushback.

1. On the OIS **GROUND** page, close all doors and remove ground equipment when ready.
2. Verify door indications on the systems display.
3. Confirm the APU is available and **APU BLEED** is on.
4. Switch the beacon on before engine start.
5. Configure surveillance/transponder settings on the **SURV** page.
6. Obtain pushback/start clearance if using ATC, then begin pushback.

### Starting the engines

Set the **ENG START** selector to **IGN/START**, then switch an **ENG MASTER** to ON. The aircraft's FADEC manages the starting process. Watch the engine indications as the start develops rather than immediately selecting the other engine.

The manual describes a temporary **AVAIL** indication when a successful start is complete. Repeat the procedure for the other engine.

If a start is abnormal, don't improvise by repeatedly switching controls. Stop the sequence and use the aircraft's applicable abnormal procedure.

### After-start flow

| Control | Action |
|---|---|
| ENG START | NORM |
| APU BLEED | OFF |
| APU MASTER | OFF when no longer needed |
| Ground spoilers | ARM |
| Rudder trim | RESET |
| Flaps | Set calculated takeoff configuration |
| Anti-ice | As required |
| Systems / ECAM indications | Check |

Make sure the tug has disconnected and you have clearance to taxi before moving.

## 9. Taxi and before takeoff

Before we taxi, check the flight controls. Make smooth full-range movements and confirm the expected control-surface response on the aircraft's systems display. The A350 can bring up the flight-control indications automatically in response to the stick movement.

Arm the appropriate rejected-takeoff autobrake mode and press **T.O CONFIG** to check the takeoff configuration. Review the takeoff memo for outstanding indications.

One particularly useful A350 feature is the **Airport Navigation Function (ANF)**. With the navigation display in an appropriate mode, rotating the ND range into **ZOOM** brings up the airport map, where available. This can make taxiing much easier at an unfamiliar airport.

Release the parking brake and use minimum practical thrust. Keep the speed controlled, especially when turning. At the holding point, stop and review the takeoff briefing: runway, departure path, initial altitude, V-speeds, flap configuration and any expected restrictions.

Before entering the runway, complete the before-takeoff checklist and set exterior lights for departure. Move the ND out of airport-map zoom once lined up so you can see the departure route.

## 10. Takeoff and initial climb

The A350 has two typical takeoff thrust choices:

- **FLEX** applies reduced takeoff thrust when the performance calculation permits it and the correct FLEX temperature is entered.
- **TOGA** commands full available takeoff thrust.

Use the result of your takeoff calculation. Don't choose a FLEX temperature by guesswork.

On the runway, align carefully with the centreline. Apply the calculated takeoff thrust and confirm the expected FMA indications. Maintain directional control through the takeoff roll.

At **VR**, rotate smoothly and establish a positive climb. Retract the landing gear when safely airborne and climbing. Follow the flight director indications and engage the autopilot when ready.

As the aircraft climbs, monitor the FMA and PFD for the change into climb and navigation modes. Retract the flaps progressively according to the displayed speed indications and the aircraft checklist. Reduce thrust from takeoff power when prompted by the programmed thrust-reduction point and the applicable procedure.

**The important habit:** after every change to the FCU or thrust levers, look at the FMA. The aircraft's actual guidance mode matters more than the mode you thought you selected.

## 11. Climb and cruise

The workload drops once the autopilot is engaged and the aircraft is following its programmed lateral and vertical path. That doesn't mean we can stop monitoring it.

Check that the aircraft is complying with the departure altitude and speed restrictions. If ATC gives a new altitude or heading, select it as appropriate and verify the FMA. When cleared, continue the climb to the cruising level from the SimBrief OFP.

During cruise, review your progress against the flight plan:

- Fuel remaining compared with the plan.
- Distance and estimated time to destination.
- Destination weather and possible landing runway.
- Arrival STAR, transition and approach chart.
- Suitable descent planning and approach configuration.

Because Hakodate–Haneda is a comparatively short flight, we'll begin planning the descent early.

## 12. Preparing the arrival

Obtain the latest Haneda weather and check the appropriate arrival and approach charts. Choose the runway, STAR and approach that match the conditions and any ATC clearance.

Use the MFD flight-plan pages to enter or revise the arrival. Inspect the route in PLAN mode again, including its constraints and any discontinuities. Do not assume the arrival automatically selected by a planning service is the runway you'll actually use.

Next, use **OIS → LDG PERF** to calculate landing performance. Check runway condition **manually**; as with takeoff performance, this isn't reliably inferred by the SYNC function.

Review the landing weight and resulting landing data. Set or confirm the appropriate approach information in the FMS and brief the missed-approach procedure before beginning the final descent.

## 13. Descent and approach

Use the FMS's descent profile as a guide, but monitor your actual distance, speed and altitude against the arrival constraints.

Set the altitude cleared by ATC or appropriate for the procedure. Use managed descent when applicable and verify the descent mode on the FMA. Selected vertical modes may be useful when you need to comply with particular clearances, but always crosscheck the aircraft's path against the procedure.

As you approach Haneda:

1. Confirm the assigned approach and runway.
2. Set the correct local altimeter reference at the appropriate transition level.
3. Verify the ILS or other approach guidance and its correct identification when applicable.
4. Configure the aircraft progressively for the approach, respecting speed limits.
5. Arm or capture the approach guidance as appropriate, watching the FMA.
6. Extend the landing gear and set the final landing configuration in accordance with the checklist.

An ILS approach is not necessarily an autoland. For a manually flown landing, disconnect the autopilot at a sensible point, maintain the flight-director guidance as appropriate, and make sure the aircraft is stabilized before continuing below the required point.

If you're unstable, or the approach guidance is not behaving as expected, **go around**. Practising that decision is part of learning the aircraft.

## 14. Landing, taxi-in and shutdown

On final, monitor the runway alignment, approach speed, descent path and FMA. Retard the thrust levers at the appropriate landing cue. After touchdown, monitor deceleration and use the approved combination of spoilers, reverse thrust and braking for your configuration and runway.

Once clear of the runway, complete the after-landing flow: retract spoilers and flaps as appropriate, reset lights, and begin the taxi-in checklist.

At the parking stand:

| Item | Action |
|---|---|
| Parking brake | SET, or chocks as appropriate |
| APU | Start if needed for power |
| Electrical supply | Confirm APU or ground power available |
| Engine masters | OFF |
| Beacon | OFF once engines have stopped |
| Seat-belt signs | OFF when appropriate |
| Ground services | Connect through OIS as required |
| ADIRS and electrical power | Shut down according to securing checklist |

Take your time during shutdown: make sure you have a valid electrical source before switching off the engines if you still need the cockpit displays. Use the full securing checklist to turn the aircraft completely cold and dark.

## 15. Common problems

### SimBrief import doesn't appear

Check the SimBrief User ID in **OPTIONS → 3RD PARTY**, confirm you generated an OFP, and retry the import. Check that origin, destination and aircraft type agree with your intended flight.

### The aircraft doesn't follow the route

Look at the FMA first. Check whether **NAV** is active or armed, inspect the flight plan for discontinuities, and confirm that you haven't unintentionally selected a heading mode.

### Takeoff speeds are missing

Revisit the OIS loadsheet, T.O PERF calculation, **SEND TO FMGS**, and the FMS takeoff performance page. Check whether the aircraft's weight or departure runway changed after the calculation.

### The descent starts too late

Review the descent profile well before top of descent. A short domestic flight leaves little time to recover if you've remained too high and fast. Use the appropriate Airbus descent guidance rather than simply increasing the descent rate without considering the flight path.

### Something looks wrong on the autoflight display

Read the **FMA**, not just the FCU. The FMA tells you which vertical, lateral and thrust guidance modes are active and armed.

## Quick-reference flow

| Phase | Main objective |
|---|---|
| Power-up | Batteries, ground power, ADIRS |
| OIS | SimBrief, fuel, payload and charts |
| MFD | Flight plan, SID and route check |
| Performance | T.O PERF, transfer data, FCU |
| Before start | APU, doors, beacon, pushback |
| Engine start | IGN/START, monitor both engines |
| Taxi | Flight controls, autobrake, T.O CONFIG |
| Takeoff | FLEX/TOGA, rotation, positive climb |
| Cruise | Monitor FMA, route, fuel and arrival |
| Descent | STAR, approach, landing calculations |
| Landing | Stable approach, deceleration, runway exit |
| Shutdown | Parking, ground power/APU, secure |

## Further reading

- [iniBuilds A350 Airliner official aircraft manual](https://forum.inibuilds.com/topic/25085-a350-aircraft-manual/) — the primary reference for the procedures in this guide.
- [A380 video framework](https://www.youtube.com/watch?v=MsrFyhGewLE&list=PL-4y7fmOeA-WnosVNL7rlVujBef29w8EV&index=2) — for teaching structure only, not A350 procedures.
- [Horizon Boeing 787 full-flight tutorial](/blog/msfs2020-boeing-787-horizon-full-flight-tutorial/) — our earlier tutorial using the same Hakodate–Haneda route.

*Editorial note: This is the first written draft. Before publication, add our own cockpit screenshots (OIS, MFD, overhead, FCU, takeoff performance, arrival and landing), verify all cockpit flows against the installed aircraft version, and test the RJCH–RJTT flight end to end.*

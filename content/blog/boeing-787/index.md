+++
authors = [ "JPGame" ]
title = "MSFS2020 Boeing 787 Horizon Full Flight Tutorial"
date = ""
feature = ""
featureCaption = ""
tags = [ "MSFS2020", "787" ]
categories = [ "MSFS", "787", "Tutorial" ]
series = ""
slug = "msfs2020-boeing-787-horizon-full-flight-tutorial"
+++

## Introduction
Welcome to my MSFS Boeing 787 Full Flight Tutorial, I am using the
Horizon mod for this so if you are using the default 787 or other mod,
some items may be a little different but you should still be able to
follow along.

We are going to begin cold and dark at Hakodate Airport in Hokkaido,
Japan. I will go through the start up procedures and show how to enter
and check a flight plan, set the performance for the flight and show
you my flows and checklists.

This guide assumes you have a SimBrief account and have also linked
your SimBrief id with the aircraft. If you haven't done that then
follow the instructions on this page before continuing.

After take off we will fly to Tokyo Haneda Airport. During the cruise
I will show you how I prepare for descent and approach. After Landing
we will go through shut down and securing the aircraft.

## Power on From Cold And Dark
Go to the overhead panel, started at the left hand side of the panel,
perform the following flow to perform power up.
| Electrical Power Up           |           |
|-------------------------------|-----------|
| Battery Switch                | On        |
| C1 and C2 ELEC pump Selectors | Off       |
| DEMAND Pump Selectors         | Off       |
| WIPER Selectors               | Off       |
| Landing Gear Lever            | Down      |
| Electrical Power              | Establish |

Establish the Electrical Power by using the APU or, if available,
external power.

### Using External Power
| via EXT PWR |  |
|---|---|
| EXT PWR AVAIL lights | Illuminated |
| EXT PWR switches | Push |

### Using APU
|  via APU   |
|---|---|---|
| APU Generator switches | On |
| APU Selector | Start, then ON |

## Pre Flight Procedures
Now we have power to the aircraft let’s begin the pre flight procedures

| Pre Flight
|---|---|
| IRS Selectors | Off 30 seconds then On |
| Status Display | Check (No abnormal messages) |

## CDU/EFB Pre Flight Procedures
The CDU will default to the IDENT page. Press RTE to open the RTE 1 page.

Pressing the REQUEST button will fetch the latest SimBrief flight plan. 
Once the plan is available press LOAD and our initial flight plan will automatically be loaded.
We still need to insert our departure runway and procedures. 

Press DEP ARR and choose the departure runway and SID according to your flight plan.
![SimBrief Routing ](hkdhndroute.png#center)

As we can see from the image, our departure is from runway 12 via the TSUGA2 SID. Press the buttons next to the to select and your departure should be ready and look like this image
![RJCH Departures](dep1.png#center)

Press the DEP ARR button to go back to the DEP/ARR Index page, this time press the ARR button on the right.

Our arrival runway is 22 so select it and the available STARs will be filtered for that runway, pretty neat.

According to SimBrief we are using the MESSEN STAR so press NEXT PAGE until MESSEN is available and press the button next to it to select. The arrival should look like this:
![RJTT Arrivals](arr1.png#center)
The route is loaded but we still need to finalize it by pressing EXEC.

## Add Fuel
Look at the flight plan from SimBrief, the Summary and Fuel page will list our block fuel. Add or remove fuel - using the Weights and Balance widget in MSFS - to match this number, I usually take a little extra.

I also remove all fuel from the centre tank unless it’s a long haul flight. This saves me from switching on the centre fuel pumps.
![SimBrief Fuel](fuel.png#center)

## Performance
With the fuel on board, we can input our flight performance values.

Press INIT REF to go to the PERF INIT page on the CDU. Press the button next to ZFW to show the number on the scratchpad then press again to input the value.

Get the RESERVES value from SimBrief and enter it by using the numpad next to the CDU. The reserve fuel is listed on the SimBrief plan as FINRES.

COST INDEX is entered the same way and is listed as CI.

![SimBrief Fuel and CI](reserveci.png#center)

The next part of the performance calculations are performed on the EFB.

Press PERFORMANCE and the take off screen should be displayed. First we copy the data from the FMC to automatically populate some of the fields. Do this by pressing COPY FMC DATA.

We now fill in the following sections to allow the EFB to calculate the take off data.

| EFB Data |  |  |
|---|---|---|
| Runway Condition |  | As Required |
| Wind |  | From METAR |
| OAT (Outside Air Temperature) |  | From METAR |
| Thrust RTG (Rating) |  | OPTIMUM |
| Flap Config |  | OPTIMUM |
| AI (Anti Ice) |  | As needed |

A/I is the Anti Ice setting and since Ice is possible on my flight today I will set it to ENGINE. IF you don’t need it then set it to off.

With everything set, press CALC to finalize the takeoff setting then press SEND OUTPUT to transfer the data to the CDU.

### Back to the CDU

Press INIT REF >> INDEX >> TAKEOFF to go to the TAKEOFF REF UPLINK page.

Here we can press ACCEPT to finalize the Vref data. 

Double press the CG button to complete the FMC Preflight.
![Takeoff Ref](vref.png#center)

Press LEGS on CDU then switch to PLAN mode on the MFD. Check the flight plane by pressing STEP. This will go through each leg individually. If there are any discontinuities then delete then by pressing the DEL key then pressing the button next to the discontinuity.

## Overhead Panel Flow
Beginning at the top left of the panel and working our way down the across:
| Left Panel              |                 |
|--------------------------|-----------------|
| Flight Control Surfaces  | Set and guarded |
| Heading Ref Switch       | NORM            |
| PRIMARY FLIGHT COMPUTERS | Guard Closed    |
| BATTERY                  | ON              |
| IFE PASS SEATS           | ON              |
| CABIN UTILITY            | ON              |
| APU GEN                  | ON              |
| GEN CTRL                 | ON              |
| DRIVE DISC               | ON              |

[test link](/microsoft-flight-sim-2020-garmin-g1000-track-up-north-up)
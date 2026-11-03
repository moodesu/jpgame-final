+++
authors = ["JPGame"]
title = "Create a SimBrief Flight Plan in the iniBuilds A350 OIS"
date = 2026-11-03
description = "How to generate and load a SimBrief flight plan directly from the iniBuilds Airbus A350 Onboard Information System in Microsoft Flight Simulator 2024."
tags = ["MSFS 2024", "A350", "SimBrief", "iniBuilds"]
categories = ["MSFS", "Tutorial"]
slug = "inibuilds-a350-ois-simbrief-flight-planning"
+++

[← All Airbus A350 tutorials](/guides/a350/)

## Introduction

One of the useful features of the iniBuilds Airbus A350 in **Microsoft Flight Simulator 2024** is the ability to **generate a new SimBrief flight plan from inside the cockpit**. Rather than switch to a browser, you can enter your departure and arrival airports on the aircraft's **Onboard Information System (OIS)** and have SimBrief build the plan.

In this tutorial, I'll use **Hong Kong (VHHH) to Taiwan Taoyuan (RCTP)**, the route used in my [A350 full-flight tutorial](/blog/inibuilds-airbus-a350-full-flight-tutorial/). We'll link SimBrief, generate an operational flight plan (OFP), and then make the plan available to the aircraft's other systems.

> **Aircraft version:** These instructions describe the iniBuilds A350 OIS planner introduced in April 2025. Menu names and behaviour can change in later aircraft releases. This is for flight simulation, not real-world operations.

## 1. Power the aircraft and open the OIS

Begin at a parking stand with the A350 powered by ground electrical power or the APU. Open the OIS and select **FLT OPS MENU**. You should be able to access the planning functions from here.

> **First time using SimBrief with this aircraft?** Follow our [A350 SimBrief connection guide](/blog/connect-simbrief-inibuilds-a350/) before continuing.

## 2. Link your Navigraph and SimBrief accounts

Before creating a plan, we need to connect the OIS to SimBrief and Navigraph.

1. Open **FLT OPS MENU → OPTIONS → 3RD PARTY**.
2. Enter your **SimBrief User ID**. This is the numeric account ID, **not your username**.
3. To authenticate Navigraph, scan the QR code displayed on the OIS, or visit [navigraph.com/code](https://navigraph.com/code) and enter the code shown.
4. Finish authorization in the browser and return to the OIS.

When authorization is complete, you should see the additional **UPDATE DATA** and **RESET NAVIGRAPH** options. This is a useful confirmation that your account connection has been established.

## 3. Open FLT OPS PLAN

From **FLT OPS MENU**, open **FLT OPS PLAN**, the A350's built-in SimBrief planner.

You don't need to fill out every field to get a usable flight plan. In fact, **only FROM and TO are mandatory**:

| OIS field | Our example |
|---|---|
| FROM | VHHH — Hong Kong International |
| TO | RCTP — Taiwan Taoyuan International |

Leaving the remaining options at **AUTO** tells SimBrief to make those planning decisions. Press **GENERATE PLAN** when you're ready.

For our published example OFP, the filed route is **DALOL1Y DALOL V631 ENVAR M750 TONGA TONGA1A**, planned at **FL390**, with cost index **15** and **16,243 kg** of block fuel. These are outputs to compare with your newly generated OFP, not values to copy blindly. For the first attempt, I recommend leaving the optional fields on AUTO. After you've seen the result, come back and experiment with different runways, weights and fuel settings.

## 4. Optional flight-planning settings

If you want more control over the flight, the planner offers additional settings.

| Field | Description |
|---|---|
| ALTN | Alternate airport, or AUTO |
| AIRLINE | Three-letter ICAO airline code |
| FLT NUM | Flight number |
| FROM RWY / TO RWY | Preferred departure and arrival runways |
| PAX | Passenger count, capped at the aircraft's maximum |
| FREIGHT | Cargo weight, capped at the aircraft's maximum |
| CRZ FL | Three-digit flight level, e.g. 380 for FL380 |
| REG | Aircraft registration; normally filled from aircraft configuration |
| CPT NAME / FO NAME | Names printed on the operational flight plan |
| PLAN | OFP format; LIDO is the default |
| FUELING | Specify fuel sections by weight or time, or leave AUTO |

Use the **CLEAR** control if you want to return the form to its defaults. The planning weight units, **KG** or **LBS**, follow the aircraft-weight setting in the OIS settings page.

For our short VHHH–RCTP demonstration flight, take special care with cruise altitude: a very high flight level may not be practical on a short route, so check the generated plan rather than assuming the automatic choice is appropriate.

## 5. Generate and inspect the OFP

Once the required airport codes and any optional settings are ready, press **GENERATE PLAN**.

After successful generation, the OIS automatically opens the **OFP** page and shows a **PLAN GENERATED SUCCESSFULLY** notification.

This isn't merely a local draft in the cockpit: it creates a new plan in your **SimBrief account**, just as if you'd generated it with the SimBrief website.

Read through the OFP and check the origin, destination, proposed route, alternate, fuel and weights. Make sure you're happy with the plan before using it in the flight-management system.

## 6. Use the generated plan in the aircraft

Generating an OFP and loading the aircraft are **separate steps**.

The new plan is available to the OIS through the normal SimBrief import or sync functions. Use the appropriate import/sync control on:

- **FLT OPS STATUS** — flight operations information.
- **LOADSHEET** — payload and fuel loading.
- **TO PERF** — takeoff performance calculation.
- **LDG PERF** — landing performance calculation.

To retrieve the flight plan into the aircraft's flight-management system, go to the **FMS INIT page** and use **CPNY F-PLN REQUEST**. Confirm that the requested route is the new plan you generated.

Now review the departure, route and arrival on the FMS. The availability of a plan in SimBrief doesn't remove the need to verify procedures, constraints and runway selections. Load the intended fuel and payload using the appropriate OIS controls before calculating takeoff performance.

From this point, continue with the [full A350 flight tutorial](/blog/inibuilds-airbus-a350-full-flight-tutorial/), starting with flight-plan verification and takeoff preparation.

## Troubleshooting

### Nothing happens when I generate a plan

Check the connection in **OPTIONS → 3RD PARTY**, make sure your SimBrief ID is numeric, and verify that both airport fields contain valid four-letter ICAO codes.

### The OIS has a plan but the FMS doesn't

A generated OFP is not automatically the active route on the MFD. Use **CPNY F-PLN REQUEST** on the **INIT** page, then check and confirm the requested plan.

### The payload or fuel doesn't match the OFP

Import or sync the new SimBrief plan on the **LOADSHEET** page and use the relevant loading controls. Generating a plan doesn't by itself physically load its planned fuel and payload.

### I need to start again

Use **CLEAR** to reset the planning form. Remember that generating another flight plan updates the active plan on your SimBrief account.

## References and related tutorials

- [iniBuilds official guide: Create SimBrief flight plans on the OIS](https://forum.inibuilds.com/topic/29120-how-to-create-simbrief-flightplans-on-the-ois-flt-ops-plan/) — primary reference, published 4 April 2025.
- [iniBuilds A350 aircraft manual](https://forum.inibuilds.com/topic/25085-a350-aircraft-manual/).
- [JP-Game: iniBuilds A350 full-flight tutorial](/blog/inibuilds-airbus-a350-full-flight-tutorial/).

*Screenshot checklist before final editorial sign-off: third-party settings, the FLT OPS PLAN form, the generated OFP, the loadsheet sync screen, and the FMS CPNY F-PLN REQUEST page. Use screenshots from the same aircraft version as the instructions.*

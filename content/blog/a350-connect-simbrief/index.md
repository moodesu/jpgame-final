+++
authors = ["JPGame"]
title = "Connect SimBrief to the iniBuilds Airbus A350"
date = 2026-11-03
description = "Step-by-step setup for linking your SimBrief account to the iniBuilds A350 OIS, authenticating Navigraph, and checking that flight-plan import works in MSFS 2024."
tags = ["MSFS 2024", "A350", "SimBrief", "iniBuilds", "Navigraph"]
categories = ["MSFS", "Tutorial"]
slug = "connect-simbrief-inibuilds-a350"
+++

[← All Airbus A350 tutorials](/guides/a350/)

## Introduction

Before we can use SimBrief flight plans in the **iniBuilds Airbus A350 for Microsoft Flight Simulator 2024**, we need to link our SimBrief account to the aircraft's **Onboard Information System (OIS)**.

There are **two different pieces of account information** on the OIS setup page: a **numeric SimBrief User ID**, used for flight-plan import, and **Navigraph account authorisation**, used for Navigraph-integrated features including the OIS flight-plan generator. This tutorial covers both, then shows how to check that the aircraft can retrieve your plan.

We'll use **Hong Kong (VHHH) to Taiwan Taoyuan (RCTP)** as our example, matching the [A350 full-flight tutorial](/blog/inibuilds-airbus-a350-full-flight-tutorial/).

## 1. Prepare your SimBrief account

Sign in to [SimBrief](https://www.simbrief.com/) and ensure you have an account and can access its flight planning tools.

For the import test later in this guide, generate a current flight plan with **VHHH** as departure and **RCTP** as destination. Use an A350-900 profile if you're following our main tutorial.

You will also need your **SimBrief User ID**. This is a numeric account identifier—not the username or email address you use to sign in. You can find it in your SimBrief account details or account settings. Copy the number exactly.

## 2. Power the A350

Start Microsoft Flight Simulator 2024, load the iniBuilds A350 at an airport parking stand and establish electrical power using ground power or the APU.

The OIS is the tablet-style display in the cockpit. Open its **FLT OPS MENU** home screen.

## 3. Enter your SimBrief User ID

Navigate to:

**FLT OPS MENU → OPTIONS → 3RD PARTY**

Find the field labelled **SimBrief User ID**, enter your numeric ID and confirm the entry as required by the OIS.

| Field | What to enter |
|---|---|
| SimBrief User ID | Your **numeric** account ID |
| SimBrief username | **Do not** enter it in the User ID field |
| Hoppie login | Optional, unrelated to the basic SimBrief flight-plan import |

The aircraft manual specifically identifies this page as the location for the SimBrief User ID. If you use Hoppie's ACARS service, its login field is separate and can be configured independently.

## 4. Authorise Navigraph for the integrated planner

If you want to use the A350's built-in **FLT OPS PLAN** function to *create* SimBrief flight plans directly in the cockpit, iniBuilds also instructs you to connect your Navigraph account on the **3RD PARTY** screen.

You can authenticate in either of these ways:

1. Scan the **QR code** displayed on the OIS with your phone, then follow the sign-in instructions.
2. Alternatively, open [navigraph.com/code](https://navigraph.com/code) in a browser and enter the authorisation code displayed on the OIS.

Finish the account-authorisation process and return to the cockpit. After a successful connection, iniBuilds says the OIS should display **UPDATE DATA** and **RESET NAVIGRAPH**. These are useful visual checks that Navigraph authorisation has completed.

**Important:** Don't confuse the two steps. Entering your SimBrief User ID and authorising your Navigraph account are separate actions. The official iniBuilds instructions require both for **generating a plan directly on the OIS**.

## 5. Test importing an existing flight plan

With your VHHH–RCTP SimBrief plan generated, use the OIS navigation bar and open:

**FLT OPS MENU → FLT OPS STS**

Select **SIMBRIEF IMPORT**. The OIS should retrieve your current SimBrief plan.

Check that it shows the expected departure and destination, and compare the flight information with your SimBrief OFP. For our published example, the flight is **EVTWF2605**, but if you generate another OFP, use the details of **your newest plan**, not that earlier flight's number.

Next open **LOADSHEET**. Import or synchronise the relevant fuel and payload information. The aircraft manual instructs you to use **SET ZFW** and **SET FUEL** to apply these quantities; retrieving the plan alone does not necessarily load the aircraft.

## 6. Check the flight plan in the FMS

The OIS account connection does not by itself mean the route is the active flight plan in the A350's **Flight Management System (FMS)**.

Open the MFD **INIT** page and use **CPNY F-PLN REQUEST** to request the company flight plan from SimBrief. Review the imported route on the MFD, confirm the departure and arrival procedures, and check for any discontinuities that need investigation.

For our reference flight, the planned routing is:

```text
VHHH/07C DALOL1Y DALOL V631 ENVAR M750 TONGA TONGA1A RCTP/05R
```

This is specific to the **3 November 2026** OFP. If you've generated a new one, compare the FMS against the new SimBrief route instead.

## 7. Troubleshooting

### SimBrief import returns no flight

Check the **numeric SimBrief User ID** in **OPTIONS → 3RD PARTY** and confirm that an OFP has actually been generated in your account. If you have several plans, check which one is currently active in SimBrief.

### Navigraph authorisation hasn't completed

Try the on-screen QR code or visit [navigraph.com/code](https://navigraph.com/code) and enter the current code. Return to the OIS after sign-in and look for **UPDATE DATA** and **RESET NAVIGRAPH**. An expired code may need to be renewed.

### The OIS has the flight, but the FMS route is missing

Go to the MFD **INIT** page and use **CPNY F-PLN REQUEST**. Importing an OFP into the OIS and requesting the route into the FMS are separate operations.

### The route imports, but the fuel or weight is wrong

Visit **LOADSHEET**, synchronise the planned figures and use **SET ZFW** and **SET FUEL**. Check that the aircraft weight and fuel agree with the OFP before calculating takeoff performance.

## What next?

Your A350 is now configured to use SimBrief. Continue with either of these tutorials:

- [Create a SimBrief flight plan inside the A350 OIS](/blog/inibuilds-a350-ois-simbrief-flight-planning/) — enter airports and generate a plan without leaving the aircraft.
- [A350 full-flight tutorial: Hong Kong to Taiwan Taoyuan](/blog/inibuilds-airbus-a350-full-flight-tutorial/) — import the plan, configure the FMS, and fly the route.

## References

- [iniBuilds: Creating SimBrief flight plans on the OIS](https://forum.inibuilds.com/topic/29120-how-to-create-simbrief-flightplans-on-the-ois-flt-ops-plan/)
- [iniBuilds: Airbus A350 aircraft manual](https://forum.inibuilds.com/topic/25085-a350-aircraft-manual/)

*Screenshots to add: OIS OPTIONS → 3RD PARTY, Navigraph authorisation and successful connection, FLT OPS STS import, LOADSHEET, and FMS INIT company flight-plan request.*

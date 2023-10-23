from dataclasses import dataclass


@dataclass
class QuestionSet:
    question: str
    generative_answer: str
    retrieved_passages: list


question_set1 = QuestionSet(
    question = "What is manufactured at this working site?",
    generative_answer = "This site manufactures satellites, satellite components as well as sensors and antenna systems for satellites. Primary customers are the U.S. Government include the Department of Defense and NASA, as well as private industry who work with space and earth sciences.",
    retrieved_passages = [
        """Occupancy/Special Hazards
    This site manufactures satellites, satellite components as well as sensors and antenna systems for
    satellites. Primary customers are the U.S. Government include the Department of Defense and NASA, as
    well as private industry who work with space and earth sciences. Supporting activities include R&D,
    design, and testing. The facility includes many labs for specific disciplines as well as two machine shops.
    Production is currently supported by a staff of approximately 2,466 employees working mostly a single
    shift. The Some Springfield campus covers nearly 835,000 in over 20 owned and leased buildings of non-
    combustible construction. Approximately 70% of the buildings are sprinklered. The main production /
    assembly areas are in the FA, YY, FI and FT building complex on Commerce street. These buildings
    include various labs, testing assemblies, clean rooms and component assembly areas. Overhead cranes
    are provided in the high bay areas and some clean rooms to handle larger project components.
    The remaining buildings on the Springfield Some campus are for various labs, offices, engineering,
    technical service, facilities, design and R&D. It is understood these functions while important are not
    critical to the ongoing work in the ”F” building complexes as the work could be performed elsewhere.
    Hazards include the storage and handling of flammable liquids and waste solvents in lab areas. Approved
    flammable liquids cabinets are in place and procedure seem adequate except for the temporary storage
    of flammables on the building FA dock while waiting QC testing and inspection. Flammable flux is used in
    the FA building wave soldiering machine that has a flash point of 52 deg F. CO 2 protection has been
    recommended.
    A detached approved flammable liquids storage container is located detached approximately 18 ft
    from the north wall of building YY for the storage of waste solvent and miscellaneous flammables. The
    building is protected with an automatic dry chemical system""",

    """Utilities
    Electrical Systems – The power to the plant is supplied by a single feeds to the various facility buildings.
    The electrical power supply is reported to be reliable.
    Annual infrared thermal scans are made annually.
    Transformers – The main transformers are owned and maintained by the electrical utility. There are
    several oil filled medium voltage transformers are located on site. Transformer oil testing is completed on
    an annual basis with the last testing in March of 2001. There are no PCBs reported in any transformers.
    Overhead Lighting – No unusual features.
    Natural Gas/Building Heat – Buildings are heated by natural gas fired unit heaters or furnaces.
    Industrial Boilers – There are several Patterson Kelly small gas-fired boiler throughout with acceptable
    combustion controls.
    Chilled Water – There are Chillers in Buildings FT and FA to serve the “F” building complex. The
    cooling tower located between Building FT and YY is reported to contain YY approved fill material.
    Compressed Air Systems – Air compressors are provided with a level of redundant capacity. The units
    are rotated in and out of service to even the life cycle. Compressed air can be provided via trailer
    mounted units if needed.
    Emergency Diesel Generators – Emergency are installed in the “F” Complex for computers, phones and
    emergency lighting;
    Lift Trucks – none
    Vacuum Pumps – Very small units in some labs, with larger units for the 2 large vacuum chambers;""",

    """Business Interruption Features
    This plant is currently operating at what appears to be 100% capacity with very little available production
    in the event of a loss resulting in an interruption of operations.
    Contingency plans call for assistance from other Some location in Broomfield, Colorado. However
    many functions not available in Broomfield that include Lubrication Lab, Polymerics Lab, Cleaning Lab,
    X-ray, NDT, dimensional tolerances, Metal Finish shop, Detector Technology Center, Metrology,
    components in the Machine shop, Electronics Production Lab, Weld shop, acoustical testing, Vibration
    Lab, Vacuum Lac, Leak Check Lab, EMI shops, and many of the cleanrooms. In addition the large
    vacuum chamber used for testing is not duplicated and could take up top 18 months to replace.
    The use of outside vendors for parts varies from 30 to 70% approximately based on the project
    and customer requirements. Most but not all parts have at least two approved suppliers.
    Some can manufacture some parts or purchase if needed provided the supplier is customer approved.
    Computer data is backed up either daily or weekly (depending on the data) to the Some facility
    in Westminster, CO.
    It should be noted that full observation of all areas and photographs were not permitted due to security
    requirements. Additionally critical information to develop accurate Business Interruption loss estimates
    was also denied for the same security requirements. All comments and recommendations is based only
    on the areas observed and information provided.""",

    """Intrusion Supervision – None
    Watchman – Security at this site is considered to be adequate with access control systems in place in all
    building. Security service is provided on site during the day shift. All fire alarms ring to the security
    headquarters at the Some Aerospace Facility in Otherplace, Colorado.
    Operating Hours – The plant operates one shift 5 – 6 days based on department and projects / testing in
    progress."""
    ]
)

question_set2 = QuestionSet(
    question = "What are the main risks at this location?",
    generative_answer = "The main risks at this location include fire, flood, earthquake, and climate-related hazards. Fire risks are considered to be low due to the lack of directly adjacent structures, however, there is still a risk of fire due to human error or other causes. Flood risks are low due to the facility being located outside the 500-year flood zone, but it is still important to monitor the area for potential flooding. Earthquake risks are moderate due to the facility being located in the MR earthquake zone. Climate-related hazards such as snow, ice, and wind can also pose a risk to the facility.",
    retrieved_passages = [
        """Risk Assessment Risk Management Passive Protection Occupancy Hazards Human Element Active Protection Surveillance Third Party Exposure BI Exposure Standard Standard Standard Below Standard Below Standard Standard Low Severe Vulnerability: 74/ 100 Location Quality Rating: 8.7/ 20""",
        
        """Exposures
    Fire – Low; no directly adjacent structures.
    Flood – This facility is located outside the 500 yr. flood zone. Building FA and FI has been reevaluated
    based on the 2013 flood to Zone X. Zone X is areas determined to be outside 500-year floodplain
    determined to be outside the 1% and 0.2% annual chance floodplains;
    Earthquake – This facility is located in the MR earthquake zone – 0. Damage Expected – None.
    Climate – This site is located in an area subject to significant snow, ice and low winter temperatures.
    Surface Water – This facility is not susceptible to surface water damage.
    Smoke Damage – The production areas and storage areas are highly susceptible to smoke damage.
    Snow Loading – Roofs are designed per local snow loading and exposures.
    Hail Storm – Hail exposure is MR Zone 5.
    Rainfall Intensity/Surface Water – The site appears to have proper positive drainage.
    Windstorm – Exposure in extra tropical storm is 121 to 160 km/hr. The plant is located in a MR Tornado
    Zone 3.
    Water/Liquid Damage – This facility is not susceptible to water/liquid damage.
    Lightning – Lightning exposure per MR is 4 to 10 strokes per year/km 2 . Lightning protection is not
    provided. There are no buildings, chimneys, stacks, or miscellaneous structures over 75 ft. in height.""",

    """Risk Evaluation Summary
    Fire and Natural Catastrophe Perils
    ONBEKENDE CORPORATION
    AEROSPACE & TECHNOLOGIES DIVISION
    UNITED STATES OF AMERICA
    Longitude: -8.572721
    Latitude: 57.837894
    Client Code: 1-01010
    Site Code: US-10101
    Survey Date: 20 April 2001
    Engineer: Tim SMITH""",

    """Earth Quake – MR Zone 0
    The site survey consisted of the following:
    - A review of recent or planned changes in production, products, construction, or fire protection;
    - A review of loss prevention Human Element Programs;
    - A review of preventative and predictive maintenance procedures;
    - A partial tour of the production facility interior and exterior, as limited by security requirements;
    - A visual inspection of fire protection equipment and associated fire protection control valves, as limited
    by security requirements;
    - Discussion of observations and recommendations;
    Human Element programs were found to be in various stages of development. Programs reviewed included
    the following:
    - Housekeeping;
    - Hot Work;
    - Fire Protection Impairments;
    - Fire Protection Inspection and Maintenance;
    - Management of Change;
    - Smoking Policy;
    - Contractors Work Procedures;
    - Emergency Procedures;
    - Business Contingency Planning;
    Continuity of combustibles throughout the site is generally considered light to moderate in most areas.
    Production hazards are considered to be low and are generally well controlled.
    Security at this site is considered to be adequate with access control systems in place in all building.
    Security service is provided on site during the day shift. All fire alarms ring to the security headquarters
    at the Some Aerospace Facility in Broomfield, Colorado.
    Key opportunities for improvement were observed with recommendations made as follows:
    1. Improve or add sprinkler protection in critical areas;
    2. Improve maintenance and inspection of fire protection equipment;
    3. Improve inspection and service of fire extinguishers;
    4. Provide battery backup for aspirating smoke detection systems in in critical assembly and testing areas;
    5. Improving storage of flammable liquids on the FA dock;
    6. Repair the leaking fire department connection for the FA building;
    7. Provide CO2 fire protection for the Heller 1707 MK III wave soldering machine in the FA building;
    8. Develop an effective business contingency plan for all critical operations;
    9. The solid shelving in the store room area should to allow for fire sprinkler distribution;
    Overall the Somwhere facility was found to be well maintained with excellent. Cooperation of the plant
    facilities staff was very much appreciated.""",

    """Risk Engineering Report
    Property - Fire and Natural Catastrophe Perils
    Aerospace & Technologies Division
    1000 Evergreen Street
    Springfield CO 10101
    UNITED STATES OF AMERICA
    Survey type : Original
    Survey date : 20 April 2001
    Engineer : Tim Smith"""
    ]
)

question_set3 = QuestionSet(
    question = "Where does this location get their water supply from?",
    generative_answer = "This location gets their water supply from the city of Springfield's municipal water supply.",
    retrieved_passages = [
        """Water Supply Test Results
Water Supply
COPE Report
This site is supplied by a strong municipal water supply from the city of Springfield. The facility sprinklers are fed from
6-inch connections to 8-inch city water mains.
FIRE	 RATING	 SUCTION	   AUTO OR	    PUMPS	 GPM @ PSI @ RPM	 FROM	 DRIVE	 MANUAL	 RELIABLE	 COMMENTS/CONDITIONS
DATE	 TEST	 FLOW LOCATION &	 GPM	 STATIC	 NET OR	 STATIC &	 FIRE PUMP
                    SUCT	 DISCH	 SPEED	 RATING
& BY	 OF	 DISCHARGE COEFF.	     RESIDUAL	 RESIDUAL LOCATION	 PSI	 PSI	 RPM	  City of Springfield Water	 City	 February 2014	 1876	 155	 150""",

"""Protection
Fire Protection Water – This site is supplied by a strong municipal water supply from the city
of Springfield. The facility sprinklers are fed from 6-inch connections to 8-inch city water mains.
Sprinkler Protection – This facility is 70% sprinklered with approximately 25% sprinklers needed.
Existing sprinklers consist of both wet pipe and pre-action type sprinklers. Designs range from light to
ordinary hazard and are adequate for the occupancy.
Gaseous Suppression – There is both CO 2 and clean agent systems at this location for clean room and
freezer protection. Systems were noted to be lacking current service and inspection. Recommendations
have been made for improvements.
Fire Extinguishers – Fire extinguishers were found to be mostly adequately arranged. However many
were found to be lacking current inspections and additional units should be placed in some areas, see
recommendations.""",

"""Utilities
Electrical Systems – The power to the plant is supplied by a single feeds to the various facility buildings.
The electrical power supply is reported to be reliable.
Annual infrared thermal scans are made annually.
Transformers – The main transformers are owned and maintained by the electrical utility. There are
several oil filled medium voltage transformers are located on site. Transformer oil testing is completed on
an annual basis with the last testing in March of 2001. There are no PCBs reported in any transformers.
Overhead Lighting – No unusual features.
Natural Gas/Building Heat – Buildings are heated by natural gas fired unit heaters or furnaces.
Industrial Boilers – There are several Patterson Kelly small gas-fired boiler throughout with acceptable
combustion controls.
Chilled Water – There are Chillers in Buildings FT and FA to serve the “F” building complex. The
cooling tower located between Building FT and YY is reported to contain YY approved fill material.
Compressed Air Systems – Air compressors are provided with a level of redundant capacity. The units
are rotated in and out of service to even the life cycle. Compressed air can be provided via trailer
mounted units if needed.
Emergency Diesel Generators – Emergency are installed in the “F” Complex for computers, phones and
emergency lighting;
Lift Trucks – none
Vacuum Pumps – Very small units in some labs, with larger units for the 2 large vacuum chambers;""",

"""Summary
East and North View of XX and YY Buildings
This report documents the original Expert.ai MATRIX Property Loss Control Survey at the SOME
Aerospace facility in Springfield, Colorado, USA. The facility is located on a very large campus covering
several city blocks in central Springfield.
This site manufactures satellites, satellite components as well as sensors and antenna systems for
satellites. Primary customers are the U.S. Government include the Department of Defense and NASA, as
well as private industry who work with space and earth sciences. Supporting activities include R&D, design,
and testing. The facility includes many labs for specific disciplines as well as two machine shops.
Production is currently supported by a staff of approximately 2,466 employees working mostly a single shift.
The Some Springfield campus covers nearly 835,000 in over 20 owned and leased buildings of non-
combustible construction. Approximately 70% of the buildings are sprinklered. The main production /
assembly areas are in the YY, YY, XX and ZZ building complex on Some street.
The Springfield public water system provides an adequate supply to the automatic sprinklers via 8-inch
mains. Adequate public fire hydrants are available feed from the 8-inch mains. This large campus has
minimal exterior exposures.
It should be noted that full observation of all areas and photographs were not permitted due to security
requirements. Additionally critical information to develop accurate Business Interruption loss estimates was
also denied for the same security requirements. All comments and recommendations is based only on the
areas observed and information provided.
Natural catastrophe exposures are as follows per Munich Re:
Tornado – Zone 3
Hail – Zone 5
Flood – Located above 500yr level;
Lighting - 4 – 10 strokes yr/km2""",

"""Comments
Observation of the fire department connection concluded it has been leaking for some time."""
    ]
)

question_set4 = QuestionSet(
    question="Which recommendations were made at this location?",
    generative_answer="The key recommendations made at this location included installing sprinklers in several of the buildings owned by Some in accordance with YY Global standards, increasing the amount of sprinklers needed to cover the facility, installing gaseous suppression systems throughout the site, and improving security with access control systems in place in all buildings. Additionally, it was suggested that security service be provided on site during the day shift and that all fire alarms ring to the security headquarters at the Some Aerospace Facility in Broomfield, Colorado.",
    retrieved_passages=[
        """Earth Quake – MR Zone 0
The site survey consisted of the following:
- A review of recent or planned changes in production, products, construction, or fire protection;
- A review of loss prevention Human Element Programs;
- A review of preventative and predictive maintenance procedures;
- A partial tour of the production facility interior and exterior, as limited by security requirements;
- A visual inspection of fire protection equipment and associated fire protection control valves, as limited
by security requirements;
- Discussion of observations and recommendations;
Human Element programs were found to be in various stages of development. Programs reviewed included
the following:
- Housekeeping;
- Hot Work;
- Fire Protection Impairments;
- Fire Protection Inspection and Maintenance;
- Management of Change;
- Smoking Policy;
- Contractors Work Procedures;
- Emergency Procedures;
- Business Contingency Planning;
Continuity of combustibles throughout the site is generally considered light to moderate in most areas.
Production hazards are considered to be low and are generally well controlled.
Security at this site is considered to be adequate with access control systems in place in all building.
Security service is provided on site during the day shift. All fire alarms ring to the security headquarters
at the Some Aerospace Facility in Broomfield, Colorado.
Key opportunities for improvement were observed with recommendations made as follows:
1. Improve or add sprinkler protection in critical areas;
2. Improve maintenance and inspection of fire protection equipment;
3. Improve inspection and service of fire extinguishers;
4. Provide battery backup for aspirating smoke detection systems in in critical assembly and testing areas;
5. Improving storage of flammable liquids on the FA dock;
6. Repair the leaking fire department connection for the FA building;
7. Provide CO2 fire protection for the Heller 1707 MK III wave soldering machine in the FA building;
8. Develop an effective business contingency plan for all critical operations;
9. The solid shelving in the store room area should to allow for fire sprinkler distribution;
Overall the Somwhere facility was found to be well maintained with excellent. Cooperation of the plant
facilities staff was very much appreciated.""",

"""Protection
Fire Protection Water – This site is supplied by a strong municipal water supply from the city
of Springfield. The facility sprinklers are fed from 6-inch connections to 8-inch city water mains.
Sprinkler Protection – This facility is 70% sprinklered with approximately 25% sprinklers needed.
Existing sprinklers consist of both wet pipe and pre-action type sprinklers. Designs range from light to
ordinary hazard and are adequate for the occupancy.
Gaseous Suppression – There is both CO 2 and clean agent systems at this location for clean room and
freezer protection. Systems were noted to be lacking current service and inspection. Recommendations
have been made for improvements.
Fire Extinguishers – Fire extinguishers were found to be mostly adequately arranged. However many
were found to be lacking current inspections and additional units should be placed in some areas, see
recommendations.""",

"""Comments
Very little information was made available on ay procedures all ready established.""",

"""Main Changes / Projects
Currently, it is being planned that the Tech Tower and buildings T-1, T-2 and T-3 will razed to make room
for a new engineering building. The current occupancies will be shifted to other buildings on the campus
during the project. When completed many of the occupants of the leased buildings will be moved to the new
engineering building.
Additionally, plans are also being made to install sprinklers in several of the buildings owned by Some in
accordance with YY Global previous recommendations including the penthouse supporting the FA clean
room and the 3rd floor north area of building FT. Design specifics and schedules were not available.
The site has recently completed a new electrical connection and switch gear for Building FI. The new
equipment will increase reliability and capacity for additional equipment with in the complex.
The FA large clean room is expected to be changed to an assembly area in the next 2 years.
YY Global recommendations 13-03-002 & 003 have been reported completed.
No sprinklers have been recommended for the T-1,2,3 and Tech Tower or leased building based on limited
impact to operations and impeding replacement by the new engineering building.""",

"""Risk Assessment
Risk Management	 Passive Protection	 Occupancy Hazards	 Human Element	 Active Protection	 Surveillance	 Third Party Exposure	 BI Exposure
Standard	 Standard	 Standard	 Below Standard	 Below Standard	 Standard	 Low	 Severe
Vulnerability: 74/ 100
Location Quality Rating: 8.7/ 20"""
    ]
)

question_set5 = QuestionSet(
    question="Which is the cost estimated for the new recommendations?",
    generative_answer="The cost estimated for the new recommendations is $169,100,000.",
    retrieved_passages=[
        """Risk improvement potential
Currency USD LE before: Loss Estimate before the recommendation is completed
Fire
Rec. No. Recommendation Status LE before
2017.2	 HUMAN ELEMENT Fire Protection Maintenace and Testing Open Priority: Important	 0 0 0
2017.6	 Sprinkler Leak Open	 0 0 0
  Priority: Important	  2017.8	 Fire Extinguisher Inspections & Placement Open	 0 0 0
  Priority: Important	  2017.4	 Business Contingency Planning Open	 0 0 0
  Priority: Important""",

  """Maximum Foreseeable Loss (MFL – Fire)
Scenario:
A fire in the FA penthouse ( which is unprotected with automatic sprinklers), would result in fire and smoke damage
to the FA clean room damaging all equipment, contents and work in progress. With no response from the public
fire department the fire would be expected to involve 75% of the "F" complex either through direct damage or
smoke and water damage.
Property damage would be 75% of the estimated "F" complex (estimated to be 80% of site values) PD =
69,100,000 USD
Operations would be expected to be affected for 12 months, however it is thought that some portion of work could
be shifted to the Broomfield location. With an estimated total net loss of 10 months or 83%. BI = 332,000,000 USD
BI = 100,000,000 USD
MFL: PD = 207,300,000 BI without interdependencies = 332,000,000 Total = 539,300,000
BI with interdependencies = Not evaluated
Definition: The MFL represents the estimate of the loss (property damage and business interruption) that could happen under the
most adverse conditions in the event of fire or explosion with all fire protection out of service and no response from any public or
private emergency response organizations.""",

"""Main Changes / Projects
Currently, it is being planned that the Tech Tower and buildings T-1, T-2 and T-3 will razed to make room
for a new engineering building. The current occupancies will be shifted to other buildings on the campus
during the project. When completed many of the occupants of the leased buildings will be moved to the new
engineering building.
Additionally, plans are also being made to install sprinklers in several of the buildings owned by Some in
accordance with YY Global previous recommendations including the penthouse supporting the FA clean
room and the 3rd floor north area of building FT. Design specifics and schedules were not available.
The site has recently completed a new electrical connection and switch gear for Building FI. The new
equipment will increase reliability and capacity for additional equipment with in the complex.
The FA large clean room is expected to be changed to an assembly area in the next 2 years.
YY Global recommendations 13-03-002 & 003 have been reported completed.
No sprinklers have been recommended for the T-1,2,3 and Tech Tower or leased building based on limited
impact to operations and impeding replacement by the new engineering building.""",

"""Values and Loss Estimates
FIRE	 Group Currency	 Local Currency	 %	 Values Provided by:	 Broker 2001	  Currency	 USD	 USD	        Exchange Rate	 1.0000	 1.0000	        PD Values	 345,462,341	 345,462,341	        BI Values	 400,000,000	 400,000,000	        BI Values Period	 12 months	 12 months	        Total Sum Insured	 745,462,341	 745,462,341	     PD	  PD MFL	 207,300,000	 207,300,000	 60%	   BI	  BI MFL	 332,000,000	 332,000,000	 83%	      Total MFL	 539,300,000	 539,300,000	 72%	      PD NLE	 69,100,000	 69,100,000	 20%	      BI NLE	 100,000,000	 100,000,000	 25%	      Total NLE	 169,100,000	 169,100,000	 23%	 Values MFL	 NLE	  The abovementioned BI Loss Estimates do not include interdependencies.
PD: Property Damage BI: Business Interruption MFL: Maximum Foreseeable Loss NLE: Normal Loss Expectancy
Earthquake	   Tropical Storms & Cyclones	   Flood
  Expert.ai EQ Zone: 0	   Expert.ai WS Zone: 0	 0	 Flood Hazard:	 Above 500 Year Level
EML-EQ: Not evaluated	   EML-Wind: Not evaluated	   EML 100 -Flood:	 Not evaluated 3
Expert.ai EQ Zone: 0 m/s² ≤ PGA   0.6 m/s²
Expert.ai WS Zone: Tropical Storms: 120-141 km/h,
75-88 mph EML: Estimated Maximum Loss""",


"""PHYSICAL PROTECTION
Active Protection
          2017.1	 Improve Sprinkler Protection	 Open	 169,100,000	 1,500,000	 750,000
  Priority: Important	        Occupancy Related Hazards
          2017.5	 Flammable Liquids Storage	 Open	 65,000,000	 1,500,000	 50,000
  Priority: Important	        2017.7	 CO2 Protection Wave Soldering	 Open	 13,500,000	 1,500,000	 25,000
  Priority: Important	        Surveillance
          2017.3	 Back UP Power Aspirating Smoke Detection Systems	 Open	 60,000,000	 1,500,000	 50,000
  Priority: Important	        """
    ]
)

question_set6 = QuestionSet(
    question="Which actions need to be taken to adhere to  fire protections standards?",
    generative_answer="""A. Monthly fire protection valve inspections
B. Monthly waterflow alarm tests
C. Monthly sprinkler riser drain tests
D. Semi Annual tests and inspection of all CO2 fire protection systems per NFPA 12
E. Semi Annual tests and inspection of all clean agent fire protection systems per NFPA 2001
F. Aspirating smoke detection systems should be tested and inspected annually
G. Fire Extinguisher Inspections & Placement per NFPA 10 standard
H. Human Element Programs Fire Protection Self-Inspections
I. Improve Sprinkler Protection
J. Flammable Liquids Storage""",
    retrieved_passages=[
        """2017.2 Fire Protection Maintenace and Testing
The following improvements should be made to insure the reliability of all fire protection
systems;
A. Monthly fire protection valve inspections;
B. Monthly waterflow alarm tests;
C. Monthly sprinkler riser drain tests;
D. Semi Annual tests and inspection of all CO2 fire protection systems per NFPA 12;
E. Semi Annual tests and inspection of all clean agent fire protection systems per NFPA
2001;
F. Aspirating smoke detection systems should be tested per NFPA 72 and manufactures
requirements;
G. Pre-Action Sprinkler systems should be trip tested per NFPA 25 standard for
maintenance and inspection of water based sprinkler systems""",

"""Protection
Fire Protection Water – This site is supplied by a strong municipal water supply from the city
of Springfield. The facility sprinklers are fed from 6-inch connections to 8-inch city water mains.
Sprinkler Protection – This facility is 70% sprinklered with approximately 25% sprinklers needed.
Existing sprinklers consist of both wet pipe and pre-action type sprinklers. Designs range from light to
ordinary hazard and are adequate for the occupancy.
Gaseous Suppression – There is both CO 2 and clean agent systems at this location for clean room and
freezer protection. Systems were noted to be lacking current service and inspection. Recommendations
have been made for improvements.
Fire Extinguishers – Fire extinguishers were found to be mostly adequately arranged. However many
were found to be lacking current inspections and additional units should be placed in some areas, see
recommendations.""",

"""PHYSICAL PROTECTION
Active Protection
          2017.1	 Improve Sprinkler Protection	 Open	 169,100,000	 1,500,000	 750,000
  Priority: Important	        Occupancy Related Hazards
          2017.5	 Flammable Liquids Storage	 Open	 65,000,000	 1,500,000	 50,000
  Priority: Important	        2017.7	 CO2 Protection Wave Soldering	 Open	 13,500,000	 1,500,000	 25,000
  Priority: Important	        Surveillance
          2017.3	 Back UP Power Aspirating Smoke Detection Systems	 Open	 60,000,000	 1,500,000	 50,000
  Priority: Important""",

  """Human Element Programs
Fire Protection Self-Inspections – Inspection programs are well developed and documented and are
completed by a combination of plant maintenance staff and qualified outside contractors.
Human Element – Fire Protection Self Inspection Program	 Frequency	 Documentation	 Person/ Department Responsible
Fire Pump Churn Testing	 Weekly	 N/A	 N/A
Visual Inspection of All Sprinkler / Fire Protection Control Valves	 Semi Annual	 yes	 Maintenance
Sprinkler waterflow alarm testing	 Semi Annual	 yes	 Contractor
2-inch main drain testing	 Semi Annual	 yes	 Contractor
Visual inspection of all fire extinguishers	 Monthly	 Limited	 Plant
Physical inspection of all fire extinguishers	 Annually	 yes	 Contractor
Physical inspection of all sprinkler control valves (complete turndown)	 Semi Annual	 yes	 Contractor
Physical inspection of all sprinkler control valves (PIVs)	 Semi Annual	 yes	 Maintenance
Physical test of the fire alarm system	 Semi-annual	 yes	 Contractor
Hydrant Flushing	 City of Springfield	 yes	 Contractor
Servicing of Fire Pump Diesel Drivers	 Annually	 N/A	 N/A
Lubricate all sprinkler control valves	 Unknown	 None	 Contractor
Special Hazards Systems	 Varies	 Limited	 Contractor
Housekeeping – Housekeeping at the plant was found to be at a very high level with regular
housekeeping inspections made.""",

"""2017.8 Fire Extinguisher Inspections & Placement
The Inspections & Placement of fire extinguishers should be reviewed per NFPA 10
standard on fire extinguishers to ensure the following:
A. Extinguisher are available and placed at readily accessible locations;
B. Extinguisher are inspected monthly;
C. Extinguishers are provided with annual contractor service, maintenance and any
required testing.
Noted areas of concern included the YY penthouse, FI penthouse, software lab, rooms
2C385 & 2B149. All areas should be reviewed."""
    ]
)

question_set7 = QuestionSet(
    question="which kind of earthquake reinforcement does the building have?",
    generative_answer="The building has reinforced concrete bearing walls, which is a type of earthquake reinforcement.",
    retrieved_passages=[
        """Natural Catastrophe Perils
Earthquake
Expert.ai EQ Zone:
Local soil conditions:
Building type:
Building irregularities:
0 (0 m/s² ≤ PGA   0.6 m/s²)
Average
3: Reinforced concrete bearing walls
No""",

"""Flood
Flood Zone:
Above 500 Year Level
Vulnerability of contents to
water damage: Severe
Comments:
This facility is located outside the 500 yr. flood zone. Building FA and FI has been reevaluated based on the 2013
flood to Zone X. Zone X is areas determined to be outside 500-year floodplain determined to be outside the 1%
and 0.2% annual chance floodplains;""",

"""Construction
Area ft 2	 Percentage	 Building Height	 Construction	 Floor
404,650	 48	 5 Story	 Reinforced Concrete	 Concrete
84,900	 10	 4 Story	 Concrete on Protected Steel	 Concrete
12,500	 1	 1 Story	 Concrete on Exposed Steel	 Concrete
45,300	 5	 2 Story	 Steel Deck 1	 Concrete
46,080	 6	 5 Story	 Misc. Non Combustible	 Concrete
240,802	 29	 2 Story	 Steel Deck 2	 Concrete
576	 0	 1 Story	 Plank on timber	 Concrete""",

"""Exposures
Fire – Low; no directly adjacent structures.
Flood – This facility is located outside the 500 yr. flood zone. Building FA and FI has been reevaluated
based on the 2013 flood to Zone X. Zone X is areas determined to be outside 500-year floodplain
determined to be outside the 1% and 0.2% annual chance floodplains;
Earthquake – This facility is located in the MR earthquake zone – 0. Damage Expected – None.
Climate – This site is located in an area subject to significant snow, ice and low winter temperatures.
Surface Water – This facility is not susceptible to surface water damage.
Smoke Damage – The production areas and storage areas are highly susceptible to smoke damage.
Snow Loading – Roofs are designed per local snow loading and exposures.
Hail Storm – Hail exposure is MR Zone 5.
Rainfall Intensity/Surface Water – The site appears to have proper positive drainage.
Windstorm – Exposure in extra tropical storm is 121 to 160 km/hr. The plant is located in a MR Tornado
Zone 3.
Water/Liquid Damage – This facility is not susceptible to water/liquid damage.
Lightning – Lightning exposure per MR is 4 to 10 strokes per year/km 2 . Lightning protection is not
provided. There are no buildings, chimneys, stacks, or miscellaneous structures over 75 ft. in height.""",

"""Utilities
Electrical Systems – The power to the plant is supplied by a single feeds to the various facility buildings.
The electrical power supply is reported to be reliable.
Annual infrared thermal scans are made annually.
Transformers – The main transformers are owned and maintained by the electrical utility. There are
several oil filled medium voltage transformers are located on site. Transformer oil testing is completed on
an annual basis with the last testing in March of 2001. There are no PCBs reported in any transformers.
Overhead Lighting – No unusual features.
Natural Gas/Building Heat – Buildings are heated by natural gas fired unit heaters or furnaces.
Industrial Boilers – There are several Patterson Kelly small gas-fired boiler throughout with acceptable
combustion controls.
Chilled Water – There are Chillers in Buildings FT and FA to serve the “F” building complex. The
cooling tower located between Building FT and YY is reported to contain YY approved fill material.
Compressed Air Systems – Air compressors are provided with a level of redundant capacity. The units
are rotated in and out of service to even the life cycle. Compressed air can be provided via trailer
mounted units if needed.
Emergency Diesel Generators – Emergency are installed in the “F” Complex for computers, phones and
emergency lighting;
Lift Trucks – none
Vacuum Pumps – Very small units in some labs, with larger units for the 2 large vacuum chambers;"""
    ]
)
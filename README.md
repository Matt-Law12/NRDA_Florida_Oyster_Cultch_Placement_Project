# Florida Oyster Cultch Placement Restoration Project
Analyzing the monitoring data for the NRDA Florida Oyster Cultch Placement Restoration Project. Interactive PowerBI dashboard can be found [here](https://app.powerbi.com/view?r=eyJrIjoiODhhZGQxZmYtYjYzYy00MTQ0LWI3M2EtZmE3NzdlODdlOGE3IiwidCI6ImI2MjAxOTYwLTQ1YmEtNGI3OC1iMDgwLWYxYzQzM2ZmNmUzNiIsImMiOjZ9).

![Screenshot 2025-05-15 141510](https://github.com/user-attachments/assets/fc778dc5-0492-43ee-a7d9-2d50f60f37f8)

## Project Overview
The objective of the Florida Oyster Cultch Placement Project is to promote reef development for oysters by restoring existing, degraded oyster reef habitats that have reached their productive lifespan. The restoration work for this project included the placement of suitable cultch material on existing or previously constructed oyster bars by barge for the settling of native oyster larvae and oyster colonization. Approximately 61,943 cubic yards of oyster cultch was placed over an estimated 296 acres of existing oyster bars, including placing approximately 24,840 cubic yards of shell on 16 debilitated oyster reefs over an approximately 124-acre area in the Apalachicola Bay system in Franklin County, placing approximately 17,000 cubic yards of crushed granite over an estimated 84 acres of debilitated oyster reefs in the St. Andrews Bay System in Bay County, and placing approximately 20,103 cubic yards of a lime rock aggregate over an estimated 88 acres of debilitated oyster reefs in the Pensacola Bay System in Escambia and Santa Rosa Counties.

Cultch material consisted of combinations of oyster shells, either mined from existing sources or from active oyster shell collection sources, and/or limestone approved for use in these projects by Florida’s Department of Agriculture and Consumer Services (FDACS). Placing substrate or "cultch" in bays where natural reproduction occurs is the most effective technique used throughout the Gulf of Mexico to create three-dimensional reef structure, stimulate spat setting, sustain oyster fisheries, enhance community functions, increase natural productivity, and accelerate the recovery process. Florida has been involved in rehabilitating oyster reefs for more than sixty years and provides a multi-dimensional approach built on decades of experience. These restoration methods are established methods for this type of restoration project.

## Data Collection
To collect the monitoring data for this project, a diver descends and places a 0.25 m² quadrat on the bottom in a haphazard manner near the transect line. Live oysters, shell, and associated fauna are removed to the depth of the sediment, placed in mesh collecting bags, and delivered to the survey vessel. This is repeated five times on each side of the boat, as well as off the bow of the boat. A total of 15 quadrats (5 starboard, 5 port, and 5 bow) are sampled for each midpoint. 

The team onboard records water quality observations at the surface and bottom of the water column, using a Yellow Springs Instrument (YSI) handheld datasonde. Parameters recorded include: water temperature, dissolved oxygen, specific conductivity, salinity, and pH. Weather conditions, wind, current, and latitude and longitude are also recorded.

Samples are processed once all the quadrats have been collected for a midpoint. If it is not possible to process samples immediately after sampling, they are frozen until processing can be completed. 

First, the sample is weighed using a digital hanging scale. If oysters are present in the collected sample, shell height of the first 100 live oysters is measured to the nearest millimeter (mm). Oyster shell height is defined as the distance from the umbo to the distal margin of the shell.

If the sample contains more than 100 live oysters, the remaining live oysters are counted. Live oysters are divided into one of three size classes: spat (0-25 mm), seed (26-74 mm), and harvestable adult (75 mm and larger). The number of dead oysters in the sample is also counted.

Monitoring for this project occurs on a yearly basis, with annual monitoring reports being created and pubished by Central Panhandle Aquatic Preserves (CPAP) staff.

## Data Analysis
To evaluate the outcomes of the NRDA Florida Oyster Cultch Placement Restoration Project, I conducted a detailed analysis of the project's monitoring data. Using Python, along with libraries such as pandas, matplotlib, and numpy, I cleaned, grouped, and visualized the data to identify trends in oyster reef development following restoration efforts. I selected graph types and styles that prioritize clarity and accessibility, ensuring the visuals effectively communicate the data in a clear and accessible way for a broad range of stakeholders. The primary goal of this analysis was to assess how oyster populations have progressed since cultch placement, using the Florida Department of Agriculture and Consumer Services (FDACS) scale for estimating harvestable oyster density as a benchmark for reef health, defined as follows:

•	More than 400 bags/acre = Healthy oyster reefs capable of sustaining commercial harvest.

•	More than 200 bags/acre = Oyster reefs capable of sustaining limited harvest.

•	Less than 200 bags/acre = Below level necessary to support commercial harvest.

•	Less than 100 bags/acre = Oyster reefs considered depleted.


I also created an [interactive PowerBI dashboard](https://app.powerbi.com/view?r=eyJrIjoiODhhZGQxZmYtYjYzYy00MTQ0LWI3M2EtZmE3NzdlODdlOGE3IiwidCI6ImI2MjAxOTYwLTQ1YmEtNGI3OC1iMDgwLWYxYzQzM2ZmNmUzNiIsImMiOjZ9) geared more specifically towards individuals with little to no prior knowledge of the project. The dashboard enables users to explore key insights through dynamic visuals, making complex data more accessible and engaging—far beyond what static graphs or traditional reports can offer.

### Report Visuals:
Below are the visuals I created for the Apalachicola monitoring report:

![Figure_5](https://github.com/user-attachments/assets/a071e544-775b-4043-aa07-a066c822a21b) <br />
_Figure 5: Total number of live vs. dead oysters by sampling round_
<br />
<br />
<br />
<br />
![Figure_6](https://github.com/user-attachments/assets/01118f7f-26d6-4c90-92e2-24d7d59ddab3)<br />
_Figure 6: Number of live oysters by size class per sampling round_
<br />
<br />
<br />
<br />
![Figure_7](https://github.com/user-attachments/assets/7aae9ae3-6afb-41c6-894a-87a174350a2c)<br />
_Figure 7: Number of live oysters per size class by side of bay and sampling round_ 
<br />
<br />
<br />
<br />
![Figure_8](https://github.com/user-attachments/assets/46c14d2a-c8a2-43b7-b5d9-6a5054c9aa7a)<br />
_Figure 8: Number of spat sized oysters per site by round_
<br />
<br />
<br />
<br />
![Figure_9](https://github.com/user-attachments/assets/6c478869-6a4e-437f-9716-72bd5ed7dbf3)<br />
_Figure 9: Number of seed sized oysters per site by round_
<br />
<br />
<br />
<br />
![Figure_10](https://github.com/user-attachments/assets/837007eb-0296-44e4-80d5-08f4da735bb8)<br />
_Figure 10: Number of adult sized oysters per site by round_
<br />
<br />
<br />
<br />
![Figure_11](https://github.com/user-attachments/assets/d00fc7f7-9af7-469c-aed5-91bb6b5b2d11)<br />
_Figure 11: Average shell height of live oysters collected in Apalachicola Bay_
<br />
<br />
<br />
<br />
![Figure_12](https://github.com/user-attachments/assets/0523bf8c-c3a9-4fb0-a722-a2382546a3d0)<br />
_Figure 12: Shell height distribution by sampling round for the entire bay_
<br />
<br />
<br />
<br />
![Figure_13](https://github.com/user-attachments/assets/41d98d6f-a461-4752-b71f-4cc2ba05c9c0)<br />
_Figure 13: Shell height distribution by sampling round for the East side of bay_
<br />
<br />
<br />
<br />
![Figure_14](https://github.com/user-attachments/assets/5a89ec11-8ea6-4c14-9b32-12af44fbf3ec)<br />
_Figure 14: Shell height distribution by sampling round for the West side of the bay_

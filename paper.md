---
title: Which Cheifdom Has the Furtherest Average Distance to a Health Facility For Under 5 Children?
author: Jacob Lamers
output: pdf_document
bibliography: bibliography.bib
csl: american-chemical-society.csl
documentclass: report
---

<!--
pandoc -o Personal_Statement.pdf Personal_Statement.md
-->

## Introduction:

The intersection of geospatial data and public health research has become increasingly pivotal in recent years. As researchers and policymakers seek to address complex healthcare challenges, understanding the geographical distribution of health facilities and demographic patterns emerges as a cornerstone for effective planning and resource allocation. Geospatial analysis allows for a nuanced exploration of spatial relationships, offering insights that extend beyond traditional demographic studies. This analysis, often conducted through the lens of geographic information systems (GIS), has the potential to inform evidence-based decision-making and enhance the overall efficiency of healthcare systems [@doi:10.1080/17538941003759255].

The objective of the analysis presented here is to embark on a comprehensive geographic exploration, amalgamating third-level administrative geodata, health center geodata, and population estimates. This multifaceted approach seeks to uncover intricate patterns in health center distribution, population demographics, and accessibility within specific geographical regions. By combining diverse datasets and employing spatial analysis techniques, this study aims to contribute to the growing body of knowledge that leverages geospatial insights for public health enhancement.

## Methods

The provided code encompasses a multifaceted data processing pipeline. In the initial phase, the code focuses on data acquisition by downloading and extracting third-level administrative geodata, health center geodata, and population estimate data. Each dataset is stored in dedicated directories for subsequent processing.

The code leverages the GeoPandas library to manipulate the third-level administrative geodata and health center geodata. Spatial operations, such as a spatial join, are performed to associate health centers with specific districts. The resulting GeoDataFrame captures the count of health centers within each district, contributing to a comprehensive understanding of their distribution.

The population data processing section involves reading data from GeoTIFF files and constructing a GeoPandas DataFrame. This DataFrame encapsulates pixel coordinates as points and their corresponding population values. Age and gender-specific DataFrames are created, eventually merged into a unified GeoDataFrame. The total population is then computed through grouping based on spatial geometry.

To facilitate further analysis, the GeoDataFrame with population data is exported as a CSV file. The code subsequently conducts a spatial join between the population GeoDataFrame and the district GeoDataFrame, augmenting the dataset with additional information.

The subsequent section involves calculating distances between population points and the nearest health centers. Geographic coordinates are utilized to determine the proximity, and these results are integrated back into the population GeoDataFrame. The updated GeoDataFrame is persisted as a CSV file. Spatial join operations are extended to the chiefdom level, facilitating the computation of weighted average distances.

Normalization of health center counts and visualization are integral components of the code. The health center count is normalized, and heatmaps depicting health centers per 1000 population and under-5 population are generated. The ensuing analysis includes plotting average distances to the nearest health center per chiefdom.

Spatial analysis and visualization further enhance the insights derived from the data. Points within chiefdom polygons are identified through spatial joins, enabling the calculation of weighted average distances at the chiefdom level. Visualization efforts span from heatmaps showcasing average distances per chiefdom to customized maps illustrating the spatial distribution of points and health centers within specific chiefdoms.

As the code progresses, it undertakes tasks related to file reading and data cleaning. CSV files containing population and chiefdom data are read into DataFrames. Geometric information undergoes processing and conversion into appropriate GeoPandas formats.

The final segment delves into plotting and visualization, where various plots are generated to visually represent health center counts per 1000 population, under-5 population, and average distances per chiefdom. The creation of customized maps further enhances the interpretability of the data, providing insights into the spatial relationships between points, health centers, and chiefdoms.

## Results


| Cheifdom Name   |   Health Center Count |   u5 population |   Health Centers per 1000 |   Health Center Count Normalized |   Avg Distance |
|:----------------|----------------------:|----------------:|--------------------------:|---------------------------------:|---------------:|
| Neya            |                     7 |         4347.58 |                  1.61009  |                        0.0504202 |        4.96328 |
| Tambakha        |                     5 |         5885.6  |                  0.849532 |                        0.0336134 |        4.74312 |
| Dodo            |                     3 |         3073.32 |                  0.976144 |                        0.0168067 |        4.40525 |
| Banta Mokele    |                     3 |         1295.51 |                  2.31568  |                        0.0168067 |        4.17774 |
| Mongo           |                    11 |         5021.18 |                  2.19072  |                        0.0840336 |        3.70462 |

![Figure Label](Avg_Distance.jpg){#fig:1}
![Figure Label](pop.jpg)
![Figure Label](Healthcenter.jpg)

**Table 1: Insights on Chiefdoms and Health Center Distances**

Table 1 presents valuable insights into the average distances from different chiefdoms to health centers. Notably, Neya emerges with the longest average distance, spanning approximately 4.96 kilometers. The order of the top 5 chiefdoms with the longest average distances to health centers is as follows: Neya, Tambakha, Dodo, Banta Mokele, and Mongo. This ranking provides a clear understanding of the geographic distribution of healthcare accessibility, highlighting areas where populations face greater challenges in reaching health facilities.

**Figure 1: Average Distance Heat Map**

Figure 1 illustrates a heat map showcasing the average distances, measured in kilometers, from various locations to the nearest health center. The visualization reveals a spatial pattern, with a higher density of chiefdoms experiencing longer distances situated in the northern region. This geographical insight offers a visual representation of disparities in healthcare accessibility, guiding further exploration and intervention strategies in regions with pronounced challenges.

**Figure 2: Population Geolocation in Neya District**

Figure 2 provides a geospatial representation of population distribution within the Neya district. The visualization indicates that the population is more concentrated in the southern part of the district. This insight is crucial for understanding population density patterns, enabling targeted efforts in healthcare resource allocation and service delivery where the population is most dense.

**Figure 3: Health Centers in Neya District**

Figure 3 focuses on the distribution of health centers within the Neya district. The visualization clearly depicts the concentration of health centers in two distinct areas: the northwest and southeast of the district. This spatial arrangement provides insights into the accessibility of health services, suggesting that residents in these regions have relatively easier access to healthcare facilities. The visualization aids in identifying areas with potential gaps in healthcare infrastructure, informing strategic planning for additional health center placements.

These visual and tabular representations collectively contribute to a comprehensive understanding of the geographic dynamics related to healthcare accessibility, population distribution, and health center placement within the Neya district. The integration of such insights is crucial for informed decision-making in public health planning and resource allocation.

## Conclusion

The amalgamation of table insights and geospatial visualizations provides a nuanced understanding of healthcare accessibility, population distribution, and health center placement within the Neya district. These findings carry implications for strategic public health planning and resource allocation. The key takeaways from the analysis are summarized below.

**Healthcare Accessibility:**
The identification of Neya as having the longest average distance to health centers, reaching approximately 4.96 kilometers, underscores significant challenges in healthcare accessibility for residents in this chiefdom. The subsequent ranking of chiefdoms with longer average distances, including Tambakha, Dodo, Banta Mokele, and Mongo, emphasizes the need for targeted interventions to address geographical disparities in healthcare access [@doi:10.1080/00045608.2012.687349].

**Geospatial Disparities:**
The heat map in Figure 1 vividly illustrates the spatial distribution of average distances to health centers. The higher density of chiefdoms experiencing longer distances in the northern region signifies a geographical pattern of healthcare disparities. This insight aligns with existing research highlighting the role of geospatial analysis in identifying areas with reduced healthcare accessibility [@absRemotenessAreas]

**Population Distribution:**
Figure 2 provides a geospatial representation of population distribution within the Neya district. The concentration of population in the southern part of the district is a crucial demographic insight. This information is valuable for tailoring healthcare services to areas of higher population density, aligning with principles of equitable resource allocation [@taylorfrancisIntroductionSpatial].

**Health Center Placement:**
The distribution of health centers, as depicted in Figure 3, showcases concentrated placements in the northwest and southeast of the Neya district. This spatial arrangement suggests relatively better access to healthcare facilities for residents in these regions. The identification of such patterns aids in recognizing areas where healthcare infrastructure may require reinforcement to bridge potential gaps [@nihDevelopmentManagement].

In conclusion, the integration of table insights and geospatial visualizations provides a comprehensive view of the healthcare landscape in the Neya district. The identified disparities in healthcare accessibility and population distribution offer valuable inputs for evidence-based decision-making in public health planning. Addressing these geographic variations is essential to ensuring equitable healthcare services and improving health outcomes for all residents.

## Refrences 
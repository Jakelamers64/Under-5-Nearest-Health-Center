---
title: "Optimizing Access to Health Facilities for Under 5 Children: Assessing the Chiefdom with the Longest Average Distance"
author: Jacob Lamers
output: pdf_document
bibliography: bibliography.bib
csl: american-chemical-society.csl
documentclass: report
header-includes:
    - \usepackage{graphicx}
    - \usepackage{tabularx}
    - \usepackage{tabulary}
---

<!--
pandoc --citeproc -o paper.pdf paper.md
-->

<!--
TODO
- edit figure labels
- write results
- edit conculsion
- Read article
- cross check table values

DONE
- Find source intro
5/12
- cited article
- grammarly intro
- edit/grammarly methods
7/12
- fix pop distribution to show points by size
- make figure labels in latex
8/12
- convert table to latex table
- remove title from heat map
-->

## Introduction:

The intersection of geospatial data and public health research has become increasingly pivotal in recent years. As researchers and policymakers seek to address complex healthcare challenges, understanding the geographical distribution of health facilities and demographic patterns emerges as a cornerstone for effective planning and resource allocation. Geospatial analysis allows for a nuanced exploration of spatial relationships, offering insights that extend beyond traditional demographic studies. This analysis, often conducted through the lens of geographic information systems (GIS), has the potential to inform evidence-based decision-making and enhance the overall efficiency of healthcare systems[@0c2a1c700ec444a2884c74645fd06387]. Whether authoratively created or volnteer generated and asserted GIS systems can offer useful insights to assist in systems level descion making [@doi:10.1080/17538941003759255].

Nations frequently encounter obstacles in the integration of Geographic Information Systems (GIS). African countries, in particular, confront some of these challenges, each with its unique set of issues [@doi:10.1080/02693799108927829]. GRID3 stands out as an organization actively tackling these challenges across multiple African nations. In addition to generating datasets, such as those utilized in this analysis, GRID3 collaborates with the Ministry of Health (MOH) to enhance capabilities and establish sustainable GIS data practices in Sierra Leone [@grid3SierraLeones]. The data for health centers and population distribution used in this study was sourced from GRID3 [@grid3SierraLeone; @grid3GRID3Sierra].

The objective of the analysis presented here is to embark on a comprehensive geographic exploration, amalgamating third-level administrative geodata[@berkeleyBerkeleyGeoData], health center geodata[@grid3SierraLeone], and population estimates[@grid3GRID3Sierra]. This multifaceted approach seeks to uncover intricate patterns in health center distribution, population demographics, and accessibility within specific geographical regions. By combining diverse datasets and employing spatial analysis techniques, this study aims to contribute to the growing body of knowledge that leverages geospatial insights for public health enhancement.

## Methods

### Data Processing

The provided code encompasses a multifaceted data processing pipeline. In the initial phase, the code focuses on data acquisition and processing. Third-level administrative geodata, health center geodata, and georefrenced population estimate data were all obtained for futher analysis. The code leverages the GeoPandas library to manipulate the third-level administrative geodata and health center geodata. Spatial operations were performed to associate health centers with specific districts. The resulting GeoDataFrame captures the count of health centers within each district, contributing to a comprehensive understanding of their distribution.

The population data processing section involves reading data from GeoTIFF files. This DataFrame encapsulates pixel coordinates as points and their corresponding population values. Age and gender-specific DataFrames are created, eventually merged into a unified GeoDataFrame containing the under-5 population at each georefrenced point. This population count was computed through grouping based on spatial geometry.

Straight line distance was then calculated to every health center for each pixel containing under-5 population count greater than one. The distance to the nearest health center was then stored along with the name of that health center. Geographic coordinates were utilized to determine the proximity. 

### Visualizaton

The ensuing analysis includes calculating and plotting weighted average distances to the nearest health center per chiefdom. A heat map was generated showing this average distance. A table was also generated displaying the five cheifdoms with the longest average distance. This table also displays relevent values for these calculations.

Spatial analysis and visualization further enhance the insights derived from the data. Population within the chiefdom of Neya wass visualized. Customized maps illustrating the spatial distribution of populatons and health centers within the chiefdom.

## Results

\begin{table}[h]
    \centering
    \begin{tabulary}{\textwidth}{LCCCCC}
        \hline
        Cheifdom Name & Health Center Count & Health Centers per 1000 U5 & Avg Distance \\
        \hline
        Neya & 7 & 1.61009 & 4.96328 \\
        Tambakha & 5 & 0.849532 & 4.74312 \\
        Dodo & 3 & 0.976144 & 4.40525 \\
        Banta Mokele & 3 & 2.31568 & 4.17774 \\
        Mongo & 11 & 2.19072 & 3.70462 \\
        \hline
    \end{tabulary}
    \caption{presents valuable insights into the average distances from different chiefdoms to health centers.}
    \label{tab:results_table}
\end{table}

\begin{figure}
    \centering
    \textbf{Average Distance Heat Map}\par\medskip
    \includegraphics[width=\linewidth]{Avg_Distance.png}
    \caption{
        Illustrates a heat map showcasing the weighted average straight line distances, measured in kilometers, from various under 5 population centers to the nearest health center.
        }
    \label{fig:Avg_Distance}
\end{figure}

\begin{figure}
    \centering
    \textbf{Health Center and Under 5 Population Distribution in Neya District}\par\medskip
    \includegraphics[width=\linewidth]{High_resoltion.png}
    \caption{
        Provides a geospatial representation of population distribution within the Neya district. And the distribution of health centers within the Neya district.
        }
    \label{fig:High_resoltion}
\end{figure}

In \ref{tab:results_table} Notably, Neya emerges with the longest average distance, spanning approximately 4.96 kilometers. The order of the top 5 chiefdoms with the longest average distances to health centers is as follows: Neya, Tambakha, Dodo, Banta Mokele, and Mongo. This ranking provides a clear understanding of the geographic distribution of healthcare accessibility, highlighting areas where populations face greater challenges in reaching health facilities.

The visualization reveals a spatial pattern, with a higher density of chiefdoms experiencing longer distances situated in the northern region. This geographical insight offers a visual representation of disparities in healthcare accessibility, guiding further exploration and intervention strategies in regions with pronounced challenges.

<!--
**Figure 2: Population Geolocation in Neya District**

Figure 2  The visualization indicates that the population is more concentrated in the southern part of the district. This insight is crucial for understanding population density patterns, enabling targeted efforts in healthcare resource allocation and service delivery where the population is most dense.

**Figure 3: **

Figure 3 focuses  The visualization clearly depicts the concentration of health centers in two distinct areas: the northwest and southeast of the district. This spatial arrangement provides insights into the accessibility of health services, suggesting that residents in these regions have relatively easier access to healthcare facilities. The visualization aids in identifying areas with potential gaps in healthcare infrastructure, informing strategic planning for additional health center placements.

These visual and tabular representations collectively contribute to a comprehensive understanding of the geographic dynamics related to healthcare accessibility, population distribution, and health center placement within the Neya district. The integration of such insights is crucial for informed decision-making in public health planning and resource allocation.

-->

## Conclusion

<!--
Limitations
- straightline distance
-->

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

## Acknowledgments 

ChatGPT was used extensively in code creation and manuscript writing.

## Refrences 
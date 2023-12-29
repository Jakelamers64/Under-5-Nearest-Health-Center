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
9/12
- edit figure labels
- write results
- cross check table values
10/12
- edit conculsion
11/12
22/12
- Fixed some sources
- Read articles
- Ensure accuracy of all citations
12/12
- grammarly everything
-->

## Introduction:

The intersection of geospatial data and public health research has become increasingly pivotal in recent years. As researchers and policymakers seek to address complex healthcare challenges, understanding the geographical distribution of health facilities and demographic patterns emerges as a cornerstone for effective planning and resource allocation. Geospatial analysis allows for a nuanced exploration of spatial relationships, offering insights that extend beyond traditional demographic studies. This analysis, often conducted through the lens of geographic information systems (GIS), has the potential to inform evidence-based decision-making and enhance the overall efficiency of healthcare systems[@0c2a1c700ec444a2884c74645fd06387]. Whether authoritatively created or volunteer generated and asserted GIS systems can offer useful insights to assist in systems-level decision making [@doi:10.1080/17538941003759255].

Nations frequently encounter obstacles in the integration of Geographic Information Systems (GIS). African nations often face distinctive challenges when implementing these systems[@doi:10.1080/02693799108927829]. GRID3 stands out as an organization actively tackling these challenges across multiple African nations. In addition to generating datasets, such as those utilized in this analysis, GRID3 collaborates with the Ministry of Health (MOH) to enhance capabilities and establish sustainable GIS data practices in Sierra Leone [@grid3SierraLeones]. The data for health centers and population distribution used in this study was sourced from GRID3 [@grid3SierraLeone; @grid3GRID3Sierra].

The objective of the analysis presented here is to embark on a comprehensive geographic exploration, amalgamating third-level administrative geodata[@berkeleyBerkeleyGeoData], health center geodata[@grid3SierraLeone], and population estimates[@grid3GRID3Sierra]. This multifaceted approach seeks to uncover intricate patterns in health center distribution, population demographics, and accessibility within specific geographical regions. By combining diverse datasets and employing spatial analysis techniques, this study aims to contribute to the growing body of knowledge that leverages geospatial insights for public health enhancement.

## Methods

### Data Processing

The provided code encompasses a multifaceted data processing pipeline. In the initial phase, the code focuses on data acquisition and processing. Third-level administrative geodata, health center geodata, and georeferenced population estimate data were all obtained for further analysis. The code leverages the GeoPandas library to manipulate the third-level administrative geodata and health center geodata. Spatial operations were performed to associate health centers with specific districts. The resulting GeoDataFrame captures the count of health centers within each district, contributing to a comprehensive understanding of their distribution.

The population data processing section involves reading data from GeoTIFF files. This data frame encapsulates pixel coordinates as points and their corresponding population values. Age and gender-specific data frames are created and eventually merged into a unified GeoDataFrame containing an under-5 population at each georeferenced  point. This population count was computed through grouping based on spatial geometry.

Straight line distance was then calculated to every health center for each pixel containing under-5 population count greater than one. The distance to the nearest health center was then stored along with the name of that health center. Geographic coordinates were utilized to determine the proximity. 

### Visualization

The ensuing analysis includes calculating and plotting weighted average distances to the nearest health center per chiefdom. A heat map was generated showing this average distance. A table was also generated displaying the five chiefdoms with the longest average distance. This table also displays relevant values for these calculations.

Spatial analysis and visualization further enhance the insights derived from the data. The population within the chiefdom of Neya was visualized. Customized maps illustrating the spatial distribution of populations and health centers within the chiefdom.

## Results

\begin{table}[h]
    \centering
    \begin{tabulary}{\textwidth}{LCCCCC}
        \hline
        Chiefdom Name & Health Center Count & Health Centers per 1000 U5 & Avg Distance \\
        \hline
        Neya & 7 & 1.61009 & 4.96328 \\
        Tambakha & 5 & 0.849532 & 4.74312 \\
        Dodo & 3 & 0.976144 & 4.40525 \\
        Banta Mokele & 3 & 2.31568 & 4.17774 \\
        Mongo & 11 & 2.19072 & 3.70462 \\
        \hline
    \end{tabulary}
    \caption{
        This showcases the five districts with the lengthiest average straight-line distance, measured in kilometers. Additionally, it provides relevant data points for calculating this distance, including the number of health centers and their respective counts per 1000 individuals under the age of 5.
        }
    \label{tab:results_table}
\end{table}

\begin{figure}
    \centering
    \textbf{Average Distance Heat Map}\par\medskip
    \includegraphics[width=\linewidth]{Avg_Distance.png}
    \caption{
        This figure illustrates a heat map displaying the weighted average straight-line distances, measured in kilometers, from various under-5 population centers to the nearest health center in each chiefdom in Sierra Leone.
        }
    \label{fig:Avg_Distance}
\end{figure}

\begin{figure}
    \centering
    \textbf{Health Center and Under 5 Population Distribution in Neya District}\par\medskip
    \includegraphics[width=\linewidth]{High_resoltion.png}
    \caption{
        This figure provides a geospatial representation of the distribution of the under-5 population within the Neya district, which has the longest average distance among the districts. It also depicts the distribution of health centers (black squares) serving the under-5 population within the Neya district.
        }
    \label{fig:High_resoltion}
\end{figure}

The results of our study, as presented in Table \ref{tab:results_table}, highlight the five chiefdoms in Sierra Leone with the most extensive average straight-line distances, measured in kilometers. Notably, Tambakha and Dodo chiefdoms emerge with fewer health centers per 1000 individuals under the age of 5 compared to other districts on the list. Despite Neya chiefdom having a relatively higher count of health centers per 1000 under-fives, it still manages to have the longest average distance among the districts, indicating an interplay between healthcare accessibility and geographical factors.

Figure \ref{fig:Avg_Distance} provides a comprehensive visualization of the weighted average straight-line distances from various under-5 population centers to the nearest health center in each chiefdom across Sierra Leone. The northern regions, particularly Neya chiefdom in the northeast, exhibit a concentration of longer distances, underscoring the geographical disparities in healthcare accessibility.

Zooming in on Neya chiefdom in Figure \ref{fig:High_resoltion}, our geospatial representation reveals a qualitative distribution of the under-5 population, emphasizing the east-central region as having the longest average distances. Additionally, the presence of a main road in the west portion of the chiefdom is notable. While not directly addressed in the quantitative data, this road likely plays a significant role in reducing the actual distances traveled, suggesting that the straight-line distances presented may underestimate the true challenges faced by the population in accessing healthcare.

## Conclusion

The identification of Neya chiefdom as having the longest average distance to health centers, reaching approximately 4.96 kilometers, underscores challenges in healthcare accessibility for residents in this particular region. This finding highlights the need for targeted interventions to address geographical disparities in healthcare access, especially in areas where the population faces substantial obstacles in reaching essential health services. The ranking of chiefdoms with longer average distances, including Tambakha, Dodo, Banta Mokele, and Mongo, further expands on the situation, emphasizing the importance of devising strategies to improve healthcare infrastructure and reduce the burden on communities with limited access.

The heat map presented in Figure \ref{fig:Avg_Distance} illustrates the spatial distribution of average distances to health centers across chiefdoms in Sierra Leone. The higher density of chiefdoms experiencing longer distances in the northeastern region signifies a geographical pattern of healthcare disparities. This insight aligns with existing research, emphasizing the crucial role of geospatial analysis in identifying areas with reduced healthcare accessibility[@0c2a1c700ec444a2884c74645fd06387]. The ability to pinpoint specific regions facing greater challenges facilitates the formulation of targeted policies and interventions to mitigate these disparities effectively.

Zooming in on Neya chiefdom in Figure \ref{fig:High_resoltion}, our geospatial representation offers a qualitative distribution of the under-5 population, emphasizing the east-central region as having the longest average distances. Notably, the presence of a main road in the west portion of the chiefdom, although not explicitly addressed in the quantitative data, likely plays a significant role in reducing the actual distances traveled by residents seeking healthcare. This suggests that the straight-line distances presented may not accurately reflect the true challenges faced by the population in accessing healthcare, emphasizing the need for a more nuanced understanding of the interaction between geographical factors and healthcare accessibility. Recognizing such patterns is essential for identifying areas where healthcare infrastructure may require reinforcement to bridge potential gaps [@0c2a1c700ec444a2884c74645fd06387].

While these findings contribute valuable insights, it is important to acknowledge certain limitations. The use of straight-line distance may oversimplify the actual travel experience; the predominantly qualitative and descriptive nature of the analysis calls for a more robust quantitative approach. Additionally, the grouping of both government and private healthcare infrastructure ignores the accessibility of private versus government health facilities based on economic considerations. Future research directions could include a frequency distribution analysis to determine which health centers are driving the longest distance in Neya Chiefdom, a disaggregation of private and government health facilities, the introduction of statistical tests for comparisons of average distance, and cluster analysis to identify optimal locations for future health centers. These enhancements would further refine our understanding of healthcare accessibility challenges and contribute to the development of more effective interventions to address them.

## Acknowledgments 

ChatGPT was used extensively in code creation and manuscript writing.

## Refrences 
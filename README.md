# Abaqus-Documentation-Scraper
Script to extract keywords, parameters, and parameter values from the Abaqus HTML documentation. This script is used to generate the lists used for this [Sublime Text syntax highlighting plugin](https://github.com/bendeaton/Abaqus-Sublime). You need to have Abaqus installed and the documentation locally accessible for this to work.

## To Do

The Abaqus HTML Keyword Manual is defined in such a way that the keywords, parameters, and parameter values are called out specifically by CSS tags. Other items which are needed are not identified by the CSS in this way. These items are typically presented in tables in the Analysis Manual and could probably be identified by context, but I haven't had time to do it yet.

* Element types
* Load types
* Output types
* Probably many others

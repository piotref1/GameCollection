# GameCollection
Modules of inventory system created around the need of game collectors.

Current modules:

-Steam - Reacreation of STEAM API without relying on provided code for using it.
Scraping data from Steam website to get list of games, genres, achievements and time spent in games.
In addition it creates lists of suggestion for games to buy, finish, play and sends emails if user spent too much time in games (depending on set amount of hours)

Fixes required:

-Change all SQL inserts to do batch inserts rather than single inserts. Some are done this way at the moment due to issues while coding in batch ones.

-Fix frontend. Or better yet scrape what is there now and create new one. With paging. One that also would show only available modules.

-Figure out better email sending. Security issues galore with current flat text login stored information. 

-Check how many requests can be done to Steam servers before being blocked. Would allow to speed up the code, running processes in parallel rather than sequentiall for all users.



Future modules:

-User module - Login/Registration. Can it be done without need for logging in? Yes. But no way of changing your data by yourself so it's a must.

-Nintendo module - No scraping is available. Crud module for adding games manually thorough all generations of Nintendo consoles. In addition ability to add
hardware like consoles, controllers to list of collected items.

-Xbox - As above.

-Sony - Some scraping is available. Due to discrepancies between given data and real world it would include field "Owned" as Sony saves what was played rather than owned.
Some games would need to be manually adjusted in regards to that or manually added to the list.

-Origin/Uplay/etc - Needs research if there's any publicly available API or data source. Otherwise general crud module

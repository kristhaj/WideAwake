# WideAwake

Pekkas mystery method

WideAwake is a database-system made for warning drivers in the local area about slippery roads and other obstacles that other drivers have experienced in the same area. The product is developed by a group of students at the Norwegian University of Science and Technology (NTNU) in Trondheim, Norway. 

The system uses a Raspberry Pi 2 that collects information from the car computer when systems, such as ABS-breaks and anti-spin, activates, and sends the information, along the car location to the database. The database will then send the information to other cars with the WideAwake-system in the same local area that warns them to be carefull and/or avoid that specific location. If the system has no connection with the database, it will still function in an "offline" mode, that still record slippery roads and the cars position. All data will be uploaded to the database when the system reconnects.  

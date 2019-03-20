SELECT restaurants.NAME, neighborhoods.NAME 

	FROM neighborhoods 
	JOIN restaurants 
	ON neighborhoods.ID=restaurants.neighborhoods_ID


# Data Science - Final Group Project

![image](https://web-static.wrike.com/blog/content/uploads/2019/05/API-Wrike-.jpg?av=8d387ac3ad145fbd322ff0d641cd1124)

The following project consist in an API with multiple endpoints that return information regarding walking and bicycle routes of Valencia, Spain.

## INDEX

- [Technologies 🕹](#technologies)
- [Parts of the Project ⚙](#parts-of-the-project)
	- [Data Acquisition](#data-acquisition)
	- [Data Cleaning](#data-cleaning)
	- [Model Creation](#model-creation)
	- [Heroku App](#heroku-app)
- [Contributors](#contributors)

## Technologies

- `Python`: Python is a high-level, interpreted, general-purpose programming language
- `Heroku`: cloud platform as a service supporting several programming languages
- `PostgreSQL`:  relational database management system emphasizing extensibility and SQL compliance
- `Typeform`: online form building and online surveys. Its main software creates dynamic forms based on user needs.

## Parts of the Project

### Data Acquisition

We need two tables, one containing information of the 24 routes and another one the information of the respective points of interest for each route. This criteria comes from this [web](https://cultural.valencia.es/es/rutas/) of the city hall of Valencia.

So we scrapped the vast majority of the data from the [web](https://cultural.valencia.es/es/rutas/) just mentioned, in order to do this we use ```Beautiful Soup``` as our main to tool for scrapping both the web and the kmls containing the points of interest information.

On the other hand, we also gathered users preferences on their type of route by creating a form using `Typeform`, at the end we reached 74 forms filled over the span of a week.

### Data Cleaning

Having done the acquisition of the data the next we did was the data cleaning and adding some columns; for example filling Nan values, stripping spaces from categories, translating columns to valencian, spanish and english.

After all the cleaning, the final csv are `routes.csv` and `poi.csv`.

### Model Creation

With those 74 forms that haven been filled, we created up to 30000 synthetic data to train the model properly, giving the best score the MLP (Multi Layer Perceptron) model with an accuracy of 0.935

### Heroku App

The final part of the project, practically speaking the implementation of all the previous steps.

The APi consist of 6 endpoints in total, 5 gets and 1 post.

The first 2 are self explanatory, return all the routes or points of interest: 
- https://api-routes-data.herokuapp.com/getRoutes/
- https://api-routes-data.herokuapp.com/getPoi/

The next 2, you have to specify a id at the end of the url, for example `https://api-routes-data.herokuapp.com/getRouteById/?id=13`. The max value for id is **24 for the routes** and **293 for the poi (points of interest)**.
- https://api-routes-data.herokuapp.com/getRouteById/
- https://api-routes-data.herokuapp.com/getPoiById/

This endpoint employ the model we created, returning a recommended route, by default it returns the id of the route 15. You have to pass it the following parameters to return a different route:  age, gender, time, route_type, price, difficulty, companions, transport, time_stamp.

- https://api-routes-data.herokuapp.com/getRecommendation/

The last endpoint, need the same parameters has the previous one and returns an user id of the one that just has been created:
- https://api-routes-data.herokuapp.com/postUser/

## Contributors

- [@parismart](https://github.com/parismart)
- [@Ismaelpbla](https://github.com/Ismaelpbla)
- [@Gabox29](https://github.com/Gabox29)
- [@Rafipaulino](https://github.com/Rafipaulino)
- [@Germanga2001](https://github.com/Germanga2001)

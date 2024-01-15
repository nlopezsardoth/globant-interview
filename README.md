# globant-interview

#### Clone the project

Open your terminal and navigate to directory where you want to clone the repository:

```shell
cd folder/to/clone/
git clone git@github.com:nlopezsardoth/globant-interview.git
```

#### Set enviroment variables

Create a `.env` file containing 

```shell
API_KEY=your-api-key 
```
from OpenWeather https://openweathermap.org/


#### Run local docker

```shell
docker-compose up -d globant_interview
docker-compose build
docker-compose up globant_interview
```

### get weather results
Open `http://127.0.0.1:4000/weather?city=medellin&country=co` in browser or postman


#### Run tests
add `TEST_API_KEY` in  `.env`

```shell
TEST_API_KEY=your-test-api-key 
```
from OpenWeather https://openweathermap.org/

test are ubicated in `app/weather/tests` go to that folder and run a test using  `pytest `

```shell
pytest test_get_weather_data.py
```



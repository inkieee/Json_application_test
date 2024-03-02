# Json_application_test

# Code Structure
    main.py
        ApiKeyProvider (obtains api key)
        WeatherClient (obtains weather data for cityh)
        InsertRedisData (Inserts data into Redis)
        PlotCityWeather (matplot libs plots)
        SortCityTemp (Sorts city temperatures)
        FindCitiesBelowAvgTemp (Calculates avg temperature, finds cities below that)
    
# Requires:
    Installed in environment:
        PyMySQL==1.1.0
        redis==5.0.1
        python-dotenv==1.0.0
        PyYAML==6.0
        black
        matplotlib

    Running Redis-Stack-Server (for RedisJSON)

    An Openweathermap api key
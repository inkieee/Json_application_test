

# obtain api

# obtain cities to do something with
# read from file maybe

# put cities into memory

# instantiate a api object to store api data
# for city in list
#   city_data = object_that_instantiation_results_in_call_to_obtain_data, and puts into redis
#       //so this object is;
#       //  get api data for city
#       //  put that data into redis
#       //  destroy object
#   // now you have a lot of objects with data per city
#   //does it make sense to put this data into objects here?
#   //for what?, maybe make objects in redis

# for city_object in objects in redis
#   do some outputs
#       1. plot city, temperature
#       2. maybe graph?
#       3. calculate tempeartures in varying scales

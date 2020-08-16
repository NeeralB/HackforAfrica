from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def index():

    
    return render_template("advice.html")

@app.route("/ml", methods = ["POST"])
def ml():
    message = ""
    msg11 = request.form.get("name1")
    msg1 = int(msg11)
    msg22 = request.form.get("name2")
    msg2 = int(msg22)
    msg33 = request.form.get("name3")
    msg3 = int(msg33)
    msg44 = request.form.get("name4")
    msg4 = int(msg44)
    msg55 = request.form.get("name5")
    msg5 =  int(msg55)

    import pandas as pd
    import numpy as np
    import sklearn
    from sklearn import linear_model
    from sklearn.utils import shuffle

    data = pd.read_csv("student-mat.csv", sep=";")
    # Since our data is seperated by semicolons we need to do sep=";"

    #print(data.head())  #first 5 elements
    #factors we want
    data = data[["trees", "animals", "G3", "landsize", "avgtemp", "time"]]



    predict = "G3"

    X = np.array(data.drop([predict], 1)) # Features #what we are using to predict
    y = np.array(data[predict]) # Labels what we  want to predict

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1) #testing 0.1 so 10%, 90% training

    ## linear regressin
    linear = linear_model.LinearRegression() # the model used

    # Train and score our model
    linear.fit(x_train, y_train)
    #acc = linear.score(x_test, y_test) # acc stands for accuracy 
    #print(acc)  #accuracy

    #The constants generating the linear regression line
    #print('Coefficient: \n', linear.coef_) # These are each slope value
    #print('Intercept: \n', linear.intercept_) # This is the intercept


    predictions = linear.predict(x_test) # Gets a list of all predictions
    ## Printing out all the actual info
    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    ## Predicting a value
    #x = int(input("Enter some factors"))
    prediction1 = linear.predict([[msg1, msg2, msg3, msg4, msg5]])
    if prediction1 < 15:
        message = "Firstly, congrats on growing your garden! By doing this you are not only saving the Earth but also providing beauty to the world! Based on the machine learning algorithm, one way to expand your garden is to plant as much as you can. Make sure to water it gets watered daily, and that it is safe. Also try to have animals such as cows and goats roam on your land. Their manure greatly helps the soil as it makes it rich and fertile. Try to also use the Stone Circle Strategy as it seems like one of your issues is erosion of the soil. The stone circle strategy allows for you to place big stones in circles around bits of land so that any eroded soil will be blocked from leaving the land by the stones. Hope this helps!"
    else:
        message = "Firstly, congrats on growing your garden! By doing this you are not only saving the Earth but also providing beauty to the world! Based on the machine learning algorithm, one way to expand your garden is to plant less in concentrated areas. This way the plants will have less competition and can all thrive in your environment. Make sure to also buy an irrigation system as it will be very helpful in relieving work when there is too many plants to handle. Lastly, make sure to not have too many animals on the land. Although their manure makes the soil more fertile. With more and more animals, the soil starts to become loose as the animals causes breakages in the ground and make the roots loose.Hope this helps! "
    print(prediction1)
    print(message)
    return render_template("byte.html", message = message)
    

    
    return render_template("byte.html", message = message)



@app.route("/strategies", methods = ["POST"])
def covid():
    msg = ""
    msg1 = ""
    msg2 = ""
    msg3 = ""
    msg4 = ""
    msg5 = ""
    msg6 = ""
    msg7 = ""
    msg8 = ""
    name1 = request.form.get("name1")
    name2 = request.form.get("name2")
    name3 = request.form.get("name3")
    name4 = request.form.get("name4")
    name5 = request.form.get("name5")

    if name1 == "STRAT1":
        msg = "Awesome Choice! Planting trees is a sustainable practice and has a long lasting impact on the environment. "
        msg1 = "One of the best ways to manage soil is by planting more trees. Planting trees firstly is great for the environment as the roots of the trees compact soil and this reduces soil erosion from wind or water. "
        msg2 = "To start off, make sure to get the seeds for a tree that can survive well in the desert. This means that it is more independent than other trees which need more water or sunlight. Examples can include acacia trees, banyans, etc."
        msg3 = "Make sure that you research which trees to buy, as there are some trees who are not accustomed to living in the hot climate area and will not sprout."
        msg4 = "Plant the seeds in an open place. Where there is lots of space and no competition against other plants. Your garden has now begun. If you have the money, buy or make an irrigation system that will add controlled amounts of water to the land automatically."
        msg5 = "Save your water and use it to water the plants during the dry season. Nothing to worry about during the rainy season as the rain will make the plants wet. This is the better water management system.." 
        msg6 = "If you do not want to use plants, you can use the stone circle strategy where u keep big stones around many parts of the land so the soil never escapes. "
        msg7 = "Additionally, Make sure to minimize the amount of animals on the land as this may cause overgrazing and make the soil less compact. However, it is important to also some animals on the land as their manure makes the soil rich. This allows for the plants to be healthy and grow faster."
        msg8 = "Once again thank you for helping the community in Africa. You are one of the unsung heroes promoting the environment and helping out others all over the world."
        msg9 = "Thank you so much and have fun! If you need any funds make sure to visit our donate page or write a blog and share pictures about how your garden is going!"
    
    if name2 == "STRAT2":
        msg = "Awesome Choice! Managing the Quality of Soil Strategies are sustainable practices and has a long lasting impact on the environment. "
        msg1 = "One of the best ways to manage soil is by planting more trees. Planting trees firstly is great for the environment as the roots of the trees compact soil and this reduces soil erosion from wind or water. "
        msg2 = "To start off, make sure to get the seeds for a tree that can survive well in the desert. This means that it is more independent than other trees which need more water or sunlight. Examples can include acacia trees, banyans, etc."
        msg3 = "Make sure that you research which trees to buy, as there are some trees who are not accustomed to living in the hot climate area and will not sprout."
        msg4 = "Plant the seeds in an open place. Where there is lots of space and no competition against other plants. Your garden has now begun. If you have the money, buy or make an irrigation system that will add controlled amounts of water to the land automatically."
        msg5 = "Save your water and use it to water the plants during the dry season. Nothing to worry about during the rainy season as the rain will make the plants wet. This is the better water management system.." 
        msg6 = "If you do not want to use plants, you can use the stone circle strategy where u keep big stones around many parts of the land so the soil never escapes. "
        msg7 = "Additionally, Make sure to minimize the amount of animals on the land as this may cause overgrazing and make the soil less compact. However, it is important to also some animals on the land as their manure makes the soil rich. This allows for the plants to be healthy and grow faster."
        msg8 = "Once again thank you for helping the community in Africa. You are one of the unsung heroes promoting the environment and helping out others all over the world."
        msg9 = "Thank you so much and have fun! If you need any funds make sure to visit our donate page or write a blog and share pictures about how your garden is going!"
    
    if name3 == "STRAT3":
        msg = "Awesome Choice! The  Better Water Management strategy is a sustainable practice and has a long lasting impact on the environment. "
        msg1 = "One of the best ways to manage soil is by planting more trees. Planting trees firstly is great for the environment as the roots of the trees compact soil and this reduces soil erosion from wind or water. "
        msg2 = "To start off, make sure to get the seeds for a tree that can survive well in the desert. This means that it is more independent than other trees which need more water or sunlight. Examples can include acacia trees, banyans, etc."
        msg3 = "Make sure that you research which trees to buy, as there are some trees who are not accustomed to living in the hot climate area and will not sprout."
        msg4 = "Plant the seeds in an open place. Where there is lots of space and no competition against other plants. Your garden has now begun. If you have the money, buy or make an irrigation system that will add controlled amounts of water to the land automatically."
        msg5 = "Save your water and use it to water the plants during the dry season. Nothing to worry about during the rainy season as the rain will make the plants wet. This is the better water management system.." 
        msg6 = "If you do not want to use plants, you can use the stone circle strategy where u keep big stones around many parts of the land so the soil never escapes. "
        msg7 = "Additionally, Make sure to minimize the amount of animals on the land as this may cause overgrazing and make the soil less compact. However, it is important to also some animals on the land as their manure makes the soil rich. This allows for the plants to be healthy and grow faster."
        msg8 = "Once again thank you for helping the community in Africa. You are one of the unsung heroes promoting the environment and helping out others all over the world."
        msg9 = "Thank you so much and have fun! If you need any funds make sure to visit our donate page or write a blog and share pictures about how your garden is going!"


    if name4 == "STRAT4":
        msg = "Awesome Choice! The  Stone Circle strategy is a sustainable practice and has a long lasting impact on the environment. "
        msg1 = "One of the best ways to manage soil is by planting more trees. Planting trees firstly is great for the environment as the roots of the trees compact soil and this reduces soil erosion from wind or water. "
        msg2 = "To start off, make sure to get the seeds for a tree that can survive well in the desert. This means that it is more independent than other trees which need more water or sunlight. Examples can include acacia trees, banyans, etc."
        msg3 = "Make sure that you research which trees to buy, as there are some trees who are not accustomed to living in the hot climate area and will not sprout."
        msg4 = "Plant the seeds in an open place. Where there is lots of space and no competition against other plants. Your garden has now begun. If you have the money, buy or make an irrigation system that will add controlled amounts of water to the land automatically."
        msg5 = "Save your water and use it to water the plants during the dry season. Nothing to worry about during the rainy season as the rain will make the plants wet. This is the better water management system.." 
        msg6 = "If you do not want to use plants, you can use the stone circle strategy where u keep big stones around many parts of the land so the soil never escapes. "
        msg7 = "Additionally, Make sure to minimize the amount of animals on the land as this may cause overgrazing and make the soil less compact. However, it is important to also some animals on the land as their manure makes the soil rich. This allows for the plants to be healthy and grow faster."
        msg8 = "Once again thank you for helping the community in Africa. You are one of the unsung heroes promoting the environment and helping out others all over the world."
        msg9 = "Thank you so much and have fun! If you need any funds make sure to visit our donate page or write a blog and share pictures about how your garden is going!"
    
    if name5 == "STRAT5":
        msg = "Awesome Choice! The Irrgation System strategy is a sustainable practice and has a long lasting impact on the environment. "
        msg1 = "One of the best ways to manage soil is by planting more trees. Planting trees firstly is great for the environment as the roots of the trees compact soil and this reduces soil erosion from wind or water. "
        msg2 = "To start off, make sure to get the seeds for a tree that can survive well in the desert. This means that it is more independent than other trees which need more water or sunlight. Examples can include acacia trees, banyans, etc."
        msg3 = "Make sure that you research which trees to buy, as there are some trees who are not accustomed to living in the hot climate area and will not sprout."
        msg4 = "Plant the seeds in an open place. Where there is lots of space and no competition against other plants. Your garden has now begun. If you have the money, buy or make an irrigation system that will add controlled amounts of water to the land automatically."
        msg5 = "Save your water and use it to water the plants during the dry season. Nothing to worry about during the rainy season as the rain will make the plants wet. This is the better water management system.." 
        msg6 = "If you do not want to use plants, you can use the stone circle strategy where u keep big stones around many parts of the land so the soil never escapes. "
        msg7 = "Additionally, Make sure to minimize the amount of animals on the land as this may cause overgrazing and make the soil less compact. However, it is important to also some animals on the land as their manure makes the soil rich. This allows for the plants to be healthy and grow faster."
        msg8 = "Once again thank you for helping the community in Africa. You are one of the unsung heroes promoting the environment and helping out others all over the world."
        msg9 = "Thank you so much and have fun! If you need any funds make sure to visit our donate page or write a blog and share pictures about how your garden is going!"



    return render_template("strategiesreroute.html", name1 = name1, name2 = name2, name3 = name3, name4 = name4, name5 = name5, msg = msg, msg1 =msg1, msg2 = msg2, msg3 = msg3, msg4 = msg4, msg5 = msg5, msg6 = msg6, msg7 = msg7, msg8 = msg8)

@app.route("/d")
def index1():
    import folium
    m = folium.Map(location=[15.454166,18.732206], tiles="Stamen Terrain", zoom_start=5)
    for i in range(1):
        import folium
        m = folium.Map(location=[15.454166,18.732206], tiles="Stamen Terrain", zoom_start=5)
        #Chad
        folium.Marker(location=[12.023559,18.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.023559,20.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[13.023559,19.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.023559,15.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[12.023559,16.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[21.023559,17.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[20.023559,15.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[19.023559,17.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[18.023559,21.906193], popup="<strong>Desertificated Areas with high risk in Chad</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[11.023559,17.906193], popup="<strong>Desertificated Areas with low risk in Chad</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[13.023559,19.906193], popup="<strong>Desertificated Areas with medium to low risk in Chad</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        
        #Niger
        #folium.Marker(location=[-13.813930,10.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-13.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-15.813930,10.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-14.813930,10.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-18.813930,12.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-16.813930,6.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-11.813930,14.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)
        #folium.Marker(location=[-14.813930,13.540200], popup="<strong>Desertificated Areas with high risk in Niger</strong>", tooltip="Click for more information").add_to(m)

        #Angola
        folium.Marker(location=[-23.813930,35.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-23.813930,35.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-22.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-24.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-22.813930,33.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-21.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-21.813930,33.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-23.813930,32.540200], popup="<strong>Desertificated Areas with high risk in Angola</strong>", tooltip="Click for more information").add_to(m)

        #Sierra Leone
        folium.Marker(location=[7.813930,5.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[9.813930,5.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[5.813930,8.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,7.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,4.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[9.813930,3.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.813930,7.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[4.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Sierra Leone</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[4.23559,3.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        
        #Ethiopia
        folium.Marker(location=[8.813930,39.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[9.813930,39.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[8.813930,40.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,40.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,40.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[9.813930,41.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.813930,42.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[6.813930,41.540200], popup="<strong>Desertificated Areas with high risk in Ethiopia</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[6.23559,43.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)

        #Djibouti
        folium.Marker(location=[14.813930,15.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,17.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,15.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,18.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[17.813930,19.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[16.813930,20.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[15.813930,12.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,16.540200], popup="<strong>Desertificated Areas with high risk in Djibouti</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[18.23559,16.906193], popup="<strong>low risk Desertificated Areas in Djibouti</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        #Guinea
        folium.Marker(location=[9.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[9.813930,8.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[8.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,6.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.813930,11.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.813930,12.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[6.813930,9.540200], popup="<strong>Desertificated Areas with high risk in Guinea</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[7.23559,6.906193], popup="<strong>low risk Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="envelope", color="green")).add_to(m)

        #Sudan
        folium.Marker(location=[12.813930,30.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[12.813930,31.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[13.813930,30.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,31.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[15.813930,32.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[14.813930,32.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[15.813930,29.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[16.813930,28.540200], popup="<strong>Desertificated Areas with high risk in Sudan</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[16.23559,27.906193], popup="<strong>Desertificated Areas in Sudan</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        #Brazzavile
        folium.Marker(location=[-3.540200,15.45], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-4.54020,15.768], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-4.813930,15.540200], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-5.813930,16.540200], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-5.813930,14.540200], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-3.813930,15.540200], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-2.813930,17.540200], popup="<strong>Desertificated Areas with high risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-6.813930,18.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        #folium.Marker(location=[-6.23559,.906193], popup="<strong>Desertificated Areas in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        folium.Marker(location=[-3.540200,17.45], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-4.54020,18.768], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-4.813930,17.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-5.813930,16.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-5.813930,18.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-3.813930,18.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-2.813930,19.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-6.813930,16.540200], popup="<strong>Desertificated Areas with low risk in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-6.23559,17.906193], popup="<strong>medium risk Desertificated Areas in Brazzaville</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        #South Africa
        folium.Marker(location=[-22.813930,22.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-23.813930,22.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-23.813930,23.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-23.813930,24.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-24.813930,21.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-24.813930,22.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-22.813930,23.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-21.813930,24.540200], popup="<strong>Desertificated Areas with high risk in South Africa</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-22.23559,22.906193], popup="<strong>Desertificated Areas in South Africa</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        #Nigeria
        for i in range(8):
            folium.Marker(location=[8.813930+(0.5*i),6.540200+(0.15*i*i)], popup="<strong>Desertificated Areas with high risk in Nigeria</strong>", tooltip="Click for more information").add_to(m)
        for i in range(5):
            folium.Marker(location=[6.813930+(0.15*i*i),3.540200+(0.15*i*i*i)], popup="<strong>Desertificated Areas with medium risk in Nigeria</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        for i in range(5):
            folium.Marker(location=[-10.813930+(0.15*i*i/7),15.540200+(0.15*i*i*i)], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        for i in range(7):
            folium.Marker(location=[-29.813930+(0.15*i*i),28.540200+(0.1*i*i)], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information").add_to(m)
        for i in range(6,28):
            folium.Marker(location=[i,i], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information").add_to(m)
        for i in range(6,28):
            folium.Marker(location=[i,0], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information").add_to(m)
            folium.Marker(location=[4.5,i], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information").add_to(m)
            folium.Marker(location=[-25.023559,16.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
            
        for i in range(6,28):
            folium.Marker(location=[-10+(0.15*i),30+(0.25*i)], popup="<strong>Desertificated Areas with medium risk</strong>", tooltip="Click for more information").add_to(m)
            folium.Marker(location=[-10+(0.15*i),30+(0.007)*i], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        #Mauritania
        folium.Marker(location=[23.813930,-10.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[21.813930,-9.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[21.813930,-10.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[18.813930,-13.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[17.813930,-15.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[19.813930,-12.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[20.813930,-11.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.813930,-8.540200], popup="<strong>Desertificated Areas with high risk in Mauritania</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[10.23559,-8.906193], popup="<strong>Desertificated Areas in Mauritania</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        #Malawi
        folium.Marker(location=[-13.540200,33.45], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-14.54020,35.768], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-14.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-15.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-15.813930,32.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-13.813930,33.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-12.813930,35.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-16.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="green")).add_to(m)
        folium.Marker(location=[-13.23559,33.906193], popup="<strong>Desertificated Areas in Malawai</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        
        #Kenya
        folium.Marker(location=[0.813930,37.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[1.813930,38.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[1.813930,40.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[0.813930,39.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[0.813930,33.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-1.813930,34.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[2.813930,35.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[1.813930,37.540200], popup="<strong>Desertificated Areas with high risk in Kenya</strong>", tooltip="Click for more information").add_to(m)
        folium.Marker(location=[3.23559,38.906193], popup="<strong>Desertificated Areas in Kenya</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        

        #Mali
        folium.Marker(location=[15.023559,-5.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)
        folium.Marker(location=[14.023559,-7.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        folium.Marker(location=[3.023559,16.906193], popup="<strong>Desertificated Areas in Congo</strong>", tooltip="Click for more information",icon=folium.Icon(icon="cloud", color="red")).add_to(m)

        m1 = m.get_root().render()

    
    return render_template("desertificationml.html", m = m1)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
CREATE TABLE Address (address_ID int NOT NULL ,
                        country varchar(255) NOT NULL,
                        state varchar(255) NOT NULL,
                        city varchar(255) NOT NULL,
                        street_address varchar(255) NOT NULL,
                        zipcode int NOT NULL,
                        PRIMARY KEY (address_ID));

CREATE TABLE Customer (customer_ID int NOT NULL,
                        first_name varchar(255) NOT NULL,
                        last_name varchar(255) NOT NULL,
                        address_ID int NOT NULL,
                        PRIMARY KEY (customer_ID),
                        FOREIGN KEY (address_ID) REFERENCES Address(address_ID));

CREATE TABLE Restaurant (restaurant_ID int NOT NULL,
                        name varchar(255) NOT NULL,
                        food_genre varchar(255),
                        price_range varChar(255),
                        rating decimal(5,2),
                        address_ID int NOT NULL,
                        open_time time(6) NOT NULL,
                        close_time time(6) NOT NULL,
                        PRIMARY KEY (restaurant_ID),
                        FOREIGN KEY (address_ID) REFERENCES Address(address_ID));

CREATE TABLE Menu (menu_ID int NOT NULL,
                    restaurant_ID int NOT NULL,
                    bio varchar(255),
                    PRIMARY KEY (menu_ID),
                    FOREIGN KEY (restaurant_ID) REFERENCES Restaurant(restaurant_ID));

CREATE TABLE Section (section_ID int NOT NULL,
                        title varchar(255) NOT NULL,
                        menu_ID int NOT NULL,
                        start_time time(6) NOT NULL,
                        end_time time(6) NOT NULL,
                        PRIMARY KEY (section_ID),
                        FOREIGN KEY (menu_ID) REFERENCES Menu(menu_ID));

CREATE TABLE Dish (dish_ID int NOT NULL,
                    name varchar(255) NOT NULL,
                    section_ID int NOT NULL,
                    cost decimal(5,2) NOT NULL,
                    ingredients varchar(255) NOT NULL, 
                    PRIMARY KEY (dish_ID),
                    FOREIGN KEY (section_ID) REFERENCES Section(section_ID));


CREATE TABLE Cart (cart_ID int NOT NULL,
                    restaurant_ID int NOT NULL,
                    customer_ID int NOT NULL,
                    time_Ordered datetime DEFAULT CURRENT_TIMESTAMP,
                    cost decimal(7,2) NOT NULL,
                    tip decimal(7,2),
                    PRIMARY KEY (cart_ID),
                    FOREIGN KEY (customer_ID) REFERENCES Customer(customer_ID),
                    FOREIGN KEY (restaurant_ID) REFERENCES Restaurant(restaurant_ID));

CREATE TABLE Purchase (purchase_ID int NOT NULL,
                        cart_ID int NOT NULL,
                        dish_ID int NOT NULL,
                        quantity int NOT NULL,
                        PRIMARY KEY (purchase_ID),
                        FOREIGN KEY (cart_ID) REFERENCES Cart(cart_ID),
                        FOREIGN KEY (dish_ID) REFERENCES Dish(dish_ID));

INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (1, 'America', 'Texas', 'Mukwonago', '4356 Artesian Avenue', 53149);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (2, 'America', 'Wisconsin', 'Milwaukee', '4465 Milwaukee Street', 53201);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (3, 'America', 'Wisconsin', 'Milwaukee', '123 South Street', 53203);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (4, 'America', 'Louisiana', 'Baton Rouge', '777 Burbank Road', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (5, 'America', 'Texas', 'Baton Rouge', '528 Chimes Road', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (6, 'America', 'Louisiana', 'Baton Rouge', '197 Main Street’', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (7, 'America', 'Illinois', 'Chicago', '1489 Main Street', 60007);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (8, 'America', 'Louisiana', 'Baton Rouge', '455 Ben Hur Road', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (9, 'America', 'Louisiana', 'New Orleans', '43 Bourbon Street', 70032);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (10, 'America', 'Louisiana', 'Baton Rouge', '1499 Nicholson Drive', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (11, 'America', 'Texas', 'San Antonio', '202  Freshour Circle', 78205);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (12, 'America', 'Texas', 'Seguin', '4077  Morris Street', 78155);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (13, 'America', 'Texas', 'Dallas', '1326  Whitetail Lane', 75234);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (14, 'America', 'Colorado', 'Colorado Springs', '4168  Berry Street', 80915);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (15, 'America', 'Colorado', 'Denver', '4815  Leo Street', 80216);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (16, 'America', 'Colorado', 'Baton Rouge', '197 Main Street’', 70820);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (17, 'America', 'Colorado', 'Denver', '3362  Sweetwood Drive', 80220);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (18, 'America', 'Wisconsin', 'Cypress', '2389  Reynolds Alley', 90630);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (19, 'America', 'Louisiana', 'Los Angeles', '3570  Rhode Island Avenue', 90001);
INSERT INTO Address (address_ID, country, state, city, street_address, zipcode) VALUES (20, 'America', 'California', 'San Diego', '2102  Poplar Avenue', 92117);

INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (1, 'Austins' , 'Apples' , '$', 3, 1, '08:00:00', '21:00:00'); 
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (2, 'Bryans Bistro', 'Lunch' , '$$', 3.5, 2, '09:00:00', '22:00:00');
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (3, 'Craigs Cake', 'Desert' , '$$$', 4, 3, '10:00:00', '23:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (4, 'Dereks Desert', 'Desert' , '$$$$', 4.5, 4, '08:00:00', '21:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (5, 'Ethans Eggs', 'Breakfast' ,'$', 5, 5, '09:00:00', '20:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (6, 'Franks Food', 'Burgers','$$', 3, 6, '10:00:00', '22:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (7, 'Geralds Greens', 'Vegetarian' ,'$$$', 3.5, 7, '08:00:00', '23:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (8, 'Hanks House', 'Pizza','$$$$', 4, 8, '09:00:00', '21:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (9, 'Ithicas Igloo', 'Seafood','$', 4.5, 9, '10:00:00', '22:00:00') ;
INSERT INTO Restaurant (restaurant_ID, name, food_genre, price_range, rating, address_ID, open_time, close_time) VALUES (10, 'Justins Junction', 'Sandwhiches','$$', 5, 10, '08:00:00', '18:00:00') ;

INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (1, 'Appetizers', 1, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (2, 'Entree', 1, '12:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (3, 'Drinks', 1, '09:00:00', '21:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (4, 'Breakfast', 2, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (5, 'Lunch', 2, '12:00:00', '19:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (6, 'Drinks', 2, '09:00:00', '22:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (7, 'Appetizers', 3, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (8, 'Dinner', 3, '12:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (9, 'Drinks', 3, '09:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (10, 'Lunch', 4, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (11, 'Dinner', 4, '12:00:00', '22:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (12, 'Appetizers', 4, '09:00:00', '22:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (13, 'Desserts', 5, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (14, 'Sides', 5, '13:00:00', '21:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (15, 'Cocktails', 5, '09:00:00', '23:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (16, 'Appetizers', 6, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (17, 'Entree', 6, '13:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (18, 'Drinks', 6, '09:00:00', '21:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (19, 'Lunch', 7, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (20, 'Brunch', 7, '12:00:00', '14:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (21, 'Mixed Drinks', 7, '09:00:00', '16:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (22, 'Appetizers', 8, '10:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (23, 'Entree', 8, '12:00:00', '19:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (24, 'Desserts', 8, '09:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (25, 'Appetizers', 9, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (26, 'Lunch', 9, '12:00:00', '20:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (27, 'Dinner', 9, '09:00:00', '22:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (28, 'Appetizers', 10, '08:00:00', '12:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (29, 'Entree', 10, '12:00:00', '19:00:00');
INSERT INTO Section (section_ID, title, menu_ID, start_time, end_time) VALUES (30, 'Drinks', 10, '09:00:00', '21:00:00');

INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (1, 'Jacob', 'John', 11);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (2, 'John', 'Doe', 12);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (3, 'Jane', 'Doe', 13);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (4, 'Todd', 'Johnson', 14);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (5, 'Kurt', 'Baker', 15);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (6, 'Frank', 'Herbert', 16);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (7, 'Luke', 'Skywalker', 17);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (8, 'Tim', 'Cook', 18);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (9, 'Steve', 'Nash', 19);
INSERT INTO Customer (customer_ID, first_name, last_name, address_ID) VALUES (10, 'Pat', 'Smith', 20);

INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (1, 'Vegetable Curry', 2, 20.50, 'Vegetables, Salt, Spices, Oil, Water');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (2, 'Mashed Potatoes', 1, 7.99, 'Potatoes, Garlic, Cream, Butter');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (3, 'Burrito', 5, 12.00, 'Black Beans, Steak, Salsa, Cheese, Sour Cream'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (4, 'Steak', 8, 25.99, 'Beef'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (5, 'House Salad', 7, 6.99, 'Lettuce, Cheese, Dressing'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (6, 'Stir Fry', 10, 12.99, 'Noodles, Vegetables, Sauce'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (7, 'Cesar Salad', 12, 7.99, 'Lettuce, Cheese, Cesar Dressing');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (8, 'Alfredo Pasta', 17, 16.99, 'Noodles, Alfredo Sauce'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (9, 'Shrimp', 16, 8.99, 'Shrimp');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (10, 'Steamed Rice', 22, 2.99, 'Rice, Butter'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (11, 'Breadsticks', 25, 4.99, 'Breadsticks, Butter, Garlic');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (12, 'Chicken Noodle Soup', 26, 7.99, 'Chicken, Noodles, Chicken Broth, Carrots'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (13, 'Brownie', 24, 4.99, 'Milk, Egg, Chocolate'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (14, 'Ice Cream', 24, 4.99, 'Vanilla Ice Cream'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (15, 'Hummus', 28, 3.99, 'Chickpeas');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (16, 'Fried Vegetables', 29, 8.99, 'Carrots, Broccoli, Peas');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (17, 'Apple pie', 13 , 3.99, 'Apple Filling, Pie Crust, Cinnamon');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (18, 'Fruit Salad', 20, 1.99, 'Pineapple, Watermelon, Grape, Strawberry');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (19, 'Roast Beef', 27, 18.99, 'Beef, Mushrooms'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (20, 'Coffee', 3, 2.99, 'Coffee'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (21, 'Apple Juice', 6, 3.99, 'Pressed Apple'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (22, 'Fried Chicken', 4, 9.99, 'Chicken'); 
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (23, 'Spaghetti with Meatballs', 19, 12.99, 'Noodles, Marinara Sauce, Meatballs, Garlic');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (24, 'Burger', 23, 10.99, 'Bun, Tomato, Lettuce, Beef Patty');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (25, 'Pancakes', 4, 6.99, 'Pancakes, Syrup');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (26, 'Sprite', 9, 2.99, 'Lime, Ice');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (27, 'Cola', 9, 2.99, 'Sugar, Water');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (28, 'Chicken and Waffles', 11, 6.99, 'Chicken, Waffles');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (29, 'French Fries', 14, 3.99, 'Potato');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (30, 'Root Beer Float', 15, 3.99, 'Root Beer, Ice Cream');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (31, 'Cola', 18, 2.99, 'Sugar, Water');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (32, 'Pina-Colada', 21, 2.99, 'Pineapple, Coconut');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (33, 'Water', 30, .99, 'Hydrogen, Hydrogren, Oxygen');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (34, 'Hotdog', 17, 3.99, 'Weiner, Bun');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (35, 'Pepporonni Pizza', 23, 7.99, 'Pizz Douge, Pizza Sauce, Pepporonni');
INSERT INTO Dish (dish_ID, name, section_ID, cost, ingredients) VALUES (36, 'Boudin Balls', 25, 3.99, 'Boudin, Batter');

INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (1, 1, 'Sweetest Apples in Town!');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (2, 2, 'Where flavor meets excellence');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (3, 3, 'Professionally Made Cakes');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (4, 4, 'Got a sweet-tooth?');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (5, 5, 'Theyre Eggcelent');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (6, 6, 'Best Burgers in Town!');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (7, 7, 'We put the health in healthy');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (8, 8, 'Just like at home!');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (9, 9, 'Igloo!');
INSERT INTO Menu (menu_ID, restaurant_ID, bio) VALUES (10, 10, 'Junction between taste and comfort!');

INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (1, 10, 5, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (2, 2, 4, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (3, 6, 7, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (4, 7, 2, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (5, 3, 8, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (6, 8, 3, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (7, 5, 9, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (8, 4, 6, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (9, 1, 10, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (10, 9, 5, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (11, 6, 4, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (12, 4, 1, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (13, 4, 2, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (14, 5, 2, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (15, 2, 8, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (16, 4, 3, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (17, 7, 5, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (18, 4, 6, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (19, 8, 5, 0, 0);
INSERT INTO Cart (cart_ID, customer_ID, restaurant_ID, cost, tip) VALUES (20, 9, 5, 0, 0);

INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 1, 1, 36, 1);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 2, 2, 1, 2);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 3, 3, 34, 2);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 4, 1, 3, 3);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 5, 2, 32, 1);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 6, 3, 5, 3);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 7, 1, 30, 3);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 8, 2, 7, 3);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 9, 3, 28, 5);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 10, 1, 9, 4);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 11, 2, 26, 7);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 12, 3, 11, 8);

INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 13, 1, 24, 9);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 14, 2, 13, 9);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 15, 3, 22, 9);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 16, 1, 15, 4);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 17, 2, 20, 10);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 18, 3, 17, 10);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 19, 1, 18, 12);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 20, 2, 19, 12);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 21, 3, 16, 12);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 22, 1, 21, 11);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 23, 2, 14, 11);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 24, 3, 23, 2);

INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 25, 1, 12, 5);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 26, 2, 25, 1);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 27, 3, 10, 4);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 28, 1, 27, 4);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 29, 2, 8, 5);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 30, 3, 29, 6);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 31, 1, 6, 6);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 32, 2, 31, 6);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 33, 3, 4, 7);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 34, 1, 33, 7);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 35, 2, 2, 8);
INSERT INTO Purchase (purchase_ID, quantity, dish_id, cart_id) VALUES ( 36, 3, 35, 8);

SELECT state, COUNT(state) FROM Address
                            GROUP BY state
                            ORDER BY COUNT(state) DESC;
                        
SELECT R.name, ROUND(AVG(D.cost),2) FROM Restaurant as R
          JOIN Menu as M ON R.restaurant_ID = M.restaurant_ID
          JOIN Section as S on M.menu_ID = S.menu_ID
          Join Dish as D on S.section_ID = D.section_ID GROUP BY R.name ORDER BY ROUND(AVG(D.cost),2) DESC;
        
SELECT name FROM Restaurant as R
                      JOIN Address as A ON R.address_ID = A.address_ID
                      WHERE state IN (SELECT state FROM Customer as C
                      JOIN Address as A on C.address_ID = A.address_ID
                      WHERE C.first_name = 'Jacob');

SELECT ROUND(close_time - open_time,3) , name FROM Restaurant 
                    ORDER BY close_time - open_time DESC LIMIT 3;

SELECT COUNT(R.restaurant_ID), R.name FROM Restaurant AS R
                JOIN Menu AS M ON R.restaurant_ID = M.restaurant_ID
                JOIN Section AS S ON M.menu_ID = S.menu_ID
                JOIN Dish AS D ON S.section_ID = D.section_ID GROUP BY R.restaurant_ID
                ORDER BY COUNT(R.restaurant_ID) DESC LIMIT 1;

SELECT COUNT(R.restaurant_ID), R.name FROM Cart AS C 
                  NATURAL JOIN Restaurant as R GROUP BY R.restaurant_ID
                  ORDER BY COUNT(R.restaurant_ID) DESC;

SELECT COUNT(R.restaurant_ID), R.name FROM Cart AS C 
                  NATURAL JOIN Restaurant as R 
                  NATURAL JOIN Address as A
                  WHERE C.customer_ID
                  IN (SELECT customer_ID FROM Customer as C JOIN Address as A on C.address_ID = A.address_ID
                      WHERE A.state = 'Colorado')        
                  GROUP BY R.restaurant_ID
                  ORDER BY COUNT(R.restaurant_ID) DESC LIMIT 2;

SELECT DISTINCT state FROM Address NATURAL JOIN Restaurant
                         WHERE state IN
                         (SELECT DISTINCT state FROM Address NATURAL JOIN Customer);

SELECT D.cost , D.name FROM Restaurant AS R
                JOIN Menu AS M ON R.restaurant_ID = M.restaurant_ID
                JOIN Section AS S ON M.menu_ID = S.menu_ID
                JOIN Dish AS D ON S.section_ID = D.section_ID WHERE R.restaurant_ID 
                IN (SELECT restaurant_ID FROM restaurant WHERE name = 'Bryans Bistro')
                ORDER BY D.cost DESC;

SELECT AVG(cost) FROM Cart
                  WHERE customer_ID IN (SELECT customer_ID FROM Customer WHERE first_name = 'Johnson');

UPDATE Cart AS C JOIN Purchase AS P ON C.Cart_ID = P.Cart_ID
              JOIN Dish AS D ON P.Dish_ID = D.Dish_ID
              SET C.Cost = (SELECT sum(D.cost * P.quantity) * 1.085
                            FROM Purchase P                
                            WHERE C.cart_id = P.cart_id
                            GROUP BY P.cart_ID);

UPDATE Dish SET ingredients='Rice, butter, tomato, potato' WHERE dish_ID = 10;

UPDATE Restaurant SET food_genre='Carribean' WHERE restaurant_ID = 8;

UPDATE Cart AS C NATURAL JOIN Customer AS CT SET tip = cost*0.2 WHERE (CT.customer_ID = 1);

UPDATE Restaurant r 
    JOIN Menu as M ON R.restaurant_ID = M.restaurant_ID
    JOIN Section as S on M.menu_ID = S.menu_ID
    JOIN Dish as D on S.section_ID = D.section_ID 
SET R.price_range = CASE
    WHEN (SELECT ROUND(AVG(D.cost),2) FROM Dish) > 10 THEN '$$$'
        WHEN (SELECT ROUND(AVG(D.cost),2) FROM Dish) > 15 THEN '$$$$'
        ELSE r.price_range
END;

DELETE FROM Cart
    WHERE cost = 0;

DELETE FROM Address
   WHERE address_ID NOT IN(
       SELECT aID FROM(
           SELECT Customer.Address_id AS aID FROM Customer NATURAL JOIN
 		Address
       ) AS CA
   )
   AND address_ID NOT IN(
       SELECT aID FROM(
           SELECT Restaurant.Address_id AS aID FROM Restaurant NATURAL
 		JOIN Address
       ) AS RA
   )


DELETE FROM Customer
   WHERE customer_id IN(
       SELECT c_ID FROM(
           SELECT Cart.customer_id AS c_ID FROM Cart NATURAL JOIN
 		Customer as C
           GROUP BY C.customer_ID
           ORDER BY COUNT(C.customer_ID)
       ) AS CC
   )
   LIMIT 1;

DELETE FROM Restaurant
   WHERE name = "Justins Junction";

class Data:

    def __init__(self):
        self.users = [
            {"user_id": 1, "first_name": "Orrin", "last_name": "Palombi", "email": "opalombi0@spiegel.de","phone": "877-264-5336", "password": "mECoavG", "username": "opalombi0"},
            {"user_id": 2, "first_name": "Enrique", "last_name": "Scammell", "email": "escammell1@yellowbook.com","phone": "820-621-8379", "password": "YHLEmb", "username": "escammell1"},
            {"user_id": 3, "first_name": "Stephine", "last_name": "Arnley", "email": "sarnley2@drupal.org","phone": "261-778-8034", "password": "6R7eTgZ6", "username": "sarnley2"},
            {"user_id": 4, "first_name": "Olimpia", "last_name": "Itzik", "email": "oitzik3@yelp.com","phone": "870-457-3079", "password": "nmyVcchad8", "username": "oitzik3"},
            {"user_id": 5, "first_name": "Serge", "last_name": "Labat", "email": "slabat4@sina.com.cn","phone": "670-777-4902", "password": "ONXd7UJ", "username": "slabat4"},
            {"user_id": 6, "first_name": "Noam", "last_name": "Hand", "email": "nhand5@liveinternet.ru","phone": "220-172-7328", "password": "NmQ4U51DRLGk", "username": "nhand5"},
            {"user_id": 7, "first_name": "Merlina", "last_name": "Crisell", "email": "mcrisell6@usnews.com","phone": "844-715-3735", "password": "sw37sJ8pm", "username": "mcrisell6"},
            {"user_id": 8, "first_name": "Danna", "last_name": "Pawlaczyk", "email": "dpawlaczyk7@squidoo.com","phone": "573-216-8507", "password": "DyyhvZ", "username": "dpawlaczyk7"},
            {"user_id": 9, "first_name": "Moore", "last_name": "Iacovini", "email": "miacovini8@businesswire.com","phone": "538-338-0128", "password": "0eFnhk", "username": "miacovini8"},
            {"user_id": 10, "first_name": "Clarie", "last_name": "Fosken", "email": "cfosken9@ustream.tv","phone": "778-725-0847", "password": "PWDHZw40", "username": "cfosken9"}
        ]

        self.posts = [
            {"post_id": 1, "media": "http://dummyimage.com/147x176.png/cc0000/ffffff",
             "message": "Suspendisse potenti. Cras in purus eu magna vulputate luctus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo.",
             "post_date": "12/29/2018", "chat_group_id": 9, "post_author_id": 6},
            {"post_id": 2, "media": "http://dummyimage.com/179x225.bmp/dddddd/000000",
             "message": "Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit.",
             "post_date": "3/28/2018", "chat_group_id": 3, "post_author_id": 7},
            {"post_id": 3, "media": "http://dummyimage.com/233x143.png/cc0000/ffffff",
             "message": "Nullam varius. Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus. Phasellus in felis.",
             "post_date": "10/26/2018", "chat_group_id": 3, "post_author_id": 9},
            {"post_id": 4, "media": "http://dummyimage.com/138x225.bmp/5fa2dd/ffffff",
             "message": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus. Duis at velit eu est congue elementum. In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo. Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros.",
             "post_date": "10/4/2018", "chat_group_id": 3, "post_author_id": 1},
            {"post_id": 5, "media": "http://dummyimage.com/186x165.bmp/ff4444/ffffff",
             "message": "Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat. Nulla tempus.",
             "post_date": "1/13/2019", "chat_group_id": 9, "post_author_id": 10},
            {"post_id": 6, "media": "http://dummyimage.com/184x114.jpg/cc0000/ffffff",
             "message": "Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus.",
             "post_date": "12/10/2018", "chat_group_id": 10, "post_author_id": 9},
            {"post_id": 7, "media": "http://dummyimage.com/228x231.jpg/ff4444/ffffff",
             "message": "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.",
             "post_date": "9/6/2018", "chat_group_id": 6, "post_author_id": 4},
            {"post_id": 8, "media": "http://dummyimage.com/135x195.png/dddddd/000000",
             "message": "Suspendisse potenti. Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris. Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.",
             "post_date": "10/28/2018", "chat_group_id": 10, "post_author_id": 6},
            {"post_id": 9, "media": "http://dummyimage.com/111x223.jpg/cc0000/ffffff",
             "message": "Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem. Fusce consequat. Nulla nisl. Nunc nisl. Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapibus.",
             "post_date": "11/16/2018", "chat_group_id": 6, "post_author_id": 4},
            {"post_id": 10, "media": "http://dummyimage.com/196x203.jpg/dddddd/000000",
             "message": "In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt.",
             "post_date": "12/14/2018", "chat_group_id": 2, "post_author_id": 5}
        ]

        self.groups = [
            {"chat_group_id":1,"chat_group_name":"Aongstroemia longipes (Somm.) Bruch & Schimp.","owner_id":4},
            {"chat_group_id":2,"chat_group_name":"Schiedea salicaria Hillebr.","owner_id":4},
            {"chat_group_id":3,"chat_group_name":"Clarkia biloba (Durand) A. Nelson & J.F. Macbr. ssp. australis F.H. Lewis & M.E. Lewis","owner_id":6},
            {"chat_group_id":4,"chat_group_name":"Euphorbia polyphylla Engelm. ex Holz.","owner_id":9},
            {"chat_group_id":5,"chat_group_name":"Mirabilis nyctaginea (Michx.) MacMill.","owner_id":1},
            {"chat_group_id":6,"chat_group_name":"Carex paeninsulae Naczi, E.L. Bridges & Orzell","owner_id":5},
            {"chat_group_id":7,"chat_group_name":"Solanum triflorum Nutt.","owner_id":4},
            {"chat_group_id":8,"chat_group_name":"Eryngium pendletonensis K.L. Marsden & M.G. Simpson","owner_id":10},
            {"chat_group_id":9,"chat_group_name":"Artemisia kauaiensis (Skottsb.) Skottsb.","owner_id":5},
            {"chat_group_id":10,"chat_group_name":"Actaea laciniata (S. Watson) J. Compton","owner_id":3}
        ]

        self.group_members = [
            {"user_id":4,"chat_group_id":10},
            {"user_id":8,"chat_group_id":6},
            {"user_id":3,"chat_group_id":6},
            {"user_id":8,"chat_group_id":7},
            {"user_id":6,"chat_group_id":8},
            {"user_id":6,"chat_group_id":10},
            {"user_id":9,"chat_group_id":3},
            {"user_id":7,"chat_group_id":3},
            {"user_id":3,"chat_group_id":7},
            {"user_id":9,"chat_group_id":2}

        ]

        self.contacts = [
            {"user_id": 5, "contact_user_id": 9},
            {"user_id": 2, "contact_user_id": 8},
            {"user_id": 10, "contact_user_id": 9},
            {"user_id": 9, "contact_user_id": 6},
            {"user_id": 1, "contact_user_id": 5},
            {"user_id": 1, "contact_user_id": 7},
            {"user_id": 5, "contact_user_id": 5},
            {"user_id": 8, "contact_user_id": 5},
            {"user_id": 1, "contact_user_id": 10},
            {"user_id": 2, "contact_user_id": 2}
        ]

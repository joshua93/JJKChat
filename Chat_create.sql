-- Last modification date: 2019-04-05 18:08:03.977

-- tables

-- Table: users
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50),
    phone varchar(50),
    password varchar(200),
    username varchar(50) UNIQUE
);

-- Table: chat_groups
CREATE TABLE chat_groups (
    chat_group_id serial PRIMARY KEY,
    chat_name varchar(50),
    user_id int REFERENCES users (user_id)
);

-- Table: post
CREATE TABLE post (
    post_id serial PRIMARY KEY,
    media varchar(200),
    message varchar(255)  NULL,
    post_date date,
    chat_group_id int REFERENCES chat_groups (chat_group_id),
    user_id int REFERENCES users (user_id)
);

-- Table: chat_group_members
CREATE TABLE chat_group_members (
    user_id int REFERENCES users (user_id),
    chat_group_id int REFERENCES chat_groups (chat_group_id),
    PRIMARY KEY (user_id,chat_group_id)
);

-- Table: contact
CREATE TABLE contact (
    user_id int REFERENCES users (user_id),
    contact_user_id int REFERENCES users (user_id) ,
    PRIMARY KEY (user_id,contact_user_id)
);

-- Table: hashtags
CREATE TABLE hashtags (
    hashtag_id serial PRIMARY KEY,
    hashtag varchar(50),
    post_id int REFERENCES post (post_id)
);

-- Table: reactions
CREATE TABLE reactions (
    reaction boolean,
    user_id int REFERENCES users (user_id),
    post_id int REFERENCES post (post_id),
    reaction_date date,
    PRIMARY KEY (user_id,post_id)
);

-- Table: reply
CREATE TABLE reply (
    reply_id serial PRIMARY KEY,
    reply_date date,
    reply_message varchar(255),
    post_id int REFERENCES post (post_id),
    user_id int REFERENCES users (user_id)
);


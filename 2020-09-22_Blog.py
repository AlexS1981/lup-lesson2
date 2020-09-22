# Блог.
# 1. Реализовать класс пользователь (содержит в себе блог и информацию о пользователе)
# 2. Реализовать класс блог (содержит список постов)
# 3. Реализовать класс пост (содержит автора, контент, количество лайков)
# 4. Реализовать класс лента (содержит в себе все посты со всех блогов пользователей)
# У пользователя есть блог, у блога есть посты, у постов есть лайки, контент и автор.
# Объект класса лента содержит список всех постов всех пользователей

import re

user_id = list()
blog_id = list()
post_id = list()
likes_id = list()


class User:
    def __init__(self, name, surname, e_mail, location = None):
        if e_mail_validate(e_mail) == True:
            self.name = name
            self.surname = surname
            self.e_mail = e_mail
            self.location = location
            user_id.append(self)
            print('Создан пользователь {} {}'.format(self.name, self.surname))
        else:
            print('Ошибка e-mail!')

    def user_location(self, location):
        self.location = location


class Post:
    def __init__(self, user, blog, post, likes = None):
        self.user = user
        self.blog = blog
        self.post = post
        self.likes = likes
        post_id.append(self)
        self.likes = Like(0)

    def post_print(self):
        print(self.post)


class Like:
    def __init__(self, likes):
        self.likes = likes
        likes_id.append(self)

    def like_set(self):
        self.likes += 1
        return self

    def like_info(self):
        print('Количество лайков у поста {} - уже {}.'.format(likes_id.index(self), self.likes))


class Blog:
    def __init__(self, blog):
        self.blog = blog
        blog_id.append(self)


class Feed:
    @staticmethod
    def feed():
        f = list()
        for i in post_id:
            f.append(i.post)
        print('Лента: ', str(f)[1:-1])


def loc(list_loc):
    return [user_id[list_loc[0]], blog_id[list_loc[1]]]


def e_mail_validate(e):
    pattern = re.compile("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$")
    is_valid = pattern.match(e)
    if is_valid:
        return True

a1 = User('A1', 'S1', 'asf1@gmail.com')
a2 = User('A2', 'S2', 'asf2@gmail.com')
a3 = User('A3', 'S3', 'asf3')
print('Создано только {} пользователя.'.format(len(user_id)))
b1 = Blog('Blog1')
a2.user_location(loc([1,0]))
print('Что записывается в список аргумента "location":\n', a2.location)
p1 = Post(a2.location[0], a2.location[1], 'My post1')
Post.post_print(post_id[0])
Like.like_set(p1.likes)
Like.like_set(p1.likes)
Like.like_info(p1.likes)
p2 = Post(a2.location[0], a2.location[1], 'My post2')
Post.post_print(post_id[1])
Like.like_set(p2.likes)
Like.like_info(p2.likes)
Feed.feed()
print(likes_id.index(p2.likes))
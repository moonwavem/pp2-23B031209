#1
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#2
def score(moviess):
    for movie in moviess:
        if movie['imdb'] > 5.5:
            print(movie['name'], '-', bool(1))
        else:
            print(movie['name'], '-', bool())

score(movies)
#3
def highscore(moviees):
    for movie in moviees:
        if movie['imdb'] > 5.5:
            print(movie, end = '\n')

highscore(movies)
#4
def categ(movvies):
    cate = set()
    for movie in movvies:
        string = movie['category']
        cate.add(string)
    for categ_1 in cate:
        print(categ_1, end = ':')
        for movie in movvies:
            if categ_1 == movie['category']:
                print(movie['name'])

categ(movies)
#5
def average(movieee):
    scores = []
    for movie in movieee:
        score = movie['imdb']
        scores.append(score)
    averagescore = sum(scores) / len(scores)
    return averagescore

print(average(movies))
#6
def categ(category, movie):
    if category in movie:
        return True
    
namecateg = input()
moviee = []
for i in movies:
    if categ(namecateg, i['category']) == 1:
        moviee.append(i["imdb"])
sum = 0
for i in range(len(moviee)):
    sum += float(moviee[i])
print(float(sum / len(moviee)))
import pandas as pd

# Ruta de los archivos (ajusta la ruta si es necesario)
data_path = '/home/ubut/Descargas/ml-100k/'

ratings = pd.read_csv(data_path + 'u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])

movies = pd.read_csv(data_path + 'u.item', sep='|', encoding='latin-1', names=['movie_id', 'title'] + [f'genre_{i}' for i in range(19)])

users = pd.read_csv(data_path + 'u.user', sep='|', encoding='latin-1', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])

# Ver los primeros registros para asegurarnos de que todo está correcto
print(ratings.head())
print(movies.head())
print(users.head())

col_n = ['movie id' , 'movie title' , 'release date' , 'video release date' ,
              'IMDb URL' , 'unknown' , 'Action' , 'Adventure' , 'Animation' ,
              "Children's" , 'Comedy' , 'Crime' , 'Documentary' , 'Drama' , 'Fantasy' ,
              'Film-Noir' , 'Horror' , 'Musical' , 'Mystery' , 'Romance' , 'Sci-Fi' ,
              'Thriller' , 'War' , 'Western']

print(movies.shape)

movies.head()


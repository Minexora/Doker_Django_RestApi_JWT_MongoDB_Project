# Proje Kurulumu   

[![Build Status](https://travis-ci.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project.svg?branch=master)](https://travis-ci.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project)

Terminalde aşağıdaki komutu yazarak projeyi ayağa kaldırabilirsiniz.
    
```
sudo docker-compose up -d --build
```

# Proje default kullanıcısı
Projenin default kullanıcı bilgisi aşağıdaki gibidir.

> id: admin
> pw: 123123123

Admin paneline [buraya](http://localhost:8000/admin/) tıklayarak gidibilirsiniz.
Yeni admin kullanıcı admin panelinden eklenebileceği gibi docker da eklenebir. Bunun için;

1. Docker containerlar listelenir. Bunun için aşağıdaki komutu kullanalabirsiniz.

```
docker ps
```
        
2. Container daki bash e bağlanılır. Bunun için aşağıdaki komutu kullanabilirsiniz.

```
docker exec -it <container id> /bin/bash
```
        
3. Yeni kullanıcı oluşturulması için aşağıdaki komut kullanılır. İstenilen bilgiler 
doldurularak yeni kullanıcı oluşturulacaktır.

```
python manage.py createsuperuser
```
    


# Api request 

* Overview için aşağıdaki gibi request atılmalıdır.

![alt text](https://github.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project/blob/master/api_response_image/overview.png?raw=true)

* Login olmak ve token alma için overviewde bulunan login istekte bulunmalısınız. 
Eğer token alınmadan istek atılırsa api çalışmayıp response olara 401 Unauthorized dönecektir.
Aşağıdaki gibi istek atabilirsiniz.

![alt text](https://github.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project/blob/master/api_response_image/login.png?raw=true)

* Login olup token alındıktan sonra bu token aşağıdaki gibi request header içine eklenmelidir.

![alt text](https://github.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project/blob/master/api_response_image/list.png?raw=true)

* Overviewde bulunan linklere token eklendikten sonra istek atılabilir. 
Create ve Edit için request body aşağıdaki gibi olmalıdır.

![alt text](https://github.com/Minexora/Doker_Django_RestApi_JWT_MongoDB_Project/blob/master/api_response_image/create.png?raw=true)

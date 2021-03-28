# Proje Kurulumu
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
        
        2. Container daki bash e bağlanılır. Bunun  için aşağıdaki komutu kullanabilirsiniz.
        
        ```
        docker exec -it <container id> /bin/bash
        ```
        
        3. Yeni kullanıcı oluşturulması için aşağıdaki komut kullanılır. İstenilen bilgiler 
        doldurularak yeni kullanıcı oluşturulacaktır.
        
        ```
        python manage.py createsuperuser
        ```
    


# Api request 
    
    * Overview için 
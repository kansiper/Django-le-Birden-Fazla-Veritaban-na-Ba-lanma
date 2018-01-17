class AuthRouter(object): 

# AuthRouter isminde sadece auth_db kullanma ismini verdiğimiz veri tabanı rauterini ayarlayacağız
# yani sadece auth_db isimli veri tabanı içindir bu
    """
     Tüm veritabanı işlemlerini kontrol eden yönlendirici
     kimlik doğrulama uygulamasının modeldir.
    """
    def db_for_read(self, model, **hints):
        """
        auth_db'ye giden yetkili modelleri (auth models) Okumaya çalışır.
        """
        if model._meta.app_label == 'auth':
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == 'auth':
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Yetkilendirme uygulamasındaki bir model dahil edilirse ilişkilere izin ver.
        iki nesne de auth a ait ise ilişkiye izin veriyor
        """
        if obj1._meta.app_label == 'auth' or \ 
           obj2._meta.app_label == 'auth':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Auth uygulamasının yalnızca 'auth_db' veritabanında göründüğünden emin olun.
        """
        if app_label == 'auth':
            return db == 'auth_db'
        return None

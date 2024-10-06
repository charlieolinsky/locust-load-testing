from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0, 0)
    @task
    def hello_world(self):
        self.client.get("/")

    @task
    def dashboard(self):
        self.client.get("/dashboard")

    @task
    def login(self):
        self.client.post("/login", json={
            "username":"test", 
            "password":"test"
        })

    

from locust import HttpLocust, TaskSet, task, events
# names : random name generator https://github.com/treyhunner/names
import names
import os

def print_error(type, loc, code, reason) :
    print "Error %s %s %s Reason:%s"%(type, code, loc, reason)

def print_success(type, loc, code) :
    print "Success %s %s %s"%(type, code, loc)

def getTargetURL() :
    target = os.environ['TARGET_URL']
    print "Getting target url: %s"%(target)
    return target

class UserBehavior(TaskSet):
    root = getTargetURL()
    request_header = {"Content-Type" : "application/json"}

    @task(20)
    def findByFirstName(self):
        url = "%s/search/findByFirstName?name=%s"%(UserBehavior.root,names.get_first_name())
        r = self.client.get(url=url, name="people/search/findByFirstName?name={name}")
        type = "GET"
        if r.status_code == 200 :
            print_success(type, url, r.status_code)
        else:
            print_error(type, url , r.status_code, r.reason)

    @task(30)
    def findByLastName(self):
        url = "%s/search/findByLastName?name=%s"%(UserBehavior.root,names.get_last_name())
        r = self.client.get(url=url, name="people/search/findByLastName?name={name}")
        type = "GET"
        if r.status_code == 200 :
            print_success(type, url, r.status_code)
        else:
            print_error(type, url , r.status_code, r.reason)

    @task(10)
    def people(self):
        url = UserBehavior.root
        def payload():
            return "{ \"firstName\": \"%s\", \"lastName\":\"%s\"}"%(names.get_first_name(), names.get_last_name())

        def post():
            r = self.client.post(url=url, name="/people", data=payload(), headers=UserBehavior.request_header )
            type = "POST"
            if r.status_code == 201 :
                loc = r.headers.get('location')
                print_success(type, url, r.status_code)
                return loc
            else:
                print_error(type, url, r.status_code, r.reason)

        def get(loc):
            r = self.client.get(url=loc, name="/people/{id}")
            type = "GET"
            if r.status_code == 200 :
                print_success(type, loc, r.status_code)
            else:
                print_error(type, loc, r.status_code, r.reason)

        def put(loc):
            r = self.client.put(url=loc, name="/people/{id}", data=payload(), headers=UserBehavior.request_header)
            type = "PUT"
            if r.status_code == 200 :
                print_success(type, loc, r.status_code)
            else:
                print_error(type, loc, r.status_code, r.reason)

        def patch(loc):
            payload = "{ \"lastName\":\"%s\"}"%(names.get_last_name())
            r = self.client.patch(url=loc, name="/people/{id}", data=payload, headers=UserBehavior.request_header)
            type = "PATCH"
            if r.status_code == 200 :
                print_success(type, loc, r.status_code)
            else:
                print_error(type, loc, r.status_code, r.reason)

        def delete(loc):
            r = self.client.delete(url=loc, name="/people/{id}")
            type = "DELETE"
            if r.status_code == 204 :
                print_success(type, loc, r.status_code)
            else:
                print_error(type, loc, r.status_code, r.reason)

        location = post()
        get(location)
        patch(location)
        put(location)
        #delete(location)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

    def on_request_success(request_type, name, response_time, response_length):
        print "RequestType:[%s] Name:[%s] ResponseTime:[%s] ResponseLength:[%s]"%(request_type, name, response_time, response_length)

    def on_request_failure(request_type, name, response_time, exception):
        print "RequestType:[%s] Name:[%s] ResponseTime:[%s] Exception:[%s]"%(request_type, name, response_time, exception)

    #events.request_success += on_request_success
    events.request_failure += on_request_failure

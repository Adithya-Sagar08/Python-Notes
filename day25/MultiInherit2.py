class FrontendDev:

    @staticmethod
    def develop_frontend():
        print("Develop frontend app with HTML, CSS and React")


class BackendDev:

    @staticmethod
    def develop_backend():
        print("Develop backend app with Flask and Python")


class FullStackDev(FrontendDev, BackendDev):

    @staticmethod
    def deploy_full_stack():
        print("Deploy full stack app on Cloud Platform")


f = FullStackDev()
f.develop_frontend()
f.develop_backend()
f.deploy_full_stack()
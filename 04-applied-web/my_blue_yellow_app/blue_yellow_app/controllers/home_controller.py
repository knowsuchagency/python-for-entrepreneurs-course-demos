import pyramid_handlers


class HomeController:

    def __init__(self, request):
        self.request = request

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {}
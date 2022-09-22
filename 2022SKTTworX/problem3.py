from calendar import c


def solution(n, plans, clients):
    class Client:
        use_data: int
        additional_services: set

        def __init__(self, data, services) -> None:
            self.use_data = data
            self.additional_services = services

        def __str__(self) -> str:
            return f"Client Using Data: {self.use_data}MB, Services: {str(self.additional_services)}"

        def _unlist_services(self, services: list) -> None:
            for service in services:
                if service in self.additional_services:
                    self.additional_services.remove(service)

        def check_satisfied(self, provided_data, provided_services):
            self._unlist_services(provided_services)
            data_satisfied = self.use_data <= provided_data
            services_satisfied = len(self.additional_services) == 0
            # print(f"{data_satisfied=}")
            # print(f"{services_satisfied=}")
            return data_satisfied and services_satisfied

    def transform_client(client_str: str):
        sp = client_str.split()
        data = int(sp[0])
        additional_services = set(map(int, sp[1:]))

        return Client(data, additional_services)

    clients = [transform_client(c) for c in clients]
    answer = [0 for _ in clients]

    for plan_number, plan in enumerate(plans):
        sp = plan.split()
        provided_data: int = int(sp[0])
        added_services: list = list(map(int, sp[1:]))

        for client_index, client in enumerate(clients):
            # print(client)
            # print(f"Provides {provided_data}, {added_services}")
            if (
                client.check_satisfied(provided_data, added_services)
                and answer[client_index] == 0
            ):
                answer[client_index] = plan_number + 1

        print(answer)

    return answer


from calendar import c


def solution(n, plans, clients):
    class Client:
        use_data: int
        additional_services: set

        def __init__(self, data, services) -> None:
            self.use_data = data
            self.additional_services = services

        def __str__(self) -> str:
            return f"Client Using Data: {self.use_data}MB, Services: {str(self.additional_services)}"

        def _unlist_services(self, services: list) -> None:
            for service in services:
                if service in self.additional_services:
                    self.additional_services.remove(service)

        def check_satisfied(self, provided_data, provided_services):
            self._unlist_services(provided_services)
            data_satisfied = self.use_data <= provided_data
            services_satisfied = len(self.additional_services) == 0
            # print(f"{data_satisfied=}")
            # print(f"{services_satisfied=}")
            return data_satisfied and services_satisfied

    def transform_client(client_str: str):
        sp = client_str.split()
        data = int(sp[0])
        additional_services = set(map(int, sp[1:]))

        return Client(data, additional_services)

    clients = [transform_client(c) for c in clients]
    answer = [0 for _ in clients]

    for plan_number, plan in enumerate(plans):
        sp = plan.split()
        provided_data: int = int(sp[0])
        added_services: list = list(map(int, sp[1:]))

        for client_index, client in enumerate(clients):
            # print(client)
            # print(f"Provides {provided_data}, {added_services}")
            if (
                client.check_satisfied(provided_data, added_services)
                and answer[client_index] == 0
            ):
                answer[client_index] = plan_number + 1

    return answer

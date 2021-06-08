#eoherrerab

class Subnet:

    def __init__(self, subnet_number: int, subnet_name: str, ip: list[int], hosts_required: int):
        self.__subnet_number = subnet_number
        self.__subnet_name = subnet_name
        self.__subnet_address = ip
        self.__hosts_required = hosts_required
        self.__hosts_found = 0
        self.__exponent = 0
        self.__usage_percentage = 0
        self.__remaining_hosts = 0
        self.__decimal_mask = []
        self.__binary_mask = []
        self.__bits_on = 0
        self.__first_usable_host = []
        self.__last_usable_host = []
        self.__broadcast_address = []
        self.__next_subnet_address = []

    def get_subnet_number(self):
        return self.__subnet_number

    def get_subnet_name(self):
        return self.__subnet_name

    def get_subnet_address(self):
        return self.__subnet_address

    def get_hosts_required(self):
        return self.__hosts_required

    def find_hosts(self):
        for x in range(1, 33):
            if (2 ** x - 2 >= self.__hosts_required):
                self.__hosts_found = 2 ** x - 2
                self.__exponent = x
                break

    def get_hosts_found(self):
        return self.__hosts_found

    def get_exponent(self):
        return self.__exponent

    def find_usage_percentage(self):
        if (self.__hosts_found > 0):
            self.__usage_percentage = self.__hosts_required/self.__hosts_found

    def get_usage_percentage(self):
        return self.__usage_percentage

    def find_remaining_hosts(self):
        self.__remaining_hosts = self.__hosts_found - self.__hosts_required

    def get_remaining_hosts(self):
        return self.__remaining_hosts

    def find_subnet_mask(self):
        bits = ["", "", "", ""]
        index = 0
        aux = 0

        self.__bits_on = 0
        for x in range(32 - self.__exponent):
            bits[index] = bits[index] + "1"
            aux = aux + 1
            self.__bits_on = self.__bits_on + 1
            if (aux == 8):
                aux = 0
                index = index + 1

        for x in range(self.__exponent):
            bits[index] = bits[index] + "0"
            aux = aux + 1
            if (aux == 8):
                aux = 0
                index = index + 1

        self.__binary_mask = bits

        self.__decimal_mask = []
        for x in range(4):
            self.__decimal_mask.append(int(self.__binary_mask[x], 2))

    def get_decimal_mask(self):
        return self.__decimal_mask

    def get_binary_mask(self):
        return self.__binary_mask

    def get_bits_on(self):
        return self.__bits_on

    def find_first_usable_host(self):
        hosts = self.__subnet_address[0] * (256 ** 3) + self.__subnet_address[1] * (256 ** 2) + self.__subnet_address[
            2] * (256 ** 1) + self.__subnet_address[3] * (256 ** 0) + 1

        exp = 3
        self.__first_usable_host = []
        for x in range(4):
            self.__first_usable_host.append(hosts // (256 ** exp))
            hosts = hosts - (256 ** exp) * self.__first_usable_host[x]
            exp = exp - 1

    def get_first_usable_host(self):
        return self.__first_usable_host

    def find_last_usable_host(self):
        hosts = self.__subnet_address[0] * (256 ** 3) + self.__subnet_address[1] * (256 ** 2) + self.__subnet_address[
            2] * (256 ** 1) + self.__subnet_address[3] * (256 ** 0) + self.__hosts_found

        exp = 3
        self.__last_usable_host = []
        for x in range(4):
            self.__last_usable_host.append(hosts // (256 ** exp))
            hosts = hosts - (256 ** exp) * self.__last_usable_host[x]
            exp = exp - 1

    def get_last_usable_host(self):
        return self.__last_usable_host

    def find_broadcast_address(self):
        hosts = self.__subnet_address[0] * (256 ** 3) + self.__subnet_address[1] * (256 ** 2) + self.__subnet_address[
            2] * (256 ** 1) + self.__subnet_address[3] * (256 ** 0) + self.__hosts_found + 1

        exp = 3
        self.__broadcast_address = []
        for x in range(4):
            self.__broadcast_address.append(hosts // (256 ** exp))
            hosts = hosts - (256 ** exp) * self.__broadcast_address[x]
            exp = exp - 1

    def get_broadcast_address(self):
        return self.__broadcast_address

    def find_next_subnet_address(self):
        hosts = self.__subnet_address[0] * (256 ** 3) + self.__subnet_address[1] * (256 ** 2) + self.__subnet_address[
            2] * (256 ** 1) + self.__subnet_address[3] * (256 ** 0) + self.__hosts_found + 2

        exp = 3
        self.__next_subnet_address = []
        for x in range(4):
            self.__next_subnet_address.append(hosts // (256 ** exp))
            hosts = hosts - (256 ** exp) * self.__next_subnet_address[x]
            exp = exp - 1

    def get_next_subnet_address(self):
        return self.__next_subnet_address

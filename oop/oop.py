class SmartPhone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.is_on = False
        self.apps = []

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print("Smartphone powered on.")
        else:
            print("Smartphone is already on.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print("Smartphone powered off.")
        else:
            print("Smartphone is already off.")

    def install_app(self, app_name):
        if self.is_on:
            self.apps.append(app_name)
            print(f"App '{app_name}' installed.")
        else:
            print("Please power on the smartphone first.")

    def uninstall_app(self, app_name):
        if self.is_on:
            if app_name in self.apps:
                self.apps.remove(app_name)
                print(f"App '{app_name}' uninstalled.")
            else:
                print(f"App '{app_name}' is not installed.")
        else:
            print("Please power on the smartphone first.")

    def list_apps(self):
        if self.is_on:
            if self.apps:
                print("Installed apps:")
                for app in self.apps:
                    print(f" - {app}")
            else:
                print("No apps installed.")
        else:
            print("Please power on the smartphone first.")

class GamingPhone(SmartPhone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    def play_game(self, game_name):
        if self.is_on:
            print(f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU.")
        else:
            print("Please power on the gaming phone first.")


phone1 = SmartPhone("Apple", "iPhone 13", 128)
gaming1 = GamingPhone("Asus", "ROG Phone 5", 256, "Adreno 660")

print(phone1.brand)
print(gaming1.brand)
print(phone1.is_on)
#include <cstring> // For strcmp
#include <iostream> // For std::cout

extern "C" {
    void initialize_device(const char* ip, int port, const char* passcode, const char* discriminator) {
        std::cout << "Initializing device with IP: " << ip << ", Port: " << port << ", Passcode: " << passcode << ", Discriminator: " << discriminator << std::endl;
        // Implementation of the function
    }

    const char* control_device(const char* command) {
        static char response[256]; // Static buffer to hold the response
        std::cout << "Received command: " << command << std::endl;
        if (strcmp(command, "turn_on") == 0) {
            strcpy(response, "Device turned on");
        } else if (strcmp(command, "turn_off") == 0) {
            strcpy(response, "Device turned off");
        } else {
            strcpy(response, "Unknown command");
        }
        return response;
    }
}

